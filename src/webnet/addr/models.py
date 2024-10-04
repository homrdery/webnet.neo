from django.db import models
from django.db import models
from django.utils import timezone


class dirAddr(models.Model):
    mac_addr = models.CharField("mac_addr", max_length=32, null=False, unique=True, blank=False,
                                help_text="mac адрес pc")
    name = models.CharField("name", max_length=30, null=False, blank=False, help_text="фио работника")

    def __str__(self):
        return f"Работник {self.id}:{self.mac_addr}:{self.name}"

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"


class worker(models.Model):
    mac_addr = models.CharField("mac_addr", max_length=32, null=False, unique=True, blank=False,
                                help_text="mac адрес pc")
    ip_addr = models.CharField("ip_addr", max_length=30, default="--", null=False, blank=False, help_text="ip_addr pc")
    name = models.CharField("name", max_length=30, null=True, default="--", blank=False, help_text="name")
    vendor = models.CharField("vendor", max_length=30, null=True, default="--", blank=False, help_text="vendor")

    def __str__(self):
        return f"Работник {self.id}:{self.mac_addr}:{self.ip_addr}:{self.name}:{self.vendor}"

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"


class Pktreader(models.Model):
    mac_addr = models.CharField("mac_addr", max_length=32, null=False, blank=False, primary_key=True,
                                help_text="mac адрес pc")
    ip_addr = models.CharField("ip_addr", max_length=32, null=False, blank=False, help_text="ip адрес pc", default="--")
    time = models.DateTimeField("time", null=False, help_text="Время обнуружения pc", default=timezone.now)

    def __str__(self):
        return f"компьютер {self.mac_addr}:{self.ip_addr}:{self.time}"

    class Meta:
        verbose_name = "компьютер"
        verbose_name_plural = "компьютеры"


class PktRecordLogManager(models.Manager):
    def compute(self):
        objs = self.filter(type=1).order_by("time")
        for obj in objs:
            mac_addr = obj.data["hwsrc"]
            ip_addr = obj.data["psrc"]
            time = obj.time
            rec, created = Pktreader.objects.get_or_create(mac_addr=mac_addr)
            rec.time = time
            rec.ip_addr = ip_addr
            rec.save()


class PktRecordLog(models.Model):
    objects = PktRecordLogManager()
    type = models.IntegerField("Тип", null=False, help_text="Тип записи")
    data = models.JSONField("Данные", null=False, help_text="Данные пакета")
    time = models.DateTimeField("Время", null=False, help_text="Время добавления")

    def __str__(self):
        return f"пакет ({self.id}) {self.data}:{self.time}"

    class Meta:
        verbose_name = "пакет"
        verbose_name_plural = "пакеты"

# Create your models here.
