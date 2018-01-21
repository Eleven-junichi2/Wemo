from django.urls import path

from . import views

app_name = "wemo_app"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("memo_list/", views.MemoListView.as_view(), name="memo_list"),
    path("memo_list/<int:pk>/", views.MemoView.as_view(),
         name="memo_view"),
    path("memo_create/", views.MemoCreateFormView.as_view(),
         name="memo_create"),
    path("memo_create/add/", views.MemoCreateView.as_view(),
         name="memo_add"),
    path("credit", views.CreditView.as_view(), name="credit"),
    path("memo_list/<int:pk>/delete", views.MemoDeleteView.as_view(),
         name="memo_delete"),
    path("memo_list/<int:pk>/update", views.MemoUpdateView.as_view(),
         name="memo_update"),
    path("help/", views.HelpView.as_view(), name="help")
]
