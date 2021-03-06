"""Initial Migration

Revision ID: e6c132f604d1
Revises: 569aab85c922
Create Date: 2022-03-05 05:48:02.735877

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e6c132f604d1'
down_revision = '569aab85c922'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('image_file_1', sa.String(length=100), nullable=True))
    op.add_column('book', sa.Column('image_file_2', sa.String(length=100), nullable=True))
    op.add_column('book', sa.Column('image_file_3', sa.String(length=100), nullable=True))
    op.add_column('book', sa.Column('image_file_4', sa.String(length=100), nullable=True))
    op.drop_column('book', 'file_image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('file_image', mysql.VARCHAR(length=100), nullable=True))
    op.drop_column('book', 'image_file_4')
    op.drop_column('book', 'image_file_3')
    op.drop_column('book', 'image_file_2')
    op.drop_column('book', 'image_file_1')
    # ### end Alembic commands ###
