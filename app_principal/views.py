
## Default
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from app_principal.models import Professor

def home(request):
	retorno = {}
	professor=Professor.objects.all()[:1]
	print professor
	retorno.update({'professor':professor})

	return render_to_response("home_professor.html",retorno,context_instance=RequestContext(request))