from django.shortcuts import render
from django.http import JsonResponse
from .models import Estado, Municipio

def estados_municipios_view(request):
    estados = Estado.objects.all() 
    return render(request, 'estados.html', {'estados': estados})

def cargar_municipios(request):
    estado_id = request.GET.get('estado_id') 
    municipios = Municipio.objects.filter(estado_id=estado_id).values('id', 'nombre') 
    return JsonResponse(list(municipios), safe=False) 
