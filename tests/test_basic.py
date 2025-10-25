from app import app
import os


def test_status():
    client = app.test_client()
    rv = client.get('/status')
    assert rv.status_code == 200
    assert rv.get_json() == {'ok': True}


def test_coach_unauthorized():
    client = app.test_client()
    rv = client.post('/coach', json={'event':'morning'})
    assert rv.status_code == 401


def test_coach_authorized():
    client = app.test_client()
    os.environ['COACH_WEBHOOK_SECRET'] = 'test-secret'
    rv = client.post('/coach', headers={'X-Auth': 'test-secret'}, json={'event':'morning'})
    assert rv.status_code == 200
    data = rv.get_json()
    assert 'coach_message' in data
