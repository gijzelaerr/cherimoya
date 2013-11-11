import os
import cherimoya
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, cherimoya.app.config['DATABASE'] = tempfile.mkstemp()
        cherimoya.app.config['TESTING'] = True
        self.app = cherimoya.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(cherimoya.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()