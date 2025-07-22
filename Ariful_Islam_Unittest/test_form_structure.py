from test_base import BaseRegistrationTest

class TestFormExists(BaseRegistrationTest):
    def test_form_exists(self):
        """Ensure registration form is present"""
        self.assertIsNotNone(self.form, "Registration form is missing")
