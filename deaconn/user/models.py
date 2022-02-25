from django.db import models
from django.contrib.auth.models import User

import random
import string

from django.core.files.storage import default_storage

def file_path(instance, filename):
    pstr = ''

    while True:
        pstr = ''.join(random.choices(string.ascii_letters + string.digits, k = 8))

        if not default_storage.exists(pstr):
            break

    return 'users/' + pstr + '.' + filename.rsplit('.', 1)[1]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(verbose_name = "Avatar", upload_to = file_path)
