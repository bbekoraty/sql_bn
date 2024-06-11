from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, event
from sqlalchemy.orm import relationship, backref
from .database import Base, SessionLocal

class Job(Base):
    __tablename__ = "Job"
    
    id = Column(Integer, primary_key=True, index=True)
    project = Column(String, nullable=False)
    uid = Column(String, nullable=False)
    string_tag = Column(String, nullable=False)
    hotspot_type = Column(String, nullable=False)
    max_temp = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    header = Column(String, nullable=True)
    worker = Column(String, nullable=True)
    status = Column(String, nullable=True, default="Pending")
    



