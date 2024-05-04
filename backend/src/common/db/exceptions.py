__all__ = ("RecordNotFoundError", "DuplicateRecordError")


class DatabaseError(Exception):
    MESSAGE = "db:error:base"
    ERROR_CODE = "DB_ERROR"

    def __init__(self, *args):
        self.code = self.ERROR_CODE
        self.message = f"{self.MESSAGE}: {args[0]}" if args else self.MESSAGE
        super(self).__init__(*args)


class RecordNotFoundError(Exception):
    MESSAGE = "db:record:error:not-found"
    ERROR_CODE = "RECORD_NOT_FOUND_ERROR"


class DuplicateRecordError(Exception):
    MESSAGE = "db:record:error:duplicate"
    ERROR_CODE = "DUPLICATE_RECORD_ERROR"
