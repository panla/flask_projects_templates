"""empty message

Revision ID: f31c9658523c
Revises: 2a3a64c16461
Create Date: 2021-02-07 18:23:42.167595

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f31c9658523c'
down_revision = '2a3a64c16461'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('backstage_accounts', 'role_id',
                    existing_type=mysql.INTEGER(),
                    type_=mysql.INTEGER(unsigned=True),
                    existing_nullable=False)


def downgrade():
    op.alter_column('backstage_accounts', 'role_id',
                    existing_type=mysql.INTEGER(unsigned=True),
                    type_=mysql.INTEGER(),
                    existing_nullable=False)
