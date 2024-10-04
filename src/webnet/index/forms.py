from django import forms
# from .models import worker, Pktreader
from django.forms import HiddenInput, ChoiceField
from crispy_forms.bootstrap import Modal
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Hidden, Button, Layout, Fieldset, Field, HTML, Reset, Row, Column
import logging

APPNAME = "client"
logger = logging.getLogger(APPNAME)

