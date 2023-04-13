from dataclasses import dataclass


@dataclass
class BaseProductUser:
    login: str
    password: str


@dataclass
class AdvancedIndividualNewUser(BaseProductUser):
    """ Пользователь с сотоянием по умолчанию. (Состояние не должно меняться в тестах) """
    login: str = "1902demo+753@gmail.com"
    password: str = "1"


@dataclass
class AdvancedIndividualUser(BaseProductUser):
    login: str = "2203demo@gmail.com"
    password: str = "1"


@dataclass
class AdvancedLegalUser(BaseProductUser):
    login: str = "1902demo@gmail.com"
    password: str = "1"


@dataclass
class MLSpaceUser(BaseProductUser):
    login: str = "2303demo+2@gmail.com"
    password: str = "1"
    user_id: str = "fa8043b5-b65b-410e-af5c-0f8ae4fb7ba1"
    customer_id: str = "2117e508-d285-4e75-9e5a-485949229fbb"


@dataclass
class Admin(BaseProductUser):
    login: str = "admin"
    password: str = "H6>*F3dX)9WEU"

@dataclass
class AdvancedIndividualNewStateUser(BaseProductUser):
    login: str = "advuser"
    password: str = "H6>*F3dX)9WEU"

