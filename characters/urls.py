from django.urls import path

from characters.views import get_random_character_view


app_name = "characters"

urlpatterns = [
    path("characters/random/", get_random_character_view, name="character-random"),
]
