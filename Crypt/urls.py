from django.contrib import admin
from django.urls import path, include
from .  import views


urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.logIn,name="login"),
    path('signup',views.signUp,name="signup"),
    path('mlogin',views.mlogIn,name="mlogin"),
    path('miner',views.miner,name="miner"),

    path('msignup',views.msignUp,name="msignup"),
    path('home',views.home,name="home"),
    path('sendcoin',views.sendCoin,name="sendcoin"),
    path('api_crypto',views.api_view,name="api_view"),
    path('logout',views.logout,name="logout"),
    path('api_chain',views.get_block_chain,name="blockChain"),
    path('api_exchange',views.get_current_exchange,name="currentExchange"),
    path('api_latest',views.get_last_block,name="lastBlock"),
    path('/hash_found',views.hash_found)
]

