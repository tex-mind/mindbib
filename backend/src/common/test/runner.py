from __future__ import annotations

import logging
import time
import unittest

from django.conf import settings
from django.test.runner import DiscoverRunner


class TimeLoggingTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_timings: list = []

    def startTest(self, test):
        self._test_started_at: float = time.time()
        super().startTest(test)

    def addSuccess(self, test):
        execution_time: float = time.time() - self._test_started_at
        test_name: str = self.getDescription(test)
        self.test_timings.append((test_name, execution_time))
        super().addSuccess(test)

    def getTestTimings(self):
        return self.test_timings


class TimeLoggingTestRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        self.slow_test_threshold: float = settings.SLOW_TEST_THRESHOLD
        logging.disable(logging.CRITICAL)
        super().__init__(*args, **kwargs)

    def run_suite(self, suite, **kwargs):
        result = super().run_suite(suite, **kwargs)

        if hasattr(result, "stream") and result.stream:
            self.display_slow_tests(result)

        return result

    def display_slow_tests(self, result):
        test_timings = self.get_resultclass().getTestTimings(result)
        slow_tests: list[tuple] = [
            (name, elapsed) for name, elapsed in test_timings if elapsed > self.slow_test_threshold
        ]

        if slow_tests:
            output_strings: list = []

            title_string: str = "Slow Tests (>{:.03}s):".format(self.slow_test_threshold)
            dashes_line: str = "-" * (len(title_string) + 4)

            result.stream.write("\n")

            output_strings.append(dashes_line)
            output_strings.append(f"| {title_string} |")
            output_strings.append(dashes_line)

            result.stream.writeln("\n".join(output_strings))

            for test_name, execution_time in slow_tests:
                result.stream.writeln("- ({:.03}s) {}".format(execution_time, test_name))

            result.stream.write("\n")

    def get_resultclass(self):
        return TimeLoggingTestResult
