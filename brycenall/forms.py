from django.contrib.auth.forms import AuthenticationForm as AuthForm
from django.http import HttpRequest


class AuthenticationForm(AuthForm):
    def __init__(self, request: HttpRequest | None = None, *args, **kwargs) -> None:
        super().__init__(request, *args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "m-4 p-4 grow rounded bg-white text-gray-800"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "m-4 p-4 grow rounded bg-white text-gray-800"}
        )
