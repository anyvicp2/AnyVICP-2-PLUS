from django.http import *
from django.template import loader
from AnyVICP2.models import Website
import json
import datetime

def index(request):
    """
    Index page
    """
    # Render the template with the websites
    template = loader.get_template('index.html')

    # Get config
    context = json.load(open('./AnyVICP2/config.json', "r"))
    return HttpResponse(template.render(context, request))

def join(request):
    """
    Join page
    """
    # Render the template with the websites
    template = loader.get_template('join.html')

    # Get config
    context = json.load(open('./AnyVICP2/config.json', "r"))
    return HttpResponse(template.render(context, request))

def joinapi(request:HttpRequest):
    """
    Join api

    No template
    """
    """
    name: 名称
    domain: 域名
    author: 创建者
    createDate: 创建日期
    icpNumber: ICP号码
    status: 状态
    """
    name = request.GET.get('name')
    domain = request.GET.get('domain')
    author = request.GET.get('author')
    createDate = datetime.datetime.now()
    icpNumber = request.GET.get('icpNumber')
    status = True
    
    # Create a new website
    website = Website(name=name, domain=domain, author=author, createdate=createDate, icpNumber=icpNumber, status=status)
    website.save()

    # Redirect to result shower
    return HttpResponseRedirect('/result/?domain=' + domain)

def result(request:HttpRequest):
    """
    Result page
    """
    # Render the template with the websites
    template = loader.get_template('result.html')

    # Get config
    context = json.load(open('./AnyVICP2/config.json', "r"))

    # Find domain in database
    domain = request.GET.get('domain')
    website = Website.objects.filter(domain=domain).first()

    notfound = False
    if not website:
        notfound = True
        return HttpResponse(template.render(context, request))

    context['notfound'] = notfound
    name = website.name
    domain = website.domain
    author = website.author
    createDate = website.createdate.__str__()
    icpNumber = website.icpNumber
    status = website.status

    context['site_name'] = name
    context['site_domain'] = domain
    context['site_author'] = author
    context['site_createdate'] = createDate
    context['site_icpnumber'] = icpNumber
    context['site_status'] = status

    return HttpResponse(template.render(context, request))