"""empty message

Revision ID: ca44a3bae068
Revises: 9f03bd247fc5
Create Date: 2021-02-07 10:33:03.459672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca44a3bae068'
down_revision = '9f03bd247fc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_accounts_name'), 'accounts', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_accounts_name'), table_name='accounts')
    # ### end Alembic commands ###
