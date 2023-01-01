from sqlalchemy import (
    Column,
    Integer,
    String,
)

from .database import db
from .mixins import (
    BaseMixin,
    CreatedMixin,
)


class Homework(db.Model, BaseMixin, CreatedMixin):
    name = Column(String(100))
    status = Column(String(100))
