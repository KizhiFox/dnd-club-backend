from sqlalchemy import Boolean, Column, Integer, String

from app.db.base_class import Base


class InviteCode(Base):
    __tablename__ = 'invite_codes'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)
    uses_max = Column(Integer, nullable=False, default=-1)
    uses_count = Column(Integer, nullable=False, default=0)
    is_active = Column(Boolean, nullable=False, default=False)
