from django.views.generic import TemplateView
from django.http import HttpResponse

class HomeView(TemplateView):
    # def get(self, request):
    #     return redirect="templates/home.html"
    template_name = "home.html"