from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer


class MenuList(generics.ListAPIView):
    queryset = Menu.objects.filter(parent=None)
    serializer_class = MenuSerializer
