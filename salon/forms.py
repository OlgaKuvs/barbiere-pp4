from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Service, Barber


class ServiceForm(forms.Form):   
    service = forms.ModelChoiceField(queryset=Service.objects.all(),
            widget=forms.Select(attrs={'hx-get': 'load_barbers/', 'hx-target': '#id_barber'}))
    
    barber = forms.ModelChoiceField(queryset=Barber.objects.none())
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        #self.helper.form_action = reverse_lazy('index')
        # self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

        if 'service' in self.data:
            service_id = int(self.data.get('service'))
            self.fields['barber'].queryset = Barber.objects.filter(services = service_id)    

    class Meta:
        model = Service
        fields = ('name', )

