class Recipe:
    def __init__(self, *args):
        self.recipe = list(args)

    def add_ingredient(self, ing):
        self.recipe.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.recipe:
            self.recipe.remove(ing)

    def get_ingredients(self):
        return tuple(self.recipe)

    def __len__(self):
        return len(self.recipe)


class Ingredient:
    def __init__(self, name: str, volume: float, measure: str):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'
