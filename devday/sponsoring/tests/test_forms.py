from django.test import TestCase, override_settings

from event.models import Event
from sponsoring.forms import SponsoringContactForm


@override_settings(ROOT_URLCONF='sponsoring.tests.urls')
class SponsoringContactFormTest(TestCase):
    def setUp(self):
        self.event = Event.objects.current_event()

    def test_form_action(self):
        form = SponsoringContactForm(event=self.event)
        self.assertEqual(
            form.helper.form_action,
            '/sponsoring/{}/'.format(self.event.slug))

    def test_form_layout(self):
        pass
