from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    lastname = forms.CharField(max_length=50, label="Kullanıcı Soyadi")
    email    = forms.EmailField(max_length=64, label="Email")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)




    def clean(self):
        username = self.cleaned_data.get("username")
        lastname = self.cleaned_data.get("lastname")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")




        values = {
            "username": username,
            "lastname": lastname,
            "password": password,
            "email": email,

        }
        return values


