from test_base import BaseRegistrationTest

class TestInputFields(BaseRegistrationTest):
    def test_required_input_fields(self):
        """Check all required input fields are present"""
        expected_ids = ['firstName', 'lastName', 'email', 'password', 'confirmPassword', 'location']
        for field_id in expected_ids:
            input_tag = self.form.find('input', {'id': field_id})
            self.assertIsNotNone(input_tag, f"Input field '{field_id}' is missing")
            self.assertTrue(input_tag.has_attr('required'), f"Input field '{field_id}' should be required")
