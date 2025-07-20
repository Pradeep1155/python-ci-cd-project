from app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Welcome to Visvasa" in response.data

def test_add():
    tester = app.test_client()
    response = tester.get('/add/2/3')
    assert b'Result: 5' in response.data

