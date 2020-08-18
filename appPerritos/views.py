from django.shortcuts import render, redirect, HttpResponse
from appPerritos.models import Mascota

# Create your views here.
def index(request):
   return render(request, 'index.html')

def mascotas(request):
   return render(request, 'mascotas.html')

def busqueda_mascota(request):
   return  render(request, "mascota.html")

def buscar(request):
   if request.GET["msct"]:
      perro = request.GET["msct"]
      if len(perro)>20:
         mensaje = "Texto de busqueda muy largo"
      else:
         mascota = Mascota.objects.filter(nombre__icontains=perro)
         return render(request, "resultados_busqueda.html", {"mascota": mascota, "query":perro})
   else:
      mensaje = "Escribe algo ps gil"
   return HttpResponse(mensaje)

def mascota_list(request):
   #mascota = Mascota.objects.all()
   mascota = Mascota.objects.all().order_by('nombre') 
   contexto = {
      'mascotas':mascota
   }
   return render(request, "mascota_list.html", contexto)

def create(request):
   print(request.POST)
   nombre = request.GET['nombre']
   descripcion = request.GET['descripcion']
   perrito_details = Mascota(nombre=nombre, descripcion=descripcion, registrado=True, creado=True, actualizado=True)
   perrito_details.save()
   return redirect('/mascota-list/')

def add_perrito(request):
    return render(request, 'add_perrito.html')

def delete(request, id):
   mascota = Mascota.objects.get(pk=id)
   mascota.delete()
   return redirect('/mascota-list/')

def edit(request, id):
   mascota = Mascota.objects.get(pk=id)
   context = {
      'mascota': mascota
   }
   return render(request, 'edit.html', context)

def update(request, id):
   mascota = Mascota.objects.get(pk=id)
   mascota.nombre = request.GET['nombre']
   mascota.descripcion = request.GET['descripcion']
   mascota.save()
   return redirect('/mascota-list/')