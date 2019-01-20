"""empty message

Revision ID: 4b0bb6c422ed
Revises: 4575283e75b3
Create Date: 2019-01-19 15:06:37.519789

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4b0bb6c422ed'
down_revision = '4575283e75b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.drop_column('question', 'creste_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('creste_time', mysql.DATETIME(), nullable=True))
    op.drop_column('question', 'create_time')
    # ### end Alembic commands ###
