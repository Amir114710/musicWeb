from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':" username" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':"password" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"}))    

class RegisterationForm(forms.Form):
    username = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':" Username" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':"Password" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"}))    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':" RepeatPassword" , 'required' : "required" , 'autocomplete' : "on" , 'oninvalid' : "setCustomValidity('پر کردن این فیلد ضروری است.')" , 'onkeyup' : "setCustomValidity('')"}))    


    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if password2 != password:
            raise forms.ValidationError('this passwords are not same')
        # user = User.objects.create_user(username = self.cleaned_data.get('username'), password = self.cleaned_data.get('password') ,  email = self.cleaned_data.get('email'))
