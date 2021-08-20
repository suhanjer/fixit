from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register_view, name="register"),
    path('points', views.points, name="points"),
    path('add_issue', views.add_issue, name="add_issue"),
    path('issue_page/<int:issue_id>', views.issue_page, name="issue_page"),
    path('update_coordinates/<int:issue_id>', views.update_coordinates, name="update_coordinates"),
    path('remove/<int:issue_id>', views.remove, name="remove"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)