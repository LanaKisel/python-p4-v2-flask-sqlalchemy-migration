"""Initial migration.

Revision ID: 0775f090ee0b
Revises: 
Create Date: 2024-03-11 20:45:28.124572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0775f090ee0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###