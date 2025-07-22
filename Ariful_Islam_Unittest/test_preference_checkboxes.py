from test_base import BaseRegistrationTest

class TestPreferenceCheckboxes(BaseRegistrationTest):
    def test_checkbox_preferences_exist(self):
        """Check optional checkboxes for 'offerHelp' and 'requestHelp'"""
        offer_checkbox = self.form.find('input', {'id': 'offerHelp'})
        request_checkbox = self.form.find('input', {'id': 'requestHelp'})
        self.assertIsNotNone(offer_checkbox, "'Offer help' checkbox is missing")
        self.assertIsNotNone(request_checkbox, "'Request help' checkbox is missing")
        self.assertEqual(offer_checkbox['type'], 'checkbox')
        self.assertEqual(request_checkbox['type'], 'checkbox')
