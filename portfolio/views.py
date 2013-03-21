# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def index(request):
	return render_to_response('home.html')

def engineering(request):
	return render_to_response('engineering.html')

def photography(request):
	return render_to_response('photography.html')

def album(request):
	return render_to_response('album.html')

def sketchbook(request):
	return render_to_response('sketchbook.html')