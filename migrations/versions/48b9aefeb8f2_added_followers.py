"""added followers

Revision ID: 48b9aefeb8f2
Revises: 240047bca186
Create Date: 2021-02-13 01:02:21.464828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48b9aefeb8f2'
down_revision = '240047bca186'
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
