from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("celebrity/<int:id>/", views.celebrity_packages, name="celebrity_packages"),
    path("package/<int:package_id>/", views.package_detail, name="package_detail"),
    path("admins/", views.admin_login, name="admin_login"),
    path("admins/settings/", views.website_settings, name="website_settings"),
    path("admins/celebrities/", views.celebrities, name="celebrities"),
    path("admins/celebrities/add/", views.add_celebrity, name="add_celebrity"),
    path("admins/celebrities/edit/<int:id>/", views.edit_celebrity, name="edit_celebrity"),
    path("admins/celebrities/delete/<int:id>/", views.delete_celebrity, name="delete_celebrity"),
    path("admins/packages/", views.packages, name="packages"),
    path("admins/package/add/", views.add_package, name="add_package"),
    path("admins/packages/edit/<int:id>/", views.edit_package, name="edit_package"),
    path("admins/packages/edit/delete/<int:id>/", views.delete_package, name="delete_package"),
    path("admins/change-password/", views.change_password, name="change_password"),
    path("admins/logout/", views.admin_logout, name="admin_logout"),
]