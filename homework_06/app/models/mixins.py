from datetime import datetime
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    func,
)
from sqlalchemy.orm import (
    declared_attr,
)


class CreatedMixin:
    created = Column(
        DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
        nullable=False,
    )


class BaseMixin:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)
