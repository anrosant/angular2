# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from pruebaApp.models import Platillo
from pruebaApp.serializers import PlatilloSerializer

class JSONResponse(HttpResponse):

	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)
	
@csrf_exempt
def platillo_list(request):
	if request.method == 'GET':
		platillos = Platillo.objects.all()
		serializer = PlatilloSerializer(platillos, many=True)
		return JSONResponse(serializer.data)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PlatilloSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def platillo_detail(request, idP):
 
	try:
		platillo = Platillo.objects.get(idP=idP)
	except Platillo.DoesNotExist:
		return HttpResponse(status=404)
	if request.method == 'GET':
		serializer = PlatilloSerializer(platillo)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = PlatilloSerializer(platillo, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		platillo.delete()
		return HttpResponse(status=204)
