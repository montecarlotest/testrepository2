from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$',views.index,name='indexView'),
	url(r'^login/',views.login,{'message':""},name="loginView"),
	url(r'^logout/$',views.logout,name="logoutView"),
	url(r'^create/$',views.createQuestion,name="createView"),
	url(r'^register/$',views.register,name="registerView"),
	url(r'^registerError/$',views.registerError,name="registerErrorView"),
	url(r'^reg/$',views.reg,name="regView"),
	url(r'^auth/$',views.auth,name="authView"),
	url(r'^(?P<question_id>[0-9]+)/$',views.details,name="detailsView"),
	url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name="resultsView"),
	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name="voteView"),

]