from django.test import TestCase
from django.contrib.auth.models import User

from models import StudyGroup

class SimpleTest(TestCase):
    def test_user_add(self):
        u1 = User.objects.create(username='user1')
        u2 = User.objects.create(username='user2')
        u3 = User.objects.create(username='user3')
        sg = StudyGroup.objects.create(name='math')
        sg.users.add(u1, u2, u3)
        self.assertEquals(sg.users.count(), 3)
        sg.delete()
        User.objects.all().delete()
