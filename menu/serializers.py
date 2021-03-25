from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from menu.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    collapsed = serializers.BooleanField(default=True)

    class Meta:
        model = Menu
        fields = ('id', 'children', 'collapsed','link','info')
