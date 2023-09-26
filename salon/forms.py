from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Service, Barber, WorkingHours




# class ServiceForm(forms.Form):  

#     service = forms.ModelChoiceField(queryset=Service.objects.all(), label='Services',
#               empty_label=None, 
#               widget=forms.Select(attrs={'hx-get': 'barbers/', 'hx-trigger': 'change',
#                                          'hx-target': '#id_barber', }))
#     barber = forms.ModelChoiceField(queryset=Barber.objects.none(),  label='Barbers',                                  
#             widget=forms.Select(attrs={'hx-get': 'working_days/', 'name':'barber',
#                                        'hx-trigger': 'change', 
#                                        'hx-target': '#id_working_days' }))
#     working_days = forms.ModelChoiceField(
#                     queryset=WorkingHours.objects.none(), 
#                     label='Dates and times') 
    

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.add_input(Submit('submit', 'Submit'))
#         self.helper.form_action = reverse_lazy('saveform')
#         self.helper.form_method = 'POST'  

#         if 'service' in self.data:
#             service_id = int(self.data.get('service'))      
#             self.fields['barber'].queryset = Barber.objects.filter(services = service_id)      
            

#         if 'barber' in self.data:
#             barber_id = int(self.data.get('barber'))
#             self.fields['working_days'].queryset = WorkingHours.objects.filter(
#                                                     barber=barber_id) 
          
                    
#     class Meta:
#         model = Service
#         fields = ('name',)

