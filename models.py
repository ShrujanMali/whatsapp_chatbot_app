from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config

# url = URL.create(
#     drivername="postgresql",
#     username=config("DB_USER"),
#     password=config("DB_PASSWORD"),
#     host="localhost",
#     database="mydb",
#     port=5432
# )

# engine = create_engine(url)

DATABASE_URL = "sqlite:///mydb.sqlite"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    message = Column(String)
    response = Column(String)


Base.metadata.create_all(engine)