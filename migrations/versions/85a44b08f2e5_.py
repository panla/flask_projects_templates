"""empty message

Revision ID: 85a44b08f2e5
Revises: c70cd6316bd2
Create Date: 2021-02-07 13:19:24.817178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85a44b08f2e5'
down_revision = 'c70cd6316bd2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('backstage_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False, comment='角色名称'),
    sa.Column('permissions_set', sa.String(length=200), nullable=False, comment='权限id,以,分割'),
    sa.Column('is_delete', sa.Boolean(), server_default=sa.text('0'), nullable=False, comment='删除标志'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    comment='后台管理系统角色表'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('backstage_roles')
    # ### end Alembic commands ###
