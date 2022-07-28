import pytest
from app import create_app, db
from app.models import User


@pytest.fixture(scope='module')
def new_user():
    user = User(email='test@gmail.com', password='test123', name='joao')
    return user


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('instance/config_test.py')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user = User(email='test@gmail.com', password='test123', name='joao')
    user2 = User(email='test2@gmail.com', password='test321', name='paula')
    db.session.add(user)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login_post',
                     data=dict(email='test@gmail.com', password='test123'),
                     follow_redirects=True)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)
