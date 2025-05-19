from django.urls import path
from payment.views import (
    BkashCreatePaymentView,
    BkashExecutePaymentView,
    BkashQueryPaymentView,
    UserDataCreateView,
    UserDataListView,
)

urlpatterns = [
    path("create/", BkashCreatePaymentView.as_view(), name="bkash-create"),
    path("execute/", BkashExecutePaymentView.as_view(), name="bkash-execute"),
    path("query/", BkashQueryPaymentView.as_view(), name="bkash-query"),
    path("user-data/create/", UserDataCreateView.as_view(), name="user-data-create"),
    path("user-data/", UserDataListView.as_view(), name="user-data-list"),
]
