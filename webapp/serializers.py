from rest_framework import serializers
from rest_framework import customers
class customersSerializer(Serializers.ModelSerializer):
    class Meta:
        model=customers
        fields=('first_name','last_name')
    fields='__all__'