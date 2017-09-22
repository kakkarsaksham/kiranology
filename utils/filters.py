from django.contrib.auth.models import User
import rest_framework_filters as drf_filters

from apps.core.models import *


class UserFilterSet(drf_filters.FilterSet):
    class Meta:
        model = User
