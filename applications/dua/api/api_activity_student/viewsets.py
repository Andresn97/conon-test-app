from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin

from .serializers import ActivityStudentSerializer
from applications.base.permissions import IsOwnerAndStudent


class ActivityStudentViewSet(LoggingMixin, viewsets.ModelViewSet):
    serializer_class = ActivityStudentSerializer
    permission_classes = ([IsOwnerAndStudent])
    logging_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    sensitive_fields = {'access', 'refresh'}

    # Return Data
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.get_activity_student_list()
        return self.get_serializer().Meta.model.objects.get_activity_student_by_id(pk)

    # Get Data List
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        activity_student_serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                'ok': True,
                'conon_data': activity_student_serializer.data
            },
            status=status.HTTP_200_OK
        )

    # Create Data
    def create(self, request, *args, **kwargs):
        activity_student_serializer = self.get_serializer(data=request.data)
        if activity_student_serializer.is_valid():
            activity_student_serializer.save()

            return Response(
                {
                    'ok': True,
                    'message': 'Actividad creada correctamente.'
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                'ok': False,
                'detail': activity_student_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # Update Data
    def update(self, request, pk=None, *args, **kwargs):
        activity_student = self.get_queryset(pk)
        if activity_student:
            # Send information to serializer referencing the instance
            activity_student_serializer = self.get_serializer(activity_student, data=request.data)
            if activity_student_serializer.is_valid():
                activity_student_serializer.save()

                return Response(
                    {
                        'ok': True,
                        'conon_data': activity_student_serializer.data,
                    },
                    status=status.HTTP_200_OK
                )

            return Response(
                {
                    'ok': False,
                    'detail': activity_student_serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                'ok': False,
                'detail': 'No existe esta Actividad.'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # Detail Data
    def retrieve(self, request, pk=None, *args, **kwargs):
        if self.get_queryset(pk):
            activity_student_serializer = self.get_serializer(self.get_queryset(pk))

            return Response(
                {
                    'ok': True,
                    'conon_data': activity_student_serializer.data,
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                'ok': False,
                'detail': 'No existe esta Actividad.'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # Delete Question
    def destroy(self, request, pk=None, *args, **kwargs):
        # Get instance
        activity_student = self.get_queryset(pk)
        if activity_student:
            activity_student.auth_state = 'I'
            activity_student.save()

            return Response(
                {
                    'ok': True,
                    'message': 'Actividad eliminada correctamente.'
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                'ok': False,
                'detail': 'No existe esta Actividad.'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
