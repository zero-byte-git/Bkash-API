from django.urls import path
from .views import (
    BkashCreatePaymentView,
    BkashExecutePaymentView,
    BkashQueryPaymentView,
)

urlpatterns = [
    path("create/", BkashCreatePaymentView.as_view(), name="bkash-create"),
    path("execute/", BkashExecutePaymentView.as_view(), name="bkash-execute"),
    path("query/", BkashQueryPaymentView.as_view(), name="bkash-query"),
]
