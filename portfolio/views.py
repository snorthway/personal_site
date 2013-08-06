# Is my email address on this commit?
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.paginator import Paginator
from datetime import datetime
from models import Photo

imagedir = "/static/img/"

def index(request):
	return render_to_response('home.html')

def engineering(request):
	return render_to_response('engineering.html')

def photography(request):
	data = {}
	data['portraits'] = _imgpath('alicia')
	data['nature'] = _imgpath('birds')
	data['etcetera'] = _imgpath('piano')
	return render_to_response('photography.html',data)

def album(request,subcategory):
	photos = Photo.objects.filter(subcategory=subcategory)
	files = []
	for p in photos:
		files.append(_imgpath(p.title))

	paginator = Paginator(files,1)
	page = request.GET.get('page')
	files = paginator.page(paginator.num_pages)

	data = {'photos':photos,'files':files}

	return render_to_response('album.html',data)

def sketchbook(request):
	return render_to_response('sketchbook.html')

### Ancilliary Functions ###
def _imgpath(title):
	p = Photo.objects.get(title=title)
	path = imagedir+p.filename
	return path