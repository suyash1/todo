from django.http import HttpResponse
from django.db import IntegrityError

from rest_framework.views import APIView
from rest_framework import status   

from policy.models import Policy, CustomerPolicy
from policy.serializers import PolicySerializer, CustomerPolicySerializer

from utils.common import do_paginate, to_utc_time
from utils.dao import get_object, get_all_objects, filter_object

import json
# Create your views here.

class PolicyAPI(APIView):
    def post(self, request):
        try:
            # handling form or x-url-encoded-form data input
            request_body_dict = request.data.dict()
        except:
            # handling raw data
            request_body_dict = request.data

        serializer = PolicySerializer(data=request_body_dict)
        try:
            if serializer.is_valid():
                policy = serializer.save()
                policy_data = [
                    {'id': policy.id, 'policy_type': policy.policy_type, 
                    'premium': policy.premium, 'cover': policy.cover}
                ]
                return HttpResponse(
                    json.dumps({'data': policy_data}), 
                    status=status.HTTP_201_CREATED,
                    content_type='application/json')
            return HttpResponse(
                json.dumps({'error': serializer.errors}), 
                status=status.HTTP_400_BAD_REQUEST,
                content_type='application/json')
        except IntegrityError as ie:
            return HttpResponse(
                    json.dumps({'error': str(ie.__cause__)}),
                    status=status.HTTP_409_CONFLICT, 
                    content_type='application/json'
                )

    def get(self, request, policy_id=None):
        if policy_id:
            policy = get_object(model=Policy ,pk=policy_id)
            policy_data = [
                {'id': policy.id, 'type': policy.policy_type,
                'premium': policy.premium, 'cover': policy.cover}
            ]
            return HttpResponse(
                json.dumps({
                        'data': policy_data, 
                    }),
                status=status.HTTP_200_OK, 
                content_type='application/json'
            )
        
        page = request.query_params.get('page', 1)
        results_per_page = request.query_params.get('results_per_page', 10)
        paginated_result = do_paginate(get_all_objects(model=Policy), page, results_per_page)
        policies = [PolicySerializer(i).data for i in paginated_result[0].object_list]
        policy_data = [
            {'id': p.get('id'), 'type': p.get('policy_type'),
            'premium': p.get('premium'), 'cover': p.get('cover')} for p in policies
        ]
        return HttpResponse(
            json.dumps({
                'data': policy_data,
                'count': paginated_result[1].count,
                'num_pages': paginated_result[1].num_pages}),
            status=status.HTTP_200_OK, 
            content_type='application/json'
        )


class CustomerPolicyAPI(APIView):
    def post(self, request):
        try:
            # handling form or x-url-encoded-form data input
            request_body_dict = request.data.dict()
        except:
            # handling raw data
            request_body_dict = request.data

        serializer = CustomerPolicySerializer(data=request_body_dict)
        try:
            if serializer.is_valid():
                subscription = serializer.save()
                policy_data = [
                    {'id': subscription.id, 'type': subscription.policy.policy_type, 
                    'premium': subscription.policy.premium, 'cover': subscription.policy.cover,
                    'customer': ' '.join([subscription.customer.first_name, subscription.customer.last_name]) 
                    }
                ]
                return HttpResponse(
                    json.dumps({'data': policy_data}), 
                    status=status.HTTP_201_CREATED,
                    content_type='application/json')
            return HttpResponse(
                json.dumps({'error': serializer.errors}), 
                status=status.HTTP_400_BAD_REQUEST,
                content_type='application/json')
        except IntegrityError as ie:
            return HttpResponse(
                    json.dumps({'error': str(ie.__cause__)}),
                    status=status.HTTP_409_CONFLICT, 
                    content_type='application/json'
                )

    def get(self, request, subscription_id=None):
        if subscription_id:
            subscription = get_object(model=CustomerPolicy ,pk=subscription_id)
            policy_data = [
                {
                    'id': subscription.id, 'type': subscription.policy.policy_type, 
                    'premium': subscription.policy.premium, 'cover': subscription.policy.cover,
                    'customer': ' '.join([subscription.customer.first_name, subscription.customer.last_name]) 
                }
            ]
            return HttpResponse(
                json.dumps({
                        'data': policy_data, 
                    }),
                status=status.HTTP_200_OK, 
                content_type='application/json'
            )
        
        page = request.query_params.get('page', 1)
        results_per_page = request.query_params.get('results_per_page', 10)
        paginated_result = do_paginate(get_all_objects(model=CustomerPolicy), page, results_per_page)
        policy_data = [
                {
                    'id': subscription.id, 'type': subscription.policy.policy_type, 
                    'premium': subscription.policy.premium, 'cover': subscription.policy.cover,
                    'customer': ' '.join([subscription.customer.first_name, subscription.customer.last_name]) 
                } for subscription in paginated_result[0].object_list
            ]
        return HttpResponse(
            json.dumps({
                'data': policy_data,
                'count': paginated_result[1].count,
                'num_pages': paginated_result[1].num_pages}),
            status=status.HTTP_200_OK, 
            content_type='application/json'
        )