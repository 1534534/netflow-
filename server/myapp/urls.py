from django.urls import path

from myapp import views

app_name = 'myapp'
urlpatterns = [
    # api
    path('admin/overview/count', views.admin.overview.count),
    path('admin/overview/sysInfo', views.admin.overview.sysInfo),
    path('admin/thing/list', views.admin.thing.list_api),
    path('admin/thing/detail', views.admin.thing.detail),
    path('admin/thing/create', views.admin.thing.create),
    path('admin/thing/update', views.admin.thing.update),
    path('admin/thing/delete', views.admin.thing.delete),
    path('admin/classification/list', views.admin.classification.list_api),
    path('admin/classification/create', views.admin.classification.create),
    path('admin/classification/update', views.admin.classification.update),
    path('admin/classification/delete', views.admin.classification.delete),
    path('admin/tag/list', views.admin.tag.list_api),
    path('admin/tag/create', views.admin.tag.create),
    path('admin/tag/update', views.admin.tag.update),
    path('admin/tag/delete', views.admin.tag.delete),
    path('admin/record/list', views.admin.record.list_api),
    path('admin/record/create', views.admin.record.create),
    path('admin/record/update', views.admin.record.update),
    path('admin/record/delete', views.admin.record.delete),
    path('admin/loginLog/list', views.admin.loginLog.list_api),
    path('admin/loginLog/create', views.admin.loginLog.create),
    path('admin/loginLog/update', views.admin.loginLog.update),
    path('admin/loginLog/delete', views.admin.loginLog.delete),
    path('admin/opLog/list', views.admin.opLog.list_api),
    path('admin/user/list', views.admin.user.list_api),
    path('admin/user/create', views.admin.user.create),
    path('admin/user/update', views.admin.user.update),
    path('admin/user/updatePwd', views.admin.user.updatePwd),
    path('admin/user/delete', views.admin.user.delete),
    path('admin/user/info', views.admin.user.info),
    path('admin/adminLogin', views.admin.user.admin_login),
]
