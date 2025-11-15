"""Exception classes for marketing-spec-kit"""


class MarketingSpecError(Exception):
    """Base exception for all marketing-spec-kit errors"""

    def __init__(self, code: str, message: str, fix: str = ""):
        self.code = code
        self.message = message
        self.fix = fix
        super().__init__(f"[{code}] {message}")


class ParseError(MarketingSpecError):
    """Error during specification parsing"""

    pass


class ValidationError(MarketingSpecError):
    """Error during specification validation"""

    def __init__(
        self,
        code: str,
        message: str,
        entity: str = "",
        field: str = "",
        value: any = None,
        fix: str = "",
    ):
        self.entity = entity
        self.field = field
        self.value = value
        super().__init__(code, message, fix)

