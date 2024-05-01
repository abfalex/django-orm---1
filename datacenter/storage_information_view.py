from datetime import datetime
from django.utils import timezone
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def calc_spent_time():
    visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []

    for visit in visits:
        person_name = visit.passcard.owner_name
        entered_at = localtime(visit.entered_at)

        time_now = timezone.localtime(timezone.now())
        time_spent = time_now - entered_at

        total_seconds = int(time_spent.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60

        suspicion = total_seconds >= 3600

        non_closed_visits.append({
                'who_entered': person_name,
                'entered_at': entered_at,
                'duration': f'{hours:02}:{minutes:02}',
                'is_strange': suspicion
            })

    return non_closed_visits


def storage_information_view(request):
    non_closed_visits = calc_spent_time()

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }

    return render(request, 'storage_information.html', context)
