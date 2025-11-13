from django.urls import path
from blog import views
urlpatterns = [
    path("",views.index,name="homepage"),
    path("posts/", views.blog_listing,name="blog-listing-page"),
    path("posts/<slug:slug>", views.blog_details,name="blog-details-page")
]
