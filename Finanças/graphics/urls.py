from django.urls import path
from .views import GraphicPageView, GraphicPostView

urlpatterns = [
    path('', GraphicPageView.as_view(), name='GraphicPage'),
    path('CreateGraphic', GraphicPostView.as_view(), name='GraphicPostPage')
]