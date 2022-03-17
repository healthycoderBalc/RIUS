from django import forms
from django.forms import widgets
from crispy_forms.helper import FormHelper

from .models import *

class ManuscriptForm(forms.ModelForm):

    documento_manuscrito = forms.FileField(
        label="prueba documento manuscrito",
        widget=widgets.FileInput(),
        help_text='with widgets.FileInput()'
    )
    helper = FormHelper()
    helper.use_custom_control = True

    class Meta:
        model = Manuscript
        fields = "__all__"
        exclude = ['edicion', 'autores', 'revisores', 'fecha_aceptado']

    def __init__(self, *args, **kwargs):
        # self.user = kwargs.pop('user', None)
        super(ManuscriptForm, self).__init__(*args, **kwargs)
        self.fields["fecha_recibido"].disabled = True  
