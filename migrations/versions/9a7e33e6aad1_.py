"""empty message

Revision ID: 9a7e33e6aad1
Revises: 
Create Date: 2023-03-08 14:22:50.768000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a7e33e6aad1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('captured',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('ability', sa.String(), nullable=True),
    sa.Column('base_experience', sa.Integer(), nullable=True),
    sa.Column('sprite_url', sa.String(), nullable=True),
    sa.Column('attack_base_stat', sa.Integer(), nullable=True),
    sa.Column('hp_base_stat', sa.Integer(), nullable=True),
    sa.Column('defense_base_stat', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('captured_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['captured_id'], ['captured.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team')
    op.drop_table('captured')
    # ### end Alembic commands ###
