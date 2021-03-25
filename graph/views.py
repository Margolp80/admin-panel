# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
# from graph import models
#
#
# @api_view(['GET', 'POST'])
# def graph_list(request):
#     if request.method == 'GET':
#         return JsonResponse(models.okyanus, safe=False)
#     elif request.method == 'POST':
#         print(request.headers['Path'])
#         return JsonResponse({'message': 'shit'}, safe=False)
