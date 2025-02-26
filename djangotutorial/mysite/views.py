from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import get_resolver, URLPattern, URLResolver
from .serializers import RouteSerializer
import os

def collect_routes(urlpatterns, base_path="", request=None):
    """
    Рекурсивно собирает все маршруты, включая вложенные через include()
    """
    routes = []
    for pattern in urlpatterns:
        if isinstance(pattern, URLPattern):
            if hasattr(pattern, 'name') and pattern.name:
                route_path = f"{base_path}{pattern.pattern}"
                routes.append({
                    'name': pattern.name,
                    'url': f"{get_base_url(request)}/{route_path}",
                    'pattern': str(route_path)
                })
        elif isinstance(pattern, URLResolver):
            new_base_path = f"{base_path}{pattern.pattern}"
            if hasattr(pattern, 'url_patterns'):
                routes.extend(collect_routes(pattern.url_patterns, new_base_path, request))
    return routes

def get_base_url(request=None):
    """
    Возвращает базовый URL в зависимости от окружения (локальный сервер или GitHub Codespaces)
    """
    if 'CODESPACE_NAME' in os.environ:
        codespace_name = os.environ.get('CODESPACE_NAME')
        return f"https://{codespace_name}-8000.app.github.dev"
    else:
        return "http://localhost:8000"  # Фиксированный хост

@api_view(['GET'])
def api_root(request):
    """
    Возвращает список всех доступных маршрутов API, включая вложенные через include()
    """
    url_resolver = get_resolver()
    all_routes = collect_routes(url_resolver.url_patterns, request=request)
    serializer = RouteSerializer(all_routes, many=True)
    return Response({
        'message': 'Список всех доступных маршрутов API',
        'routes': serializer.data,
        'total': len(all_routes)
    })