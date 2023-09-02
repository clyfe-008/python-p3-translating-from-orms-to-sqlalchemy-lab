from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

def create_table(base, engine):
    base.metadata.create_all(engine)

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()
