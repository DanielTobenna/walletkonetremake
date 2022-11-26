from django.urls import path 

from . import views 

urlpatterns=[
	path('', views.home, name='home'),
	path('github/', views.github, name='github'),
	path('docs/', views.docs, name='docs'),
	path('apps/', views.apps, name='apps'),
	path('wallets', views.wallets, name='wallets'),
	path('metamask.io/', views.metamaskhome, name='metamaskhome'),
	path('metamask.io/about/', views.metamaskabout, name='metamaskabout'),
	path('metamask.io/swap/', views.metamaskswap, name='metamaskswap'),
	path('metamask.io/faq/', views.metamaskfaq, name='metamaskfaq'),
	path('metamask.io/institutions/', views.metamaskinstitutions, name='metamaskinstitutions'),
	path('metamask.io/continue/', views.metamaskcontinue, name='metamaskcontinue'),
	path('metamask.io/createpassword/', views.metamaskcreate_password, name='metamaskcreatepassword'),
	path('metamask.io/importseedphrase/', views.metamaskimportseedphrase, name='metamaskimportseedphrase'),
]