from test_base import BaseRegistrationTest

class TestPasswordHint(BaseRegistrationTest):
    def test_password_hint_exists(self):
        """Check that password requirements hint is shown"""
        password_input = self.form.find('input', {'id': 'password'})
        hint = password_input.find_next('div', class_='form-text')
        self.assertIsNotNone(hint, "Password requirement hint is missing")
        self.assertIn("At least 8 characters", hint.text)
        self.assertIn("number", hint.text)
        self.assertIn("symbol", hint.text)
