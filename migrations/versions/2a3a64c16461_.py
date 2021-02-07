"""empty message

Revision ID: 2a3a64c16461
Revises: b450755ffc4b
Create Date: 2021-02-07 18:20:06.028911

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2a3a64c16461'
down_revision = 'b450755ffc4b'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('backstage_roles', 'id',
                    existing_type=mysql.INTEGER(),
                    type_=mysql.INTEGER(unsigned=True),
                    existing_nullable=False)


def downgrade():
    op.alter_column('backstage_roles', 'id',
                    existing_type=mysql.INTEGER(unsigned=True),
                    type_=mysql.INTEGER(),
                    existing_nullable=False)
