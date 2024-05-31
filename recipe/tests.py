from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Desserts")

    def test_category_iter(self):
        category_dict = dict(self.category)
        self.assertIn('name', category_dict)
        self.assertEqual(category_dict['name'], "Desserts")


class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            description="A rich chocolate cake",
            instructions="Mix and bake",
            ingredients="Flour, sugar, cocoa",
            category=self.category
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "Chocolate Cake")
        self.assertEqual(self.recipe.description, "A rich chocolate cake")
        self.assertEqual(self.recipe.instructions, "Mix and bake")
        self.assertEqual(self.recipe.ingredients, "Flour, sugar, cocoa")
        self.assertEqual(self.recipe.category, self.category)

    def test_recipe_str(self):
        self.assertEqual(str(self.recipe), "Chocolate Cake")
