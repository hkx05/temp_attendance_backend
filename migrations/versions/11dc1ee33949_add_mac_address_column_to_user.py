"""Add mac_address column to User

Revision ID: 11dc1ee33949
Revises: d1cd543b2cd3
Create Date: 2024-10-29 15:57:13.400371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11dc1ee33949'
down_revision = 'd1cd543b2cd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('logs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mac_address', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('logs', schema=None) as batch_op:
        batch_op.drop_column('mac_address')

    # ### end Alembic commands ###
