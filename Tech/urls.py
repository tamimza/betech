from django.urls import path
from .views import index,companies,comp1,emp,fre,fre1,fre2,fre3,job,jobs,jobs1,jobs2,jobs3,about,car,cars,com,con,cons,cover,cust,custs,erro,faq,hire,invo,login,logins,mein,price,prive,reco,recos,ser,sign,signs,stat,term

urlpatterns = [

    path('companies/', companies, name='companies'),
    path('', index, name='index'),
    path('comp1/', comp1, name='comp1'),
    path('emp/', emp, name='emp'),
    path('fre/', fre, name='fre'),
    path('fre1/', fre1, name='fre1'),
    path('fre2/', fre2, name='fre2'),
    path('fre3/', fre3, name='fre3'),
    path('job/', job, name='job'),
    path('jobs/', jobs, name='jobs'),
    path('jobs1/', jobs1, name='jobs1'),
    path('jobs2/', jobs2, name='jobs2'),
    path('jobs3/', jobs3, name='jobs3'),

    path('about/', about, name='about'),
    path('car/', car, name='car'),
    path('cars/', cars, name='cars'),
    path('com/', com, name='com'),
    path('con/', con, name='con'),
    path('cons/', cons, name='cons'),
    path('cover/', cover, name='cover'),
    path('cust/', cust, name='cust'),
    path('custs/', custs, name='custs'),
    path('erro/', erro, name='erro'),
    path('faq/', faq, name='faq'),
    path('hire/', hire, name='hire'),
    path('invo/', invo, name='invo'),
    path('login/', login, name='login'),
    path('logins/', logins, name='logins'),
    path('mein/', mein, name='mein'),
    path('price/', price, name='price'),
    path('prive/', prive, name='prive'),
    path('reco/', reco, name='reco'),
    path('recos/', recos, name='recos'),
    path('services/', ser, name='ser'),
    path('sign/', sign, name='sign'),
    path('signs/', signs, name='signs'),
    path('stat/', stat, name='stat'),
    path('term/', term, name='term'),


]