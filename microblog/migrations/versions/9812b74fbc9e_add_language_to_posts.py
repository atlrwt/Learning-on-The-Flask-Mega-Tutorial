"""add language to posts

Revision ID: 9812b74fbc9e
Revises: 432020d8bd14
Create Date: 2023-04-15 09:11:59.460972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9812b74fbc9e'
down_revision = '432020d8bd14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
