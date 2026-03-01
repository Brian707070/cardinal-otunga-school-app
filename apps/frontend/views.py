from django.shortcuts import render
from django.http import HttpResponseRedirect

# mimic the flask behaviour
YOUTUBE_ID = "dQw4w9WgXcQ"


def home(request):
    query = request.GET.get('q', '')
    engine = request.GET.get('engine', 'bing')
    results = []
    if query:
        results = [f"{engine.capitalize()} result for '{query}' #1", f"{engine.capitalize()} result for '{query}' #2"]
    return render(request, 'frontend/home.html', {
        'youtube_id': YOUTUBE_ID,
        'bing_results': results,
        'query': query,
        'engine': engine,
    })
