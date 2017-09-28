import unittest
from app import application, db
from app.auth.models import User
from flask_login import LoginManager, current_user


class MyTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = application.test_client()
        self.app.testing = True
        login_manager = LoginManager()
        login_manager.init_app(application)

    def tearDown(self):
        pass

    def test_user_in_db(self):
        user = User()
        user.alias = 'test'
        user.email = 'test@example.com'
        user.password = 'test'
        db.session.add(user)
        db.session.commit()
        self.assertNotEqual(None, User().get_user_by_email('test@example.com'))

        user = User().get_user_by_email('test@example.com')
        self.assertEqual(False, user.has_role('admin'))
        self.assertEqual(False, user.has_role('writer'))
        self.assertEqual(False, user.has_role('editor'))
        self.assertEqual([], user.get_roles())

        db.session.delete(user)
        db.session.commit()
        self.assertEqual(None, User().get_user_by_email('test@example.com'))

    def test_home_status_code(self):
        result = self.app.get('/about')
        self.assertEqual(result.status_code, 200)

    def test_blog_status_code(self):
        result = self.app.get('/blog')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
