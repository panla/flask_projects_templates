"""empty message

Revision ID: 1235b64b600d
Revises: 
Create Date: 2021-01-24 18:08:07.637725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1235b64b600d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='创建时间'),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Boolean(), server_default=sa.text('0'), nullable=True, comment='删除标志'),
    sa.Column('cellphone', sa.String(length=12), nullable=False, comment='手机号'),
    sa.Column('name', sa.String(length=50), server_default='', nullable=False, comment='姓名'),
    sa.Column('nickname', sa.String(length=50), server_default='', nullable=False, comment='昵称'),
    sa.Column('password_hash', sa.String(length=300), nullable=False, comment='密码加密'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cellphone'),
    comment='账户表'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accounts')
    # ### end Alembic commands ###
