from django.db import models
from uuid import uuid4


# Create your models here.
class BkashPayment(models.Model):
    payment_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    transaction_id = models.CharField(
        max_length=255, null=True, blank=True
    )  # Add this field
    order_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, default="pending"
    )  # e.g., pending, completed, failed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bkash Payment - {self.order_id} - {self.status}"


class UserData(models.Model):
    """
    Model to store user registration and payment data for the school reunion.
    """

    # T-shirt sizes
    TSHIRT_SIZES = [
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    ]

    # SSC Batch years (dynamic, not hardcoded)
    SSC_BATCH_START = 1997
    SSC_BATCH_END = 2025
    SSC_BATCHES = [
        (str(year), str(year)) for year in range(SSC_BATCH_START, SSC_BATCH_END + 1)
    ]

    # Family Members (use integer choices for easier data handling)
    FAMILY_MEMBERS_CHOICES = [
        (1, "One"),
        (2, "Two"),
        (3, "Three"),
        (4, "Four"),
        (0, "None"),
    ]

    # Cultural events (add blank for "not participating")
    CULTURAL_EVENTS_CHOICES = [
        ("", "No Participation"),
        ("song", "গান"),
        ("dance", "নাচ"),
        ("comedy", "কৌতুক"),
        ("drama", "নাটক"),
        ("recitation", "আবৃত্তি"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20)
    ssc_batch = models.CharField(max_length=4, choices=SSC_BATCHES)
    t_shirt_size = models.CharField(max_length=4, choices=TSHIRT_SIZES)
    family_members = models.PositiveSmallIntegerField(
        choices=FAMILY_MEMBERS_CHOICES, default=0
    )
    cultural_event = models.CharField(
        max_length=20, choices=CULTURAL_EVENTS_CHOICES, blank=True, default=""
    )
    invoice = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User Data"
        verbose_name_plural = "User Data"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.ssc_batch})"

    @property
    def is_payment_completed(self):
        return self.status == "completed"
