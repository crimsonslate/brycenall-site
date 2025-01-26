from django.contrib.auth.forms import AuthenticationForm as AuthForm
from django.http import HttpRequest


class AuthenticationForm(AuthForm):
    error_messages = {"invalid_login": "couldn't find that user, please try again"}

    def __init__(self, request: HttpRequest | None = None, *args, **kwargs) -> None:
        super().__init__(request, *args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "p-2 w-full block bg-gray-600 text-gray-50"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "p-2 w-full block bg-gray-600 text-gray-50"}
        )
