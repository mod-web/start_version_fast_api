import uuid
from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, UUID

metadata = MetaData()

orders = Table(
    'orders',
    metadata,
    Column('id',
           UUID(as_uuid=True),
           primary_key=True,
           default=uuid.uuid4,
           unique=True,
           nullable=False),
    Column('user_id',
           UUID(as_uuid=True),
           unique=True,
           nullable=False),
    Column('status', String),
    Column('created_at', TIMESTAMP, default=datetime.now()),
    Column('updated_at', TIMESTAMP, default=datetime.now()),
)