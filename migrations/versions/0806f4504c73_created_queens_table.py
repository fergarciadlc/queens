"""created queens table

Revision ID: 0806f4504c73
Revises: 
Create Date: 2020-11-05 19:41:51.916596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0806f4504c73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('queens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('n', sa.Integer(), nullable=True),
    sa.Column('solutions', sa.Integer(), nullable=True),
    sa.Column('configurations', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('n')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('queens')
    # ### end Alembic commands ###
