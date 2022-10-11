from django.urls import path
from .views import GraphicPageView, GraphicPostView, GraphicPostLoseView

urlpatterns = [
    path('', GraphicPageView.as_view(), name='GraphicPage'),
    path('postGain', GraphicPostView.as_view(), name='GraphicPostGainPage'),
    path('postLose', GraphicPostLoseView.as_view(), name='GraphicPostLosePage'),
]