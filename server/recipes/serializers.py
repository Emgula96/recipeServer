from .models import Recipe
from typing import Iterable, List, Dict, Any

def serialize_recipes(recipes: Iterable[Recipe]) -> List[Dict[str, Any]]:
    data = []
    for recipe in recipes:
        data.append({
            'id': recipe.id,
            'title': recipe.title,
            'ingredients': recipe.ingredients,
            'instructions': recipe.instructions,
            'url': recipe.url,
        })
    return data
