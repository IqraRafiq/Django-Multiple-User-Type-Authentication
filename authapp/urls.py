from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import SignUpView, home, alpha, bravo, charli


urlpatterns = [
    path('', login_required(home), name='home'),
    path('alpha', login_required(alpha), name='alpha'),
    path('bravo', login_required(bravo), name='bravo'),
    path('charli', login_required(charli), name='charli'),

]
