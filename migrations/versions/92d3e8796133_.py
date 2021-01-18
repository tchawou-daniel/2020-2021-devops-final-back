"""empty message

Revision ID: 92d3e8796133
Revises: 4e9f715114ee
Create Date: 2021-01-18 02:20:24.913051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92d3e8796133'
down_revision = '4e9f715114ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tagname', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.Binary(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('bio', sa.String(length=300), nullable=True),
    sa.Column('image', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('userprofile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.Text(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['userprofile.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('followers_assoc',
    sa.Column('follower', sa.Integer(), nullable=True),
    sa.Column('followed_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_by'], ['userprofile.user_id'], ),
    sa.ForeignKeyConstraint(['follower'], ['userprofile.user_id'], )
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['author_id'], ['userprofile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favoritor_assoc',
    sa.Column('favoriter', sa.Integer(), nullable=True),
    sa.Column('favorited_article', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorited_article'], ['article.id'], ),
    sa.ForeignKeyConstraint(['favoriter'], ['userprofile.id'], )
    )
    op.create_table('tag_assoc',
    sa.Column('tag', sa.Integer(), nullable=True),
    sa.Column('article', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['article'], ['article.id'], ),
    sa.ForeignKeyConstraint(['tag'], ['tags.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag_assoc')
    op.drop_table('favoritor_assoc')
    op.drop_table('comment')
    op.drop_table('followers_assoc')
    op.drop_table('article')
    op.drop_table('userprofile')
    op.drop_table('users')
    op.drop_table('tags')
    # ### end Alembic commands ###