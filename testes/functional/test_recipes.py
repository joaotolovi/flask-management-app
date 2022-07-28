from app import create_app


def test_home_page():
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check if redirected to login page 
    """
    flask_app = create_app('instance/config_test.py')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 302
        #assert "Login" in response.data

def test_login_page():
    """
    GIVEN a Flask application
    WHEN the '/login' page is requested (GET)
    THEN check if login page loaded
    """
    flask_app = create_app('instance/config_test.py')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/login')
        assert response.status_code == 200
        assert b"Login" in response.data