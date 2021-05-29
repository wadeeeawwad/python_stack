from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('start', views.start),
	path('guess', views.process),
	path('correct', views.correct),
	path('incorrect', views.incorrect),
	path('play-again', views.play_again),
	path('reset', views.reset),
	path('leaderboard', views.leaderboard),
	path('add-to-leaderboard', views.add_high_score)
]