from ecologik.shortcuts import template_response, json_response, html_response, redirect

def index(request):
	response = {
		'page': 'index'
	}
	return template_response('index.html', response, request)

def services(request):
	response = {
		'page': 'services'
	}
	return template_response('services.html', response, request)

def plants(request):
	response = {
		'page': 'plants'
	}
	return template_response('plants.html', response, request)

def about(request):
	response = {
		'page': 'about'
	}
	return template_response('about.html', response, request)

def contact(request):
	response = {
		'page': 'contact'
	}
	return template_response('contact.html', response, request)
