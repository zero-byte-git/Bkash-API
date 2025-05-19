from django.contrib import admin
from payment.models import BkashPayment, UserData


@admin.register(BkashPayment)
class BkashPaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_id", "transaction_id", "order_id", "amount", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("order_id", "transaction_id", "payment_id")


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "ssc_batch", "t_shirt_size", "family_members", "amount", "invoice", "created_at")
    list_filter = ("ssc_batch", "t_shirt_size", "family_members", "created_at")
    search_fields = ("name", "email", "phone", "invoice")
