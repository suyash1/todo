from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError

from rest_framework.views import APIView
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer

from utils.common import do_paginate, to_utc_time
from utils.dao import get_object, get_all_objects, filter_object, delete_object

import json


class TaskAPI(APIView):
    serializer_class = TaskSerializer

    def get(self, request, task_id=None):
        if task_id:
            task = get_object(model=Task, pk=task_id)
            task_data = [
                {'id': task.id, 'first_name': task.title,
                 'last_name': task.description, 'email': str(task.due_date),
                 }
            ]
            return HttpResponse(
                json.dumps({
                    'data': task_data,
                }),
                status=status.HTTP_200_OK,
                content_type='application/json'
            )

        page = request.query_params.get('page', 1)
        results_per_page = request.query_params.get('results_per_page', 10)
        paginated_result = do_paginate(get_all_objects(model=Task), page, results_per_page)
        tasks = [TaskSerializer(i).data for i in paginated_result[0].object_list]

        return HttpResponse(
            json.dumps({
                'data': tasks,
                'count': paginated_result[1].count,
                'num_pages': paginated_result[1].num_pages}),
            status=status.HTTP_200_OK,
            content_type='application/json'
        )

    def post(self, request):
        try:
            # handling form or x-url-encoded-form data input
            request_body_dict = request.data.dict()
        except:
            # handling ray data
            request_body_dict = request.data

        serializer = TaskSerializer(data=request_body_dict)
        try:
            if serializer.is_valid():
                task_data = serializer.save()
                response_data = [
                    {'id': task_data.id, 'title': task_data.title,
                     'description': task_data.description, 'due_date': str(task_data.due_date),
                     }
                ]
                return HttpResponse(
                    json.dumps({'data': response_data}),
                    status=status.HTTP_201_CREATED,
                    content_type='application/json'
                )
            return HttpResponse(
                json.dumps({'error': serializer.errors}),
                status=status.HTTP_400_BAD_REQUEST,
                content_type='application/json'
            )
        except IntegrityError as ie:
            return HttpResponse(
                json.dumps({'error': str(ie.__cause__)}),
                status=status.HTTP_409_CONFLICT,
                content_type='application/json'
            )

    def put(self, request, task_id):
        task = get_object(model=Task, pk=task_id)
        try:
            # handling form or x-url-encoded-form data input
            request_body_dict = request.data.dict()
        except:
            # handling ray data
            request_body_dict = request.data
        serializer = TaskSerializer(task, request_body_dict)
        if serializer.is_valid():
            updated_task = serializer.save()
            task_data = [
                {'id': updated_task.id, 'first_name': updated_task.title,
                 'last_name': updated_task.description, 'email': str(updated_task.due_date),
                 }
            ]
            return HttpResponse(json.dumps(task_data), status=status.HTTP_201_CREATED, content_type='application/json')
        return HttpResponse(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
            content_type='application/json')

    def delete(self, request, task_id):
        task = filter_object(model=Task, key='id', value=task_id)
        if task:
            task[0].delete()
            return HttpResponse(
                json.dumps('Task deleted'),
                status=status.HTTP_200_OK,
                content_type='application/json')
        return HttpResponse(
            json.dumps('Task not found'),
            status=status.HTTP_404_NOT_FOUND,
            content_type='application/json')

