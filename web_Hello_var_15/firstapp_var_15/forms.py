from django.forms import Form
from django.forms import CharField

class UserForm(Form):
     name = CharField(label="Имя клиента")
     surname = CharField(label="Фамилия клиента")
