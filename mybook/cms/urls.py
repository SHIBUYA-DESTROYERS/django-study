from django.conf.urls import url
from cms import views

urlpatterns = [
    # 書籍
    url(r'book/$', views.book_list, name='book_list'),
    url(r'book/add/$', views.book_edit, name='book_add'),
    url(r'book/mod/(?P<book_id>\d+)/$', views.book_edit, name='book_mod'),
    url(r'book/del/(?P<book_id>\d+)/$', views.book_del, name='book_del'),
]

