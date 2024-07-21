from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    # payment_status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    payment_history = SerializerMethodField()

    def get_payment_history(self, obj):
        return Payment.objects.filter(data_payment=obj).all()

    class Meta:
        model = User
        fields = '__all__'
