from pydantic import BaseModel


class InviteCodeBase(BaseModel):
    code: str
    uses_max: int
    uses_count: int
    is_active: bool


class InviteCode(InviteCodeBase):
    id: int

    class Config:
        orm_mode = True
