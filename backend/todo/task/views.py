from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import DirectoryModel, TaskModel
from .serializers import DirectorySerializer, TaskSerializer, TaskCreateSerializer


# Create your views here.
def bool_validator(value):
    if value in ["true", "1", True]:
        return True
    else:
        return False


class DirectoryCreateAPiView(CreateAPIView):
    serializer_class = DirectorySerializer
    queryset = DirectoryModel.objects.all()

    @swagger_auto_schema(tags=['Directory'])
    def post(self, request, *args, **kwargs):
        """
        Create a new directory.

        Request Body:
        - title: The title of the directory (required)

        Returns:
        - 200 OK: Directory created successfully.
        - 400 BAD REQUEST: Failed to create the directory.
        - 406 NOT ACCEPTABLE: Invalid or missing title.

        Notes:
        - User authentication is not applied in this implementation.

        """
        title = request.data.get('title', None)
        if not title:
            return Response({"details": "Title is required"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if DirectoryModel.objects.filter(title=title).exists():
            return Response({"details": "Directory already exists"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        directory_serializer = DirectorySerializer(data=request.data)
        if directory_serializer.is_valid(raise_exception=True):
            directory_serializer.save()
            data = directory_serializer.data
            data["details"] = "Directory created"
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Failed to create directory"}, status=status.HTTP_400_BAD_REQUEST)


class DirectoryUpdateAPiView(UpdateAPIView):
    serializer_class = DirectorySerializer
    queryset = DirectoryModel.objects.all()

    @swagger_auto_schema(tags=['Directory'])
    def put(self, request, *args, **kwargs):
        """
        Update an existing directory.

        Request Body:
        - title: The updated title of the directory (required)

        Returns:
        - 200 OK: Directory updated successfully.
        - 400 BAD REQUEST: Failed to update the directory.
        - 404 NOT FOUND: Directory not found.
        - 406 NOT ACCEPTABLE: Invalid or missing title.

        Notes:
        - User authentication is not applied in this implementation.

        """
        title = request.data.get('title', None)
        if not title:
            return Response({"details": "Title is required"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if DirectoryModel.objects.filter(title=title).count() > 1:
            return Response({"details": "Directory already exists"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        directory_obj = DirectoryModel.objects.filter(title=title).first()
        if not directory_obj:
            return Response({"details": "Directory not found"}, status=status.HTTP_404_NOT_FOUND)
        directory_serializer = DirectorySerializer(data=request.data, instance=directory_obj)
        if directory_serializer.is_valid(raise_exception=True):
            directory_serializer.save()
            data = directory_serializer.data
            data["details"] = "Directory updated"
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Failed to create directory"}, status=status.HTTP_400_BAD_REQUEST)


class DirectoryListAPIView(ListAPIView):
    """
    Retrieve a list of all directories.

    Returns:
    - 200 OK: List of directories retrieved successfully.

    Notes:
    - User authentication is not applied in this implementation.

    """

    serializer_class = DirectorySerializer
    queryset = DirectoryModel.objects.all()

    @swagger_auto_schema(tags=['Directory'])
    def get(self, request, *args, **kwargs):
        serializer = DirectorySerializer(self.queryset.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class DirectoryDestroyAPIView(DestroyAPIView):
    """
    Delete a directory.

    Request Parameters:
    - title (str): Title of the directory to be deleted.

    Returns:
    - 200 OK: Directory deleted successfully.
    - 400 BAD REQUEST: Invalid directory or missing title parameter.

    Notes:
    - User authentication is not applied in this implementation.

    """
    queryset = DirectoryModel.objects.all()

    @swagger_auto_schema(tags=['Directory'])
    def delete(self, request, *args, **kwargs):
        title = request.query_params.get('title', None)
        if not title:
            return Response({"details": "Invalid directory"}, status=status.HTTP_400_BAD_REQUEST)
        obj = self.queryset.filter(title=title).first()
        if obj:
            obj.delete()
            return Response({"details": "Directory deleted"}, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Invalid directory"}, status=status.HTTP_400_BAD_REQUEST)


class TaskCreateAPIView(CreateAPIView):
    """
    Create a new task.

    Request Parameters:
    - title (str): Title of the task (required).
    - description (str): Description of the task (optional).
    - directory (str): Title of the task's directory (optional).
    - date (str): Task complete date (optional).
    - is_important (bool): Task is important or not (optional).
    - is_completed (bool): Task is completed or not (optional).

    Returns:
    - 201 CREATED: Task created successfully.
    - 400 BAD REQUEST: Failed to create task or missing required parameters.
    - 406 NOT ACCEPTABLE: Title already exists.

    Notes:
    - User authentication is not applied in this implementation.

    """
    serializer_class = TaskCreateSerializer
    queryset = TaskModel.objects.all()

    @swagger_auto_schema(tags=['Tasks'])
    def post(self, request, *args, **kwargs):
        title = request.data.get('title', None)
        directory = request.data.get('directory', None)
        request.data.pop('directory')
        if not title:
            return Response({"details": "Title is required"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if TaskModel.objects.filter(title=title).exists():
            return Response({"details": "Title already exists"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        directory_obj = DirectoryModel.objects.filter(title=directory).first()
        if not directory_obj:
            directory_obj, created = DirectoryModel.objects.get_or_create(title="Main")
            request.data["directory"] = directory_obj.id
        request.data["directory"] = directory_obj.id

        task_serializer = self.serializer_class(data=request.data)
        if task_serializer.is_valid(raise_exception=True):
            task_obj = task_serializer.save()
            data = TaskSerializer(task_obj).data
            data["details"] = "Task created"
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response({"details": "Failed to create task"}, status=status.HTTP_400_BAD_REQUEST)


class TaskListApiView(ListAPIView):
    """
    Retrieve a list of tasks.

    Returns:
    - 200 OK: List of tasks retrieved successfully.

    Notes:
    - User authentication is not applied in this implementation.
    """
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()

    @swagger_auto_schema(tags=['Tasks'])
    def get(self, request, *args, **kwargs):
        serializer = TaskSerializer(self.queryset.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class TaskUpdateAPIView(UpdateAPIView):
    serializer_class = TaskCreateSerializer
    queryset = TaskModel.objects.all()

    @swagger_auto_schema(tags=['Tasks'])
    def put(self, request, *args, **kwargs):
        """
    Update exiting task.

    Request Parameters:
    - title (str): Title of the task (required).
    - description (str): Description of the task (optional).
    - directory (str): Title of the task's directory (optional).
    - date (str): Task complete date (optional).
    - is_important (bool): Task is important or not (optional).
    - is_completed (bool): Task is completed or not (optional).

    URL Parameters:
    - pk (int): Primary key of the task to update (required).

    Returns:
    - 201 CREATED: Task created successfully.
    - 400 BAD REQUEST: Failed to create task or missing required parameters.
    - 406 NOT ACCEPTABLE: Title already exists.

    Notes:
    - User authentication is not applied in this implementation.

    """
        pk = kwargs.get('pk', None)
        title = request.data.get('title', None)
        directory = request.data.get('directory', None)
        request.data.pop('directory')

        if not pk:
            return Response({"detail": "Invalid task"}, status=status.HTTP_400_BAD_REQUEST)
        if TaskModel.objects.filter(~Q(pk=pk), title=title).count() > 0:
            # may user not changed the task title, so count will get 1
            return Response({"details": "Title already exists"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        directory_obj = DirectoryModel.objects.filter(title=directory).first()
        if not directory_obj:
            directory_obj, created = DirectoryModel.objects.get_or_create(title="Main")
            request.data["directory"] = directory_obj.id
        request.data["directory"] = directory_obj.id

        task_obj = TaskModel.objects.filter(pk=pk).first()
        if not task_obj:
            return Response({"detail": "Invalid task"}, status=status.HTTP_400_BAD_REQUEST)
        task_serializer = self.serializer_class(instance=task_obj, data=request.data)
        if task_serializer.is_valid(raise_exception=True):
            task_obj = task_serializer.save()
            data = TaskSerializer(task_obj).data
            data["details"] = "Task updated"
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"details": "Failed to create task"}, status=status.HTTP_400_BAD_REQUEST)


class ChangeTaskStatusAPIView(APIView):
    """
    Change the status of a task.

    Query Parameters:
    - status (str): Status to change ('completed' or 'important') (required).
    - is_completed (bool): Updated value for the 'is_completed' field (optional, default=False).
    - is_important (bool): Updated value for the 'is_important' field (optional, default=False).

    URL Parameters:
    - pk (int): Primary key of the task to update (required).

    Returns:
    - 200 OK: Task status updated successfully.
    - 400 BAD REQUEST: Invalid data or task doesn't exist.

    Notes:
    - User authentication is not applied in this implementation.

    """
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()

    @swagger_auto_schema(tags=['Tasks'])
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        status_data = request.query_params.get('status', None)
        is_completed = bool_validator(
            request.query_params.get('is_completed', False)
        )
        is_important = bool_validator(
            request.query_params.get('is_important', False)
        )
        if not pk:
            return Response({"detail": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
        task_obj = self.queryset.filter(pk=pk).first()
        if not task_obj:
            return Response({"detail": "Task doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
        if status_data == 'completed':
            task_obj.is_completed = is_completed
        elif status_data == 'important':
            task_obj.is_important = is_important
        task_obj.save()
        task_serializer = TaskSerializer(task_obj)
        data = task_serializer.data
        data["details"] = "Task updated"
        return Response(data=data, status=status.HTTP_200_OK)


class TaskDeleteAPIView(DestroyAPIView):
    """
        Delete a task.

        URL Parameters:
        - pk (int): Primary key of the task to update (required).

        Returns:
        - 200 OK: Task deleted successfully.
        - 400 BAD REQUEST: Invalid data or task doesn't exist.

        Notes:
        - User authentication is not applied in this implementation.

        """
    queryset = TaskModel.objects.all()

    @swagger_auto_schema(tags=['Tasks'])
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"detail": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
        task_obj = self.queryset.filter(pk=pk).first()
        if not task_obj:
            return Response({"detail": "Task doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
        task_obj.delete()
        return Response({"details": "Task deleted"}, status=status.HTTP_200_OK)
