from django.shortcuts import (render, render_to_response, 
                                RequestContext, redirect,
                                )
from django.contrib.auth.models import User
# Create your views here.
from .forms import (SignUpForm, ContactUs, UserRegistration,
                    )

def home(request):

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response('signup.html',
                                locals(),
                                context_instance=RequestContext(request)
                            )

def aboutus(request):
    return render_to_response('aboutus.html',
                                locals(),
                                context_instance=RequestContext(request)
                            )

def contactus(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
    return render_to_response('contactus.html',
                                locals(),
                                context_instance=RequestContext(request)
                            )

def getstarted(request):
    if request.method == "GET":
        form = UserRegistration()
    elif request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            new_user=User.objects.create_user(form.cleaned_data['username'],
                                      form.cleaned_data['email'],
                                      form.cleaned_data['password1'])
            return redirect("/upload-event")       
    return render(request, 'getstarted.html',
                    locals())

def uploadevent(request):
    return render(request, 'uploadevent.html',
                    locals())
    
    # render assumes that you're using a request context...


# ('getstarted.html',
#   locals(),
#   context_instance=RequestContext(request)
#   )



