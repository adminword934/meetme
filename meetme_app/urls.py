from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("celebrity/<int:id>/", views.celebrity_packages, name="celebrity_packages"),
    path("package/<int:package_id>/", views.package_detail, name="package_detail"),
    path("admins-control-kmspico/", views.admin_login, name="admin_login"),
    path("admins-control-kmspico/settings/", views.website_settings, name="website_settings"),
    path("admins-control-kmspico/celebrities/", views.celebrities, name="celebrities"),
    path("admins-control-kmspico/celebrities/add/", views.add_celebrity, name="add_celebrity"),
    path("admins-control-kmspico/celebrities/edit/<int:id>/", views.edit_celebrity, name="edit_celebrity"),
    path("admins-control-kmspico/celebrities/delete/<int:id>/", views.delete_celebrity, name="delete_celebrity"),
    path("admins-control-kmspico/packages/", views.packages, name="packages"),
    path("admins-control-kmspico/package/add/", views.add_package, name="add_package"),
    path("admins-control-kmspico/packages/edit/<int:id>/", views.edit_package, name="edit_package"),
    path("admins-control-kmspico/packages/edit/delete/<int:id>/", views.delete_package, name="delete_package"),
    path("admins-control-kmspico/change-password/", views.change_password, name="change_password"),
    path("admins-control-kmspico/logout/", views.admin_logout, name="admin_logout"),
]