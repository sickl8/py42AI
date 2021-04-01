from datetime import datetime
from recipe import Recipe


class Book:
    name = None
    last_update = None
    creation_date = None
    recipes_list = {
                        'starter': [],
                        'lunch': [],
                        'dessert': []
                   }

    def __init__(self, name):
        if not isinstance(name, str) or name == '':
            print('Book name should be a non-empty string')
            exit()
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date

    def get_recipe_by_name(self, name):
        """Print a recipe with the name`name`and return the instance"""
        pass
        for key in self.recipes_list:
            for recipe in self.recipes_list[key]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass
        if not isinstance(recipe_type, str):
            print('Recipe type should be a string')
            return None
        if not any(key == recipe_type for key in self.recipes_list):
            print('No such recipe type in book')
            return None
        for key in self.recipes_list:
            if key == recipe_type:
                ret = []
                for rc in self.recipes_list[key]:
                    ret.append(rc.name)
                return ret

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass
        if not isinstance(recipe, Recipe):
            print('Argument passed is not a Recipe')
            return None
        lst = self.recipes_list[recipe.recipe_type]
        if any(rc.name == recipe.name for rc in lst):
            print('Recipe with the same name already exists')
            return None
        lst.append(recipe)
        last_update = datetime.now()
