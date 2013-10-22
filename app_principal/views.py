
## Default
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from app_principal.models import Professor

def home(request):
	return render_to_response("home_professor.html",
								{'professor':Professor.objects.get(id=1)},
								context_instance=RequestContext(request)
							  )