"""Initial

Revision ID: e7df5f624b31
Revises: 5edb6f324115
Create Date: 2025-01-16 13:56:17.259021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7df5f624b31'
down_revision: Union[str, None] = '5edb6f324115'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
