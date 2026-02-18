import unittest
from test_form_structure import TestFormExists
from test_input_fields import TestInputFields
from test_password_hint import TestPasswordHint
from test_terms_checkbox import TestTermsCheckbox
from test_social_buttons import TestSocialButtons
from test_preference_checkboxes import TestPreferenceCheckboxes

def test_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestFormExists))
    suite.addTests(loader.loadTestsFromTestCase(TestInputFields))
    suite.addTests(loader.loadTestsFromTestCase(TestPasswordHint))
    suite.addTests(loader.loadTestsFromTestCase(TestTermsCheckbox))
    suite.addTests(loader.loadTestsFromTestCase(TestSocialButtons))
    suite.addTests(loader.loadTestsFromTestCase(TestPreferenceCheckboxes))

    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite())
