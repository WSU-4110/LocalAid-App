from test_base import BaseRegistrationTest

class TestTermsCheckbox(BaseRegistrationTest):
    def test_terms_checkbox_required(self):
        """Ensure 'terms' checkbox exists and is required"""
        terms_checkbox = self.form.find('input', {'id': 'terms'})
        self.assertIsNotNone(terms_checkbox, "'Terms' checkbox is missing")
        self.assertEqual(terms_checkbox.get('type'), 'checkbox')
        self.assertTrue(terms_checkbox.has_attr('required'), "'Terms' checkbox should be required")
