from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login", view=views.LoginView.as_view(), name="login"),
    path("logout", view=views.log_out, name="logout"),
    path("signup", view=views.SignUpView.as_view(), name="signup"),
    path(
        "verify/<str:key>",
        view=views.complete_verification,
        name="complete-verification",
    ),
    path(
        "login/github",
        view=views.github_login,
        name="github-login",
    ),
]
