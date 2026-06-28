import unittest
from service import app, db
from service.models import Account

class TestAccountService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        from service import talisman
        talisman.force_https = False
        cls.app = app.test_client()
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        with app.app_context():
            db.session.query(Account).delete()
            db.session.commit()

    def test_health_check(self):
        """health check"""
        resp = self.app.get('/accounts')
        self.assertEqual(resp.status_code, 200)

    def test_create_account(self):
        """create account"""
        resp = self.app.post('/accounts', json={"name": "Test", "email": "test@test.com"})
        self.assertEqual(resp.status_code, 201)

    def test_read_account(self):
        """read account"""
        resp = self.app.post('/accounts', json={"name": "Test", "email": "test@test.com"})
        account_id = resp.get_json()['id']
        resp = self.app.get(f'/accounts/{account_id}')
        self.assertEqual(resp.status_code, 200)

    def test_update_account(self):
        """update account"""
        resp = self.app.post('/accounts', json={"name": "Test", "email": "test@test.com"})
        account_id = resp.get_json()['id']
        resp = self.app.put(f'/accounts/{account_id}', json={"name": "Updated", "email": "test@test.com"})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()['name'], "Updated")

    def test_delete_account(self):
        """delete account"""
        resp = self.app.post('/accounts', json={"name": "Test", "email": "test@test.com"})
        account_id = resp.get_json()['id']
        resp = self.app.delete(f'/accounts/{account_id}')
        self.assertEqual(resp.status_code, 204)

    def test_list_accounts(self):
        """list accounts"""
        self.app.post('/accounts', json={"name": "Test1", "email": "test1@test.com"})
        self.app.post('/accounts', json={"name": "Test2", "email": "test2@test.com"})
        resp = self.app.get('/accounts')
        self.assertEqual(len(resp.get_json()), 2)

    def test_security_headers_check(self):
        """It should return security headers"""
        resp = self.app.get('/accounts')
        self.assertEqual(resp.headers.get('X-Frame-Options'), 'SAMEORIGIN')
        self.assertEqual(resp.headers.get('X-Content-Type-Options'), 'nosniff')

    def test_cors_check(self):
        """It should return a CORS header"""
        resp = self.app.get('/accounts')
        self.assertEqual(resp.headers.get('Access-Control-Allow-Origin'), '*')
