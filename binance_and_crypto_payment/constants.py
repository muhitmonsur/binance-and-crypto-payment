class StatusCode:
    SUCCESS = 2040
    ALREADY_PROCESSED = 2041

    AUTH_ERROR = 2030
    AUTH_FORMAT_ERROR = 2031

    VALIDATION_ERROR = 2050
    ORDER_NOT_FOUND = 2051
    TRANSACTION_NOT_FOUND = 2052
    INVALID_STATUS = 2054

    INTERNAL_ERROR = 5000

    # ✅ New code for cancelled orders
    ORDER_CANCELLED = 20000

    # ✅ Optional: raw gateway OK status
    STATUS_CODE_OK = 200