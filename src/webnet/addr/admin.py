from django.contrib.admin import register, ModelAdmin
from .models import *
@register(dirAddr)
class dirAddr(ModelAdmin):
    list_display = ("name", "mac_addr")
    search_fields = ('mac_addr', 'name')
    list_filter = ("mac_addr", )

# Register your models here.
@register(Pktreader)
class PktreaderAdmin(ModelAdmin):
    # pass
    list_display = ("mac_addr", "ip_addr", "time")
    search_fields = ('mac_addr', 'ip_addr')

@register(worker)
class WorkerAdmin(ModelAdmin):
    list_display = ("name", "mac_addr", "data")
    search_fields = ('mac_addr', 'name')
    list_filter = ("mac_addr", )
