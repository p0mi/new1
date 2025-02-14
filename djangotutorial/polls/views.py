from django.shortcuts import render
from django.http import HttpResponse
from .nocodb_utils_v2 import get_users


def user_list(request):
    table_id = 'ms0ix9oy5vzfw4n'  # ID вашей таблицы
    try:
        records = get_users(table_id)
        print(records)
    except Exception as e:
        records = []
        print(e)
    
    context = {'records': records}
    return render(request, 'app/user_list.html', context)
# Create your views here.
