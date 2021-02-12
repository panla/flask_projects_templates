"""empty message

Revision ID: 2d20d33364b1
Revises: 5db203661a44
Create Date: 2021-02-12 09:26:38.582904

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2d20d33364b1'
down_revision = '5db203661a44'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('backstage_roles', 'id',
                    existing_type=mysql.INTEGER(unsigned=True),
                    existing_nullable=False,
                    autoincrement=True
                    )


def downgrade():
    pass
