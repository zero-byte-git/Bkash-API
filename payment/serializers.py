from rest_framework import serializers
from payment.models import UserData


class PaymentCreateSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    invoice = serializers.CharField()


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "ssc_batch": {
                "help_text": "SSC passing year. Choices: "
                + ", ".join([f"{k}" for k, _ in UserData.SSC_BATCHES])
            },
            "t_shirt_size": {
                "help_text": "T-shirt size. Choices: "
                + ", ".join([f"{k}" for k, _ in UserData.TSHIRT_SIZES])
            },
            "family_members": {
                "help_text": "Number of family members attending. Choices: "
                + ", ".join([f"{k}" for k, _ in UserData.FAMILY_MEMBERS_CHOICES])
            },
            "cultural_event": {
                "help_text": "Participation in cultural event. Choices: "
                + ", ".join(
                    [f"{k} ({v})" for k, v in UserData.CULTURAL_EVENTS_CHOICES if k]
                )
            },
        }
