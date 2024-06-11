from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker,declarative_base


DATABASE_URL = "postgresql://postgres:droneai888@localhost:5432/singledb"  

engine = create_engine(DATABASE_URL,echo = True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

metadata = Base.metadata
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()