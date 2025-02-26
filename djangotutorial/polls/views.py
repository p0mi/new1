from django.views.generic import TemplateView
from django.http import HttpResponse
from .nocodb_utils_v2 import get_users
from rest_framework import generics
from .models import Virtuals
from .serializers import ItemSerializer

class UserListView(TemplateView):
    template_name = 'app/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table_id = 'ms0ix9oy5vzfw4n'  # ID вашей таблицы
        try:
            records = get_users(table_id)
            print(records)
        except Exception as e:
            records = []
            print(e)
        
        context['records'] = records
        return context
# Create your views here.

class VirtualsListCreate(generics.ListCreateAPIView):
    queryset = Virtuals.objects.all()
    serializer_class = ItemSerializer

class VitualsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Virtuals.objects.all()
    serializer_class = ItemSerializer
