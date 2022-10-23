from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.core.paginator import Paginator

import qrcode

# User
def homepage(request):
	return render(request=request, template_name='registration/home.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

#LOGIN REQUEST User credentials.
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homepage")

#SAMPLE
def add_sample(request):
	return render(request, 'samples/add_sample.html', {})


#FEED
def add_feed_sample(request):
	submitted = False
	form = AddFeedSampleForm(request.POST, use_required_attribute=False)
	
	if request.method == "POST":

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_feed_sample?submitted=True')
	else:
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'samples/add_feed_sample.html', {'form':form, 'submitted':submitted})

def list_feed_samples(request):
	feed_sample_list = Feed_sample.objects.all()

	# Set up Pagination
	p = Paginator(Feed_sample.objects.all(), 1000)
	page = request.GET.get('page')
	feed_samples = p.get_page(page)
	nums = "a" * feed_samples.paginator.num_pages
	return render(request, 'samples/feed_samples.html', 
		{'feed_sample_list': feed_sample_list,
		'feed_samples': feed_samples,
		'nums':nums}
		)

def view_feed_sample(request, sample_id):
	feed_sample = Feed_sample.objects.get(pk=sample_id)
	url = "20.87.17.241:8000" + str(request.path) # Check IP later on Azure
	img = qrcode.make(url) 
	type(img)
	qr_name = "static/QRcodes/feed_sample" +  str(feed_sample.sample_id) + ".png"
	img.save(qr_name)
	source_name = "QRcodes/feed_sample" +  str(feed_sample.sample_id) + ".png"
	return render(request, 'samples/view_feed_sample.html', {'feed_sample':feed_sample, 'source_name':source_name})

def update_feed_sample(request, sample_id):
	sample = Feed_sample.objects.get(pk=sample_id)
	form = UpdateFeedSampleForm(request.POST or None, instance=sample)

	if form.is_valid():
		form.save()
		return redirect('feed_samples')

	return render(request, 'samples/update_feed_sample.html', {'sample':sample, 'form':form})

	return render(request, 'samples/update_feed_sample.html', {'sample':sample})

def delete_feed_sample(request, sample_id):
	feed_sample = Feed_sample.objects.get(pk=sample_id)
	feed_sample.delete()
	return redirect('feed_samples')


#RESIDUE
def add_residue_sample(request):
	submitted = False
	form = AddResidueSampleForm(request.POST)
	
	if request.method == "POST":

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_residue_sample?submitted=True')
	else:
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'samples/add_residue_sample.html', {'form':form, 'submitted':submitted})

def list_residue_samples(request):
	residue_sample_list = Residue_sample.objects.all()

	# Set up Pagination
	p = Paginator(Residue_sample.objects.all(), 1000)
	page = request.GET.get('page')
	residue_samples = p.get_page(page)
	nums = "a" * residue_samples.paginator.num_pages
	return render(request, 'samples/residue_samples.html', 
		{'residue_sample_list': residue_sample_list,
		'residue_samples': residue_samples,
		'nums':nums}
		)

def view_residue_sample(request, sample_id):
	residue_sample = Residue_sample.objects.get(pk=sample_id)
	url = "20.87.17.241:8000" + str(request.path) # Check IP later on Azure
	img = qrcode.make(url) 
	type(img)
	qr_name = "static/QRcodes/residue_sample" +  str(residue_sample.sample_id) + ".png"
	img.save(qr_name)
	source_name = "QRcodes/residue_sample" +  str(residue_sample.sample_id) + ".png"
	return render(request, 'samples/view_residue_sample.html', {'residue_sample':residue_sample, 'source_name':source_name})

def update_residue_sample(request, sample_id):
	sample = Residue_sample.objects.get(pk=sample_id)
	form = UpdateResidueSampleForm(request.POST or None, instance=sample)

	if form.is_valid():
		form.save()
		return redirect('residue_samples')

	return render(request, 'samples/update_residue_sample.html', {'sample':sample, 'form':form})

	return render(request, 'samples/update_residue_sample.html', {'sample':sample})

def delete_residue_sample(request, sample_id):
	residue_sample = Residue_sample.objects.get(pk=sample_id)
	residue_sample.delete()
	return redirect('residue_samples')


#CLIENT
def add_client(request):
	submitted = False
	form = AddClientForm(request.POST)
	if request.method == "POST":

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_client?submitted=True')
	else:
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'registration/add_client.html', {'form':form, 'submitted':submitted})

def list_clients(request):
	client_list = Client.objects.all()

	# Set up Pagination
	p = Paginator(Client.objects.all(), 1000)
	page = request.GET.get('page')
	clients = p.get_page(page)
	nums = "a" * clients.paginator.num_pages
	return render(request, 'registration/clients.html', 
		{'client_list': client_list,
		'clients': clients,
		'nums':nums}
		)

def view_client(request, client_id):
	client = Client.objects.get(pk=client_id)
	return render(request, 'registration/view_client.html', {'client':client})

def update_client(request, client_id):
	client = Client.objects.get(pk=client_id)
	form = AddClientForm(request.POST or None, instance=client)

	if form.is_valid():
		form.save()
		return redirect('clients')

	return render(request, 'registration/update_client.html', {'client':client, 'form':form})

	return render(request, 'registration/update_client.html', {'client':client})

def delete_client(request, client_id):
	client = Client.objects.get(pk=client_id)
	client.delete()
	return redirect('clients')