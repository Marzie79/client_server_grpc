from uuid import uuid4

from django.db import models
from django_lifecycle import LifecycleModelMixin, hook, AFTER_UPDATE


class Stuff(LifecycleModelMixin, models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=150)
    service = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'service'
        verbose_name = 'stuff'

    def __str__(self):
        return self.name

    @hook(AFTER_UPDATE)
    def on_update(self):
        print("hererrer")
        print(self.initial_value('name'))
        print(self.name)
