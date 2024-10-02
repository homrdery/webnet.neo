from django.db import models
from django.db import models
class dirAddr(models.Model):
    mac_addr = models.CharField("mac_addr", max_length=32, null=False, unique=True, blank=False, help_text="mac адрес pc")
    name = models.CharField("name", max_length=30, null=False, blank=False, help_text="фио работника")

    def __str__(self):
        return f"Работник {self.id}:{self.mac_addr}:{self.name}"
    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

# Create your models here.
