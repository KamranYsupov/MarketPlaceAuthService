from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column

from .base_mixins import Base


class RefreshToken(Base):
    sub: Mapped[UUID] = mapped_column(index=True, unique=True)
    token: Mapped[str] = mapped_column(index=True)
    expires_in: Mapped[int]
