from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Service, Barber, WorkingHours


class ServiceForm(forms.Form):  

    service = forms.ModelChoiceField(queryset=Service.objects.all(),
            widget=forms.Select(attrs={'hx-get': 'barbers/', 'hx-target': '#id_barber'}))
    barber = forms.ModelChoiceField(queryset=Barber.objects.none(),                                    
            widget=forms.Select(attrs={'hx-get': 'working_days/', 'hx-target': '#id_working_days'}))
    working_days = forms.ModelChoiceField(queryset=WorkingHours.objects.none())
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        #self.helper.form_action = reverse_lazy('index')
        # self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

        if 'service' in self.data:
            service_id = int(self.data.get('service'))
            self.fields['barber'].queryset = Barber.objects.filter(services = service_id) 

        if 'barber' in self.data:
            barber_id = int(self.data.get('barber'))
            self.fields['working_days'].queryset = WorkingHours.objects.filter(barber = barber_id)    

    class Meta:
        model = Service
        fields = ('name', )

