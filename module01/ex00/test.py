from recipe import Recipe
from book import Book

book = Book('Book of tomes')
recipe0 = Recipe('googaloo', 5, 900, ['glue', 'gab', 'garo'], 'idk', 'starter')
recipe1 = Recipe('googalo', 1, 900, ['glue', 'google', '4'], '', 'lunch')
book.add_recipe(recipe0)
book.add_recipe(recipe1)

lst = book.get_recipes_by_types
print(recipe0)
book.get_recipe_by_name('googalo')
print()
print(book.get_recipes_by_types('starter'))
print(book.get_recipes_by_types('lunch'))
