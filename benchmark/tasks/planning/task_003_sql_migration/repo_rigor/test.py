import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

def test_main():
    engine = create_engine('sqlite:///app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new user
    new_user = User(name='Test User')
    session.add(new_user)
    session.commit()

    # Query the user
    user = session.query(User).filter_by(name='Test User').first()
    assert user is not None
    assert user.name == 'Test User'

    # Cleanup
    session.delete(user)
    session.commit()
    session.close()
