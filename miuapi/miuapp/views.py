from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from miuapp.models import Notice
from miuapp.serializers import NoticeSerializer

@csrf_exempt
def api_list(request):
    
    if request.method == 'GET':
        apivar = Notice.objects.all()
        serializer = NoticeSerializer(apivar, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoticeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def api_detail(request, pk):
    try:
        dvar = Notice.objects.get(pk=pk)
    except Notice.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NoticeSerializer(dvar)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoticeSerializer(dvar, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dvar.delete()
        return HttpResponse(status=204)

