from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.invite_code import InviteCode
from app.schemas.invite_code import InviteCode as InviteCodeSchema


class CRUDInviteCode(CRUDBase[InviteCode, InviteCodeSchema, InviteCodeSchema]):
    def is_code_active(self, db: Session, *, code: str) -> bool:
        db_code = db.query(InviteCode).filter(InviteCode.code == code).first()

        # if code not found
        if not db_code:
            return False

        # if code expired
        if db_code.uses_max != -1:
            if db_code.uses_count >= db_code.uses_max:
                return False

        return True

    def use_code(self, db: Session, *, code: str):
        db_code = db.query(InviteCode).filter(InviteCode.code == code).first()
        db_code.uses_count += 1
        db.add(db_code)
        db.commit()
        db.refresh(db_code)


invite_code = CRUDInviteCode(InviteCode)
