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

def plants(request, section='index'):
    plants = [
        {
            'name': 'Sweet Woodruff',
            'description': {
                'Grow': 'Perennial, 8"-12" in height, blooms spring to summer',
                'Sun': 'Shade',
                'Soil': 'Well-drained, slightly acidic',
                'Water': 'More watering will promote spread, drought tolerant',
                'Harvesting': 'Harvest leaves right after bloom',
                'Use': 'Dry and can lend fragrance to linens, sachets and potpourris',
            },
            'image': 'IMG_2631.jpg',
        }
    ]*3
    
    response = {
        'page': 'plants',
        'section': section,
        'plants': plants,
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
