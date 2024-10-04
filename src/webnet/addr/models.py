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

class worker(models.Model):
    mac_addr = models.CharField("mac_addr", max_length=32, null=False, unique=True, blank=False, help_text="mac адрес pc")
    name = models.CharField("name", max_length=30, null=False, blank=False, help_text="фио работника")
    data = models.JSONField("Данные",  help_text="Доп данные")

    def __str__(self):
        return f"Работник {self.id}:{self.mac_addr}:{self.name}:{self.data}"
    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

class Pktreader(models.Model):
    mac_addr = models.CharField("mac_addr", max_length=32, null=False, blank=False, primary_key=True, help_text="mac адрес pc")
    ip_addr = models.CharField("ip_addr", max_length=32, null=False, blank=False, help_text="ip адрес pc")
    time = models.DateTimeField("time", null=False, help_text="Время обнуружения pc")
    def __str__(self):
        return f"компьютер {self.mac_addr}:{self.ip_addr}:{self.time}"
    class Meta:
        verbose_name = "компьютер"
        verbose_name_plural = "компьютеры"

# Create your models here.
