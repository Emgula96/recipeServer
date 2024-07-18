from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Recipe
from .serializers import serialize_recipes
import json

@csrf_exempt
def recipe_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        return JsonResponse(serialize_recipes(recipes), safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        recipe = Recipe(
            title=data.get('title'),
            ingredients=data.get('ingredients'),
            instructions=data.get('instructions'),
            url=data.get('url')
        )
        recipe.save()
        return JsonResponse({
            'id': recipe.id,
            'title': recipe.title,
            'ingredients': recipe.ingredients,
            'instructions': recipe.instructions,
            'url': recipe.url,
        }, status=201)

    elif request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            recipe_id = data.get('id')
            recipe = Recipe.objects.get(pk=recipe_id)
            recipe.delete()
            return HttpResponse(status=204)
        except Recipe.DoesNotExist:
            return HttpResponse(status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
