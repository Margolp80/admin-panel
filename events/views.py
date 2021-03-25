from rest_framework import generics, mixins, status

from events.models import Event
from events.serializers import EventsSerializer


class EventView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    serializer_class = EventsSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None, format=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)
