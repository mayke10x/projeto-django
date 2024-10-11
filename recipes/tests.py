from django.test import TestCase

from django.url import reverse

class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        recipe_home_url = reverse('recipes:home')
        self.assertEqual(recipe_home_url, '/')

    