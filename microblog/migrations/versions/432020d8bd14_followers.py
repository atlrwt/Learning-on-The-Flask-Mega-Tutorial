"""followers

Revision ID: 432020d8bd14
Revises: 10c96051b792
Create Date: 2023-04-11 15:59:29.013485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '432020d8bd14'
down_revision = '10c96051b792'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
