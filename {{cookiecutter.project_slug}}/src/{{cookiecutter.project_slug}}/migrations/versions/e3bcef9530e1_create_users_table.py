"""create users table.

Revision ID: e3bcef9530e1
Revises: 
Create Date: 2019-09-08 21:20:11.257500

"""
from alembic import op
from sqlalchemy.dialects import postgresql

import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "e3bcef9530e1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():  # noqa: D103
    op.create_table(
        "users",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("username", sa.String, nullable=False),
        sa.Column("password_hash", sa.String, nullable=False),
        sa.Column("bio", sa.Unicode, nullable=True),
        sa.Column("image", sa.String, nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("email", name=op.f("uq_users_email")),
        sa.UniqueConstraint("username", name=op.f("uq_users_username")),
    )


def downgrade():  # noqa: D103
    op.drop_table("users")
