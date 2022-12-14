"""first commit

Revision ID: 912ed29dc1a1
Revises: 
Create Date: 2022-09-26 16:39:30.426987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '912ed29dc1a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('nickname', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('nickname')
    )
    op.create_index(op.f('ix_user_nickname'), 'user', ['nickname'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_nickname'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
