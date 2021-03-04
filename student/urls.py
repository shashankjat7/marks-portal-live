from django.urls import path
from . import views
urlpatterns = [
    path('submit_marks/',views.submit_marks,name='submit_marks'),
    path('leaderboard/',views.leaderboard,name='leaderboard'),
    path('leaderboard_ascending/',views.leaderboard_ascending,name='leaderboard_ascending')
]