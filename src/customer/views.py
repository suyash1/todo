from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError

from rest_framework.views import APIView
from rest_framework import status   

from customer.models import Customer
from customer.serializers import CustomerSerializer

from utils.common import do_paginate, to_utc_time
from utils.dao import get_object, get_all_objects, filter_object

import json

class CustomerAPI(APIView):

    serializer_class = CustomerSerializer

    def get(self, request, customer_id=None):
        if customer_id:
            customer = get_object(model=Customer, pk=customer_id)
            customer_data = [
                {'id': customer.id, 'first_name': customer.first_name,
                'last_name': customer.last_name, 'email': customer.email,
                'dob': str(customer.dob)}
            ]
            return HttpResponse(
                json.dumps({
                        'data': customer_data, 
                    }),
                status=status.HTTP_200_OK, 
                content_type='application/json'
            )
        
        page = request.query_params.get('page', 1)
        results_per_page = request.query_params.get('results_per_page', 10)
        paginated_result = do_paginate(get_all_objects(model=Customer), page, results_per_page)
        customers = [CustomerSerializer(i).data for i in paginated_result[0].object_list]
        customer_data = [
            {'id': c.get('id'), 'first_name': c.get('first_name'),
            'last_name': c.get('last_name'), 'email': c.get('email'),
            'dob': str(c.get('dob'))} for c in customers
        ]
        return HttpResponse(
            json.dumps({
                'data': customer_data, 
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
        
        serializer = CustomerSerializer(data=request_body_dict)
        try:
            if serializer.is_valid():
                customer = serializer.save()
                customer_data = [
                    {'id': customer.id, 'first_name': customer.first_name,
                    'last_name': customer.last_name, 'email': customer.email,
                    'dob': str(customer.dob)}
                ]
                return HttpResponse(
                    json.dumps({'data': customer_data}),
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

