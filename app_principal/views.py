
## Default
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from app_principal.models import Professor,MaterialApoio,Aviso

def home(request):
	retorno = {}
	
	try:
		#explica o pq do try
		professor=Professor.objects.all()[0]
		retorno.update({'professor':professor})
	except Exception, e:
		pass
	
	
	materiais=MaterialApoio.objects.all()[:5]
	retorno.update({'materiais':materiais})

	avisos=Aviso.objects.all()[:5]
	retorno.update({'avisos':avisos})

	return render_to_response("home_professor.html",retorno,context_instance=RequestContext(request))


