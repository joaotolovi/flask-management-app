from app.models import User, Owner, Cars

def test_new_user():
    user = User(email='test@gmail.com', password='test123', name='joao')
    assert user.email == 'test@gmail.com'
    assert user.password == 'test123'
    assert user.name == 'joao'
