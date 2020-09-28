from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Friends
# Create your tests here.

class FriendsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='Ross', password='password')
        test_user.save()

        test_post = Friends.objects.create(
            character = test_user,
            line = 'WE WERE ON A BREAK',
            plot = 'Ross and Rachel on a break',
            episode = '15',
            season = '3',

        )
        test_post.save() # Save the object to mock Database

    def test_friends_content(self):
        friends = Friends.objects.get(id=1)
        actual_character = str(friends.character)
        actual_line = str(friends.line)
        actual_plot = str(friends.plot)
        actual_episode = str(friends.episode)
        actual_season = str(friends.season)

        self.assertEqual(actual_character, 'Ross')
        self.assertEqual(actual_line, 'WE WERE ON A BREAK')
        self.assertEqual(actual_plot, 'Ross and Rachel on a break')
        self.assertEqual(actual_episode, '15')
        self.assertEqual(actual_season, '3')

