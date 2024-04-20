from django.urls import path
from .views import blogCategory, blogDetail, indexView

urlpatterns = [
    path("", indexView, name="blog_index"),
    path("post/<int:pk>/", blogDetail, name="blog_detail"),
    path("category/<category>/", blogCategory, name="blog_category"),
]