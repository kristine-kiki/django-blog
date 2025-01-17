from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is not valid")

    def test_form_is_not_valid_without_email(self):
       
        form = CollaborateForm({
            'name': 'Test User',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form should not be valid without the email field")

    def test_form_is_not_valid_without_message(self):
        
        form = CollaborateForm({
            'name': 'Test User',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form should not be valid without the message field")





