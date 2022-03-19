from django.http import HttpResponse
from django.shortcuts import render

from .utils.utils import get_current_date, check_date_in_table, update_table, get_stat
from .models import Stat


def index(request):
    current_date = get_current_date()
    in_table = check_date_in_table(current_date)
    if not in_table:
        update_table(current_date)

    data = get_stat(current_date)
    print("final answer: ", data)
    context = {
        "sick": data.sick,
        "sick_change": data.sick_change,
        "healed": data.healed,
        "healed_change": data.healed_change,
        }
    return render(request, 'main/index.html', context=context)

    
