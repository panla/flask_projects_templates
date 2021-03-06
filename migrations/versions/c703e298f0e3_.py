"""empty message

Revision ID: c703e298f0e3
Revises: 2d20d33364b1
Create Date: 2021-03-07 19:51:17.823529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c703e298f0e3'
down_revision = '2d20d33364b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_api_permissions_parent_id'), 'api_permissions', ['parent_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_api_permissions_parent_id'), table_name='api_permissions')
    # ### end Alembic commands ###
