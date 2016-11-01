from django.db import models

from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SnipcartSettings(BaseSetting):
    ApiKey = models.CharField(
        max_length=255,
        help_text='Your Snipcart Api Key'
    )
