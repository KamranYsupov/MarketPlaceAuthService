from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_mixins import AbstractUser, TimestampedMixin


class User(AbstractUser, TimestampedMixin):
    """Модель пользователя"""

    bill: Mapped[float] = mapped_column(default=0)
