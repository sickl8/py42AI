
cookbook = {
                'sandwich': {
                                'ingredients': ["ham", "bread", "cheese",
                                                "tomatoes"],
                                'meal': 'lunch',
                                'prep_time': 10
                            },
                'cake': {
                            'ingredients': ["flour", "sugar", "eggs"],
                            'meal': 'dessert',
                            'prep_time': 60
                        },
                'salad': {
                            'ingredients': ["avocado", "arugula", "tomatoes",
                                            "spinach"],
                            'meal': 'lunch',
                            'prep_time': 15
                         }
           }


def print_recipe(*args):
    if len(args) == 1 and isinstance(args[0], str):
        recipe_name = args[0]
    else:
        return
    if recipe_name in cookbook:
        print('Recipe for ' + recipe_name + ':')
        print('Ingredient list: ', end='')
        ingredients = cookbook[recipe_name]['ingredients']
        meal = cookbook[recipe_name]['meal']
        prep = cookbook[recipe_name]['prep_time']
        n_ing = len(ingredients)
        for itr in range(0, n_ing):
            print(ingredients[itr], end='')
            if itr < n_ing - 2 and itr != n_ing - 2:
                print(', ', end='')
            elif itr == n_ing - 2:
                print(' and ', end='')
        print('')
        print('To be eaten for ' + meal + '.')
        print('Takes ' + str(prep) + (' minutes' if prep != 1 else ' minute') +
              ' of cooking.')
    else:
        print('The recipe for ' + recipe_name + ' does not exist in cookbook')


def delete_recipe(*args):
    if len(args) == 1 and isinstance(args[0], str):
        recipe_name = args[0]
    else:
        return
    if recipe_name in cookbook:
        cookbook.pop(recipe_name)
        print('recipe for ' + recipe_name + ' deleted')
    else:
        print('the recipe for ' + recipe_name +
              ' does not exist in cookbook, nothing deleted')


def add_recipe(*args):
    if (len(args) == 4 and isinstance(args[0], str)
       and isinstance(args[1], list) and isinstance(args[2], str)
       and isinstance(args[3], int)):
        recipe_name = args[0]
        ingredients = args[1]
        meal_type = args[2]
        prep_time = args[3]
        for ingredient in ingredients:
            if not isinstance(ingredient, str):
                print('arg error')
                return
    else:
        print('arg error')
        return
    if recipe_name in cookbook:
        print('a recipe for ' + recipe_name + ' already exists in cookbook')
        return
    else:
        key = recipe_name
        value = {
                    'ingredients': ingredients,
                    'meal': meal_type,
                    'prep_time': prep_time
                }
        cookbook[key] = value
        print('added recipe for ' + recipe_name + ' to coobook')


def print_cookbook(*args):
    for recipe_name in cookbook:
        print_recipe(recipe_name)


def print_recipes():
    print('Cookbook contains ' + str(len(cookbook)) +
          (' recipes' if len(cookbook) != 1 else ' recipe'))
    itr = 0
    length = len(cookbook)
    for recipe_name in cookbook:
        print(recipe_name, end='')
        if itr < length - 1:
            print(', ', end='')
        itr += 1
    print('')


while True:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe\n" +
          "2: Delete a recipe\n" +
          "3: Print a recipe\n" +
          "4: Print the cookbook\n" +
          "5: Quit")
    inp = input(">> ")
    print('')
    if not inp.isnumeric() or int(inp) > 5 or int(inp) < 1:
        print("This option does not exist, " +
              "please type the corresponding number.\n" +
              "To exit, enter 5.")
    else:
        num = int(inp)
        if num == 1:
            recipe_name = input("Recipe for: ")
            if recipe_name in cookbook:
                print('Recipe for ' + recipe_name +
                      ' already exists in cookbook')
            else:
                n_ing = input("Number of ingredients: ")
                while not n_ing.isnumeric():
                    print("Please enter a number.")
                    n_ing = input("Number of ingredients: ")
                ingredients = []
                n_ing = int(n_ing)
                for itr in range(0, n_ing):
                    ing = input("Ingredient №" + str(itr + 1) + ': ')
                    ingredients.append(ing)
                meal = input("When this meal will be eaten: ")
                prep = input("Time to cook: ")
                while not prep.isnumeric():
                    print("Please enter a number.")
                    prep = input("Time to cook: ")
                add_recipe(recipe_name, ingredients, meal, int(prep))
        elif num == 2:
            recipe_name = input("What recipe do you want to delete? : ")
            delete_recipe(recipe_name)
        elif num == 3:
            print_recipe(input("Recipe to print: "))
        elif num == 4:
            print_recipes()
        else:
            print('Cookbook closed.')
            exit()
        print('')
