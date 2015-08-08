from django.shortcuts import render
from django.http import HttpResponse ,Http404,HttpResponseRedirect
from .models import Question,Choice
from django.template import RequestContext,loader
from django.shortcuts import  render,get_object_or_404
from django.core.urlresolvers import reverse
import pprint
from django.contrib.auth import  (authenticate,login as auth_login ,logout as auth_logout)
from django.contrib.auth.models import  User
import traceback
import sys
from django.utils import timezone

# Create your views here.
def index(request):
	#if request.user.is_authenticated:
	#    latest_question_list=Question.objects.order_by('-pub_date')[:5]
	#    context={'latest_question_list':latest_question_list}
    #   return render(request,"polls/index.html",context)

	#else:
     #   return   HttpResponseRedirect(reverse("polls:loginView"))

	 if request.user.is_authenticated:
		 print(request.user.is_authenticated())
		 print("has permission")
		 #print(request.user.has_perm())
		 HttpResponse("success")
		 print("authentiated")
		 print(request.user)
		 print(request.user.is_active)
		 #return HttpResponse("success")
		 latest_question_list=Question.objects.order_by('-pub_date')[:5]
		 context={'latest_question_list':latest_question_list}
		 return render(request,"polls/index.html",context)
	 else:
		 HttpResponse("fail")
		 print("not authenticated!")
		 return HttpResponseRedirect(reverse("polls:loginView"))



       # return HttpResponseRedirect(reverse("polls:loginView"))
	#template =loader.get_template('polls/index.html')
	#context=RequestContext(request,{'latest_question_list':latest_question_list})
	#return HttpResponse(template.render(context))

def details(request,question_id):
    #response="You're looking at the question %s."
    #return HttpResponse(response % question_id)
	#try:
	#	question=Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exist !")
	#
	question=get_object_or_404(Question,pk=question_id)
	return render(request,"polls/details.html",{"question":question})

def results(request,question_id):
	response="You're looking at the result of question %s"
	question=get_object_or_404(Question,pk=question_id)
	return render(request,"polls/results.html",{"question":question})

def vote(request,question_id):
	#response="You're voting on question %s"
	#return HttpResponse(response % question_id)
	p=get_object_or_404(Question,pk=question_id)
	for key in request.POST:
		value=request.POST[key]
		print(key)
		print(value)
	try:
	    selected_choice=p.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		#Redisplay the question voting form
		return render(request,"polls/details.html",{"question":p,
													"error_message":"You didn't select a choice !"})
	else:
		selected_choice.votes+=1
		selected_choice.save()
		##always return an HttpResponseRediret after successfully dealing
		#with POST data this prevents data from being posted twice if a
		#user it the back button
		return HttpResponseRedirect(reverse("polls:resultsView",args=(p.id,)))
	
def login(request,message=""):
	print(request.GET.get("message"))
	return render(request,"polls/login.html",{"message":request.GET.get("message")})
    #return render(request,"polls/login.html",{})
	#print("dfa")
    #return render(request,"polls/login.html",{"message":"daf"})
	#return render(request,"polls/login.html",{"message":"adfadf"})



def logout(request):
	if request.user.is_authenticated:
		print(request.user)
		auth_logout(request)
		print("after")
		print(request.user)
		return HttpResponseRedirect("/polls/")

	#return render(request,"polls/login.html",{});


def auth(request):
	for key in request.POST:
		value=request.POST[key]
		print(key)
		print(value)
	user=authenticate(username=request.POST["name"],password=request.POST["password"])
	#if user exist
	if user is not None:
		if user.is_active:
			print("User is valid, active and authenticated")
			auth_login(request,user)
			return HttpResponseRedirect("/polls/")
		else:
			print("The password is valid, but the account has been disabled!")
	else:
		print("The username and password were incorrect.")
		return render(request,"polls/login.html",{"error_message":"abc"})
	#return render(request,"polls/login.html",{});
	return HttpResponse("auth page");

def homepage(request):
	return render(request,"polls/homepage.html",{})

def register(request):
    return render(request,"polls/register.html",{})

def registerError(request):
	print("eneter into register error view ")
	return render(request,"polls/registerError.html",{})

def reg(request):
	print("enter into reg page")
	#output post information
	for key in request.POST:
		    value=request.POST[key]
		    print(key)
		    print(value)
	#register user
	try:
		User.objects.create_user(request.POST["name"],"test@test.com",request.POST["password"])
	except:
		print(traceback.format_exc())
		return HttpResponseRedirect("/polls/registerError")
	else:
		return HttpResponseRedirect("/polls/login/?message=congratulations")

def createQuestion(request):
	if(request.user.has_perm("Can add question")):
		q=Question(question_text="test",pub_date=timezone.now())
		q.save()
		return HttpResponseRedirect("/admin")
	else:
		return HttpResponse("sorry you do not have the permission to crate question")



