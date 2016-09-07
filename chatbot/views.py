#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

VERIFY_TOKEN = '7thseptember2016'

class MyChatBotView(generic.View):
	def get(self, request, *args, **kwargs):
		if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Oops! Invalid Token')

	@csrf_exempt
	def dispath(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	@csrf_exempt
	def post(self, request, *args, **kwargs):
		incoming_message = json.loads(self.request.body.decode('utf-8'))
		print incoming_message

def index(request):
	return HttpResponse('Hello world')