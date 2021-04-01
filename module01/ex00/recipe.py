class Recipe:
    name = ''
    cooking_lvl = 1
    cooking_time = 0
    ingredients = []
    description = ''
    recipe_type = ''
    valid_recipe_types = ["starter", "lunch", "dessert"]

    def __init__(self, name, ck_lvl, ck_time, ing, desc, recipe_t):
        if not isinstance(name, str) or name == '':
            print('Recipe name should be a non-empty string')
            exit()
        if not isinstance(ck_lvl, int) or ck_lvl > 5 or ck_lvl < 1:
            print('Cooking level should be an integer in the range [1, 5]')
            exit()
        if not isinstance(ck_time, int) or ck_time < 0:
            print('Cooking time should be a positive integer')
            exit()
        if (not isinstance(ing, list) or len(ing) == 0 or
           not all(isinstance(elem, str) and elem != '' for elem in ing)):
            print('Ingredients should be a non-empty list ' +
                  'consisting only of non-empty strings')
            exit()
        if not isinstance(desc, str):
            print('Description should be a string')
            exit()
        if (not isinstance(recipe_t, str) or not
           any(rt == recipe_t for rt in self.valid_recipe_types)):
            print('Recipe type should be either of these strings: ' +
                  str(self.valid_recipe_types))
            exit()
        self.name = name
        self.cooking_lvl = ck_lvl
        self.cooking_time = ck_time
        self.ingredients = ing
        self.description = desc
        self.recipe_type = recipe_t

    def __str__(self):
        ret = ''
        ret += 'Recipe name: ' + self.name + '\n'
        ret += 'Cooking level: ' + str(self.cooking_lvl) + '\n'
        ret += 'Cooking time: ' + str(self.cooking_time) + 'm\n'
        ret += 'Ingredients: ' + str(self.ingredients) + '\n'
        ret += 'Description: "' + self.description + '"\n'
        ret += 'Recipe type: ' + self.recipe_type
        return ret
