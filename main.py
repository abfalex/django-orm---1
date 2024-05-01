import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь

    print(len(Passcard.objects.filter(is_active=True)))
    user = Passcard.objects.all()[1]
    print(Visit.objects.filter(passcard=user.passcode))
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
