
from django.shortcuts import render_to_response
from blog.models import Blog
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
#from django.template import RequestContext
from django.template.context_processors import csrf
# Create your views here.
#login blog
@login_required
def index(request):
    blog_list = Blog.objects.all()
    username = request.session.get('username', '') #read user session
    user = username[0]
    return render(request, 'index.html', {'user': user, 'blogs': blog_list})

def login(request):
    return render(request, 'login.html')

# validate logon
def login_action(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    users_ = [username]
    user = auth.authenticate(username=username, password=password)
 #   if username != '' and password != '':
 #       response = HttpResponseRedirect('/index/')
 #       # response.set_cookie('username', username, 3600)
 #       request.session['username'] = username
 #      return response
 #   else:
 #       return render_to_response('login.html', context = csrf(request))
    if user is not None:
        auth.login(request, user)
        response = HttpResponseRedirect('/index/')
        request.session['username'] = users_
        return response
    else:
        #return render_to_response('login.html', {'error', 'username or password error!'}, context_instance=RequestContext(request))
        return render(request, 'login.html', context={'error': 'username or password error!'})

#logout
@login_required
def logout(request):
    response = HttpResponseRedirect('/login/')
    del request.session['username'] #clear user session
    return response