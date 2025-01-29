from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from .models import task
from .serializers import taskserializer
from .filters import TaskFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

#task to list and create view
class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = task.objects.all()
    serializer_class = taskserializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = TaskFilter
    search_fields = ['Title', 'Description']  #search: title and description

#update and delete for view
class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = task.objects.all()
    serializer_class = taskserializer

    # مشاهده Task بر اساس ID (درواقع از get_object استفاده می‌کند)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # Update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    #Delete
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
