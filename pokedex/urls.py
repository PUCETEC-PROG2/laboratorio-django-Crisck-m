from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),
    path("trainers", views.trainers, name="trainers"),
    path("trainers/add", views.add_trainer, name="add_trainer"),  # Nueva ruta para agregar entrenador
    path("trainers/<int:trainer_id>/", views.trainer_details, name="trainer_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



