from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'job/index.html',{})
def companies(request):
    return render(request, 'job/companies.html', {})
def comp1(request):
    return render(request,'job/company-profile.html',{})
def emp(request):
    return render(request,'job/employee-profile.html',{})
def fre(request):
    return render(request,'job/freelancers-grid.html',{})
def fre1(request):
    return render(request,'job/freelancers-grid-side-filter.html',{})
def fre2(request):
    return render(request,'job/freelancers-list.html',{})
def fre3(request):
    return render(request,'job/freelancers-list-side-filter.html',{})
def job(request):
    return render(request,'job/job-description.html',{})
def jobs(request):
    return render(request,'job/jobs-grid.html',{})
def jobs1(request):
    return render(request,'job/jobs-grid-side-filter.html',{})
def jobs2(request):
    return render(request,'job/jobs-list.html',{})
def jobs3(request):
    return render(request,'job/jobs-list-side-filter.html',{})



def about(request):
    return render(request,'pages/about-agency.html',{})
def car(request):
    return render(request,'pages/careers.html',{})
def cars(request):
    return render(request,'pages/careers-single.html',{})
def com(request):
    return render(request,'pages/coming-soon.html',{})
def con(request):
    return render(request,'pages/contacts-agency.html',{})
def cons(request):
    return render(request,'pages/contacts-start-up.html',{})
def cover(request):
    return render(request,'pages/cover-page.html',{})
def cust(request):
    return render(request,'pages/customer-story.html',{})
def custs(request):
    return render(request,'pages/customers.html',{})
def erro(request):
    return render(request,'pages/error-404.html',{})
def faq(request):
    return render(request,'pages/faq.html',{})
def hire(request):
    return render(request,'pages/hire-us.html',{})
def invo(request):
    return render(request,'pages/invoice.html',{})
def login(request):
    return render(request,'pages/login.html',{})
def logins(request):
    return render(request,'pages/login-simple.html',{})
def mein(request):
    return render(request,'pages/maintenance-mode.html',{})
def price(request):
    return render(request,'pages/pricing.html',{})
def prive(request):
    return render(request,'pages/privacy.html',{})
def reco(request):
    return render(request,'pages/recover-account.html',{})
def recos(request):
    return render(request,'pages/recover-agency.html',{})
def ser(request):
    return render(request,'pages/services-agency-agency.html',{})
def sign(request):
    return render(request,'pages/signup.html',{})
def signs(request):
    return render(request,'pages/signup-simple.html',{})
def stat(request):
    return render(request,'pages/status.html',{})
def term(request):
    return render(request,'pages/terms.html',{})