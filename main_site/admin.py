from django.contrib import admin
from main_site.models import TeamMember, SiteInfoMessage, Event, Supporter,Statistic, Contact


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
	list_display = ('name', 'last_name')

@admin.register(SiteInfoMessage)
class SiteInfoMessageAdmin(admin.ModelAdmin):
	list_display = ('title', 'text')

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
	list_display = ('title', 'count')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ['title']

@admin.register(Supporter)
class SupporterAdmin(admin.ModelAdmin):
	list_display = ['name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['phone']


