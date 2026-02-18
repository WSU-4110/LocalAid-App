from test_base import BaseRegistrationTest

class TestSocialButtons(BaseRegistrationTest):
    def test_social_buttons_exist(self):
        """Verify Google and Facebook social login buttons exist"""
        social_buttons = self.form.find_all('button', class_='btn-outline-primary')
        self.assertEqual(len(social_buttons), 2, "There should be exactly two social login buttons")

        google_button = next((btn for btn in social_buttons if "Google" in btn.text), None)
        facebook_button = next((btn for btn in social_buttons if "Facebook" in btn.text), None)

        self.assertIsNotNone(google_button, "Google login button missing")
        self.assertIsNotNone(facebook_button, "Facebook login button missing")
