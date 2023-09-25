from src.crud.base import CRUDBase
from src.models import Url


class CRUDUrl(CRUDBase[Url, None, None]):
    pass


url = CRUDUrl(Url)