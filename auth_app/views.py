from django.shortcuts import render
from shopify_auth.decorators import login_required

@login_required
def home(request):
    return render(request, "home.html")