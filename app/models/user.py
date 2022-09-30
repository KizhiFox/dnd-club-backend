from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from app.db.base_class import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_superuser = Column(Boolean, nullable=False, default=False)
    invite_code = Column(Integer, ForeignKey('invite_codes.id'), ondelete='SET NULL')
