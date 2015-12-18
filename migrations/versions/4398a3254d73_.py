"""empty message

Revision ID: 4398a3254d73
Revises: None
Create Date: 2015-06-15 15:50:35.167699

"""

# revision identifiers, used by Alembic.
revision = '4398a3254d73'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_time', sa.Time(), nullable=True),
    sa.Column('place', sa.String(length=128), nullable=True),
    sa.Column('descriptions', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('skype_login', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game_date',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_date', sa.Date(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('players',
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['game.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('players')
    op.drop_table('game_date')
    op.drop_table('user')
    op.drop_table('player')
    op.drop_table('game')
    ### end Alembic commands ###
