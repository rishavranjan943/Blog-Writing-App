from django.urls import path

from .views import *


app_name='core'
urlpatterns = [
    path('', index,name='index'),
    path('add-blog/', add_blog,name='add_blog'),
    path('my-blog/', my_blog,name='my_blog'),
    path('detail-blog/<int:id>/', detail_blog,name='detail_blog'),
    path('update-blog/<int:id>/', update_blog,name='update_blog'),
    path('delete-blog/<int:id>/', delete_blog,name='delete_blog'),
]
