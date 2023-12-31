"""05_added_cascade_delete

Revision ID: 79c401c10044
Revises: f5faae5208ff
Create Date: 2023-09-27 15:02:11.029302

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79c401c10044'
down_revision: Union[str, None] = 'f5faae5208ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('visit', 'url_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('visit_url_id_fkey', 'visit', type_='foreignkey')
    op.create_foreign_key(None, 'visit', 'url', ['url_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'visit', type_='foreignkey')
    op.create_foreign_key('visit_url_id_fkey', 'visit', 'url', ['url_id'], ['id'])
    op.alter_column('visit', 'url_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
