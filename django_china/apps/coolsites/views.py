# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from coolsites.models import SiteCategory, CoolSites
from coolsites.forms import SiteCategoryForm, CoolSitesForm

def index(request):
    """酷站首页面"""
    sc = SiteCategory.objects.all() ## site分类

    return render_to_response('coolsites/index.html',
                              {'sc': sc},
                              context_instance=RequestContext(request))

@login_required
def create(request):
    """登录用户可自行添加相关网站"""

    if request.method == 'POST':
        form = CoolSitesForm(request.POST)
        if form.is_valid():
            model = form.save(request.user)
            return HttpResponseRedirect(reverse('sites_index'))
    else:
        form = CoolSitesForm()

    return render_to_response('coolsites/create.html',
                              {'form': form},
                              context_instance=RequestContext(request))
