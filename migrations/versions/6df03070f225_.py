"""empty message

Revision ID: 6df03070f225
Revises: 5f299af02a3e
Create Date: 2021-02-08 14:39:53.812134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6df03070f225'
down_revision = '5f299af02a3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('endpoint', table_name='api_permissions')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('endpoint', 'api_permissions', ['endpoint'], unique=True)
    # ### end Alembic commands ###
