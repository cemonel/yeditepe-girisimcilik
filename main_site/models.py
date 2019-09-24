from django.db import models


# Create your models here.

class TeamMember(models.Model):
	name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	instagram = models.CharField(max_length=50, blank=True)
	facebook = models.CharField (max_length=50, blank=True)
	linkedin = models.CharField (max_length= 50, blank=True)
	photo = models.ImageField(null=True, blank=True, upload_to="team_members/")

class SiteInfoMessage(models.Model):
	title = models.CharField(max_length=30)
	text = models.TextField(max_length=1000)

class Event(models.Model):
	title = models.CharField(max_length=50)
	application_form_link = models.CharField(max_length=300, blank=True)
	text = models.TextField(max_length=1000, blank=True)
	application_start_date = models.DateTimeField(editable=True)
	application_end_date = models.DateTimeField(editable=True)
	event_date = models.DateTimeField(editable=True)
	photo = models.ImageField(null=True, blank=True, upload_to="event_photo/")

class Supporter(models.Model):
	name = models.CharField(max_length=50)
	site_link = models.CharField(max_length=200)
	photo = models.ImageField(blank=True, upload_to="supporter_photo/")

class Statistic(models.Model):
	title = models.CharField(max_length=50)
	count = models.IntegerField()

class Contact(models.Model):
	adress = models.CharField(max_length=300)
	info = models.CharField(max_length=300)
	phone = models.CharField(max_length=100)
	mail = models.CharField(max_length=100)
	facebook = models.CharField(max_length=100)
	twitter = models.CharField(max_length=100)
	linkedin = models.CharField(max_length=100)
