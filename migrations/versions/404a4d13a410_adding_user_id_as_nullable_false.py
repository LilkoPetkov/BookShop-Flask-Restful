"""Adding user ID as nullable false

Revision ID: 404a4d13a410
Revises: c39aa26ec180
Create Date: 2023-03-19 17:37:51.749900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '404a4d13a410'
down_revision = 'c39aa26ec180'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('buyer_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('buyer_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###