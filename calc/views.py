from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import safe_eval


def index(request):
    return render(request, 'calc/index.html')


@csrf_exempt
def evaluate(request):
    if request.method == 'POST':
        expr = request.POST.get('expr', '')
        try:
            result = safe_eval(expr)
            return JsonResponse({'result': str(result)})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Only POST allowed'}, status=405)
