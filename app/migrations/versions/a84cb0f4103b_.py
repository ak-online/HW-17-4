"""empty message

Revision ID: a84cb0f4103b
Revises: a81267a1ac3a
Create Date: 2025-01-16 13:17:03.286835

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a84cb0f4103b'
down_revision: Union[str, None] = 'a81267a1ac3a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
