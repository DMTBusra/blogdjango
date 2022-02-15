from django.urls import path
from blog.views import HomeView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns = [
     path('', HomeView.as_view(), name='home' ),
     path('blog_add', BlogCreateView, name='add' ),
     path('blog_detail/<int:id>', BlogDetailView, name='detail' ),
     path('blog_update/<int:pk>', BlogUpdateView.as_view(), name='update' ),
     path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='delete' ),
    
]