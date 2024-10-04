from django import forms
from .models import dirAddr, worker, Pktreader
from django.forms import HiddenInput, ChoiceField
from crispy_forms.bootstrap import Modal
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Hidden, Button, Layout, Fieldset, Field, HTML, Reset, Row, Column
import logging

APPNAME = "client"
logger = logging.getLogger(APPNAME)


def list_mac_addr():
    box = []
    for mac in Pktreader.objects.order_by('mac_addr').values_list('mac_addr', flat=True):
        items = worker.objects.filter(mac_addr = mac).values_list('id')
        if len(items) == 0:
            box.append((mac, mac))
    logger.error(box)
    return box

class addFormAddr(forms.ModelForm):
    action = forms.CharField(widget=forms.HiddenInput(), initial="subAddr", required=True)
    mac_addr = forms.ChoiceField(choices=list_mac_addr)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(Modal(Field('name'), Field('mac_addr'), Field('action'), Submit("submit", "Оправить", css_class='btn btn-primery float-end'),  css_id="addForm", title='Добавить новую запись'))

    class Meta:
        model = dirAddr
        fields = ('name', 'mac_addr')
class addForm(forms.ModelForm):
    action = forms.CharField(widget=forms.HiddenInput(), initial="sub", required=True)
    mac_addr = forms.ChoiceField(choices=list_mac_addr)
    # mac_addr = forms.CharField(widget=forms.Select(choices=list_mac_addr))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(Modal(Field('name'), Field('mac_addr'),Field('action'), Submit("submit", "Оправить", css_class='btn btn-primery float-end'),  css_id="addForm", title='обавить новую запись'))


    class Meta:
        model = worker
        fields = ('name', 'mac_addr', 'data')
