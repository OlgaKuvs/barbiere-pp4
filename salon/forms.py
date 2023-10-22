from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CustomerForm(UserCreationForm):
    username = forms.CharField(max_length=20, help_text=('Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.'))
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True        
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
        # self.helper.form_action = reverse_lazy('registration')        
        
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)               
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Login'))        

    class Meta:
        model = User
        fields = ['username', 'password']