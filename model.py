from sqlalchemy import (create_engine, Column, Integer, String, Numeric,
                        DateTime, Table, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class YudarlinnSegment(Base):
    __tablename__ = 'yudarlinn_segment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    stream_id = Column(String(255))
    segment_id = Column(String(255))
    segment_length = Column(Numeric(10, 6))
    segment_number = Column(Integer)
    link = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
