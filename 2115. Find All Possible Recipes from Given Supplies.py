class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph, can_make, supplies = {recipe : [] for recipe in recipes}, {}, set(supplies)
        def dfs(recipe):
            if recipe not in can_make:
                can_make[recipe] = False
                can_make[recipe] = all(dfs(ingr) for ingr in graph[recipe])
            return can_make[recipe]
        
        for i,recipe in enumerate(recipes):
            for ingr in ingredients[i]:
                if ingr not in supplies:
                    graph[recipe].append(ingr if ingr in graph else recipe)
        return [recipe for recipe in recipes if dfs(recipe)]
