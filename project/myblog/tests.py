from django.test import TestCase
from myblog.forms import ContactForm


class ContactFormTest(TestCase):

    def test_if_contact_form_is_filled(self):
        contact_form_data = {'name': 'name',
                             'email': 'email',
                             'phone': 'phone',
                             'message': 'message',
                             }
        contact_form = ContactForm(data=contact_form_data)
        self.assertTrue(contact_form.is_valid())
