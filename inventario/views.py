from django.shortcuts import render
from .models import Inventario
from django.utils import timezone
# Create your views here.
def post_list(request):
	posts = Inventario.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'inventario/inventario_list.html', {'posts': posts})
