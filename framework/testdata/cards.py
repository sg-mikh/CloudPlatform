from dataclasses import dataclass


@dataclass(frozen=True)
class VisaCard:
    number: str = "4111 1111 1111 1111"
    month: int = 12
    year: int = 24
    cvv: int = 123
    secure_code: int = 12345678


@dataclass(frozen=True)
class MasterCard:
    number: str = "5555 5555 5555 5599"
    month: int = 12
    year: int = 24
    cvv: int = 123
