from django.shortcuts import render
from main_site.models import SiteInfoMessage, Supporter, Contact, TeamMember
from main_site.models import Event

def index(request):
	info_messages = SiteInfoMessage.objects.order_by('id')[:5]
	supporters = Supporter.objects.order_by('id')
	contact =  Contact.objects.first()
	team_members =  TeamMember.objects.order_by('id')
	return render(request, 'index.html', context= {'info_messages': info_messages,
													'supporters': supporters,
													'contact': contact,
												   	'team_members': team_members})

def team(request):

	return render(request, 'team.html')

def info(request):

	return render(request, 'info.html')

def event(request):
	events = Event.objects.order_by('event_date')
	return render(request, 'event.html', context= {'events': events})

def supporter(request):

	return render(request, 'supporter.html')