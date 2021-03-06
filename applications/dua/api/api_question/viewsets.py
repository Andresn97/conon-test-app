from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import QuestionSerializer
from applications.base.permissions import IsOwnerAndTeacher
from applications.base.paginations import CononPagination


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = ([IsOwnerAndTeacher])
    pagination_class = CononPagination

    # Return Question Data
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.get_question_list()
        return self.get_serializer().Meta.model.objects.get_question_by_id(pk)

    # Get Question List
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        question_serializer = self.get_serializer(queryset, many=True)

        return Response(
            {
                'ok': True,
                'conon_data': question_serializer.data
            },
            status=status.HTTP_200_OK
        )

    # Create Question
    def create(self, request, *args, **kwargs):
        is_many = True if isinstance(request.data, list) else False
        question_serializer = self.get_serializer(data=request.data, many=is_many)
        if question_serializer.is_valid():
            question_serializer.save()

            return Response(
                {
                    'ok': True,
                    'question':
                        question_serializer.data
                        if isinstance(question_serializer.data, list)
                        else question_serializer.data['id'],
                    'message':
                        'Preguntas agregadas correctamente'
                        if isinstance(question_serializer.data, list)
                        else 'Pregunta agregada correctamente'
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                'ok': False,
                'detail': question_serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # Update Question
    def update(self, request, pk=None, *args, **kwargs):
        question = self.get_queryset(pk)
        if question:
            # Send information to serializer referencing the instance
            question_serializer = self.get_serializer(question, data=request.data)
            if question_serializer.is_valid():
                question_serializer.save()

                return Response(
                    {
                        'ok': True,
                        'conon_data': question_serializer.data,
                    },
                    status=status.HTTP_200_OK
                )

            return Response(
                {
                    'ok': False,
                    'detail': question_serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                'ok': False,
                'detail': 'No existe esta Pregunta.'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # Detail Question
    def retrieve(self, request, pk=None, *args, **kwargs):
        if self.get_queryset(pk):
            question_serializer = self.get_serializer(self.get_queryset(pk))

            return Response(
                {
                    'ok': True,
                    'conon_data': question_serializer.data,
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                'ok': False,
                'detail': 'No existe esta Pregunta.'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # Delete Question
    def destroy(self, request, pk=None, *args, **kwargs):
        # Get instance
        question = self.get_queryset(pk)
        if question:
            question.active = False
            question.auth_state = 'I'
            question.save()

            return Response(
                {
                    'ok': True,
                    'message': 'Pregunta eliminada correctamente.'
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                'ok': False,
                'detail': 'No existe esta Pregunta.'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # Block Question
    @action(detail=True, methods=['DELETE'], url_path='block')
    def block_question(self, request, pk=None):
        question = get_object_or_404(self.serializer_class.Meta.model, id=pk)
        question.active = False
        question.save()
        return Response(
            {
                'ok': True,
                'message': 'Pregunta bloqueada correctamente.'
            },
            status=status.HTTP_200_OK
        )
