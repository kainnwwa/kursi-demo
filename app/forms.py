from django.contrib.auth.forms import UserCreationForm
from .models import UserWithPhone

class UserWithPhoneCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserWithPhone
        fields = ("username", "phone")