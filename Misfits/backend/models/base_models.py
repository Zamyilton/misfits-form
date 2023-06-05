from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Configure the SQLAlchemy connection
db_uri = 'mysql://root:root@localhost/Misfits'
engine = create_engine(db_uri)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

