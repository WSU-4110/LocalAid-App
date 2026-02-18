from bs4 import BeautifulSoup
import unittest

class BaseRegistrationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("register.html", "r", encoding="utf-8") as f:
            cls.soup = BeautifulSoup(f.read(), 'html.parser')
            cls.form = cls.soup.find('form')
