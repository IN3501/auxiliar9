from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Usuarios, Cursos, RolUsuarioCurso
from .forms import FormularioCurso, FormularioUD,FormularioDelete
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request,'app_de_in3501/index.html')

def lista_usuarios(request):
    contexto = {}
    contexto['usuarios'] = Usuarios.objects.all()
    return render(request,'app_de_in3501/lista_usuarios.html', contexto)

def lista_cursos(request):
    contexto = {}
    contexto['cursos_otonio'] = Cursos.objects.filter(semestres_id=1)
    contexto['cursos_primavera'] = Cursos.objects.filter(semestres_id=2)
    return render(request,'app_de_in3501/lista_cursos.html', contexto)

def inputs(request):
    return render(request, 'app_de_in3501/inputs.html')
   
def added(request):
    new_user=Usuarios(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
                      direccion=request.POST['direccion'], rut=request.POST['rut'],
                      puntaje_psu=request.POST['puntaje_psu'], username=request.POST['username'],
                      password=request.POST['password'], email=request.POST['email']);
    new_user.save()
    context={'Titulo':'Formulario Correcto', 'comentario':'Gracias'}
    return render(request, 'app_de_in3501/added.html', context)

def formularios(request):
    form_add = FormularioCurso()
    form_update = FormularioUD()
    form_delete = FormularioDelete()

    info = {'titulo': 'Agregar Curso', 'intro': "Ingrese los datos del Curso",
            'form_add': form_add, 'form_update':form_update, 'form_delete':form_delete}

    return render(request, 'app_de_in3501/formularios.html', info)

def added_curso(request):
    #Para evitar error en la recepción de los datos del formulario se usa .get()
    semestre = request.POST.get('semestre')
    departamento = request.POST.get('departamento')

    nuevo_curso = Cursos(nombre=request.POST['nombre'], ud=request.POST['ud'],
                        codigo=request.POST['codigo'], semestres_id=semestre,
                        departamento_id=departamento, horario=request.POST['horario'],
                        anho=request.POST['anho']);
    nuevo_curso.save()
    context = {'Titulo': 'Formulario Correcto', 'comentario': 'Gracias'}
    return render(request, 'app_de_in3501/added.html', context)

def updated_curso(request):
    #Para evitar error en la recepción de los datos del formulario se usa .get()
    ud = request.POST.get('ud')
    curso = request.POST.get('curso')

    select_curso = Cursos.objects.get(id=curso)
    select_curso.ud = ud
    select_curso.save()

    context = {'Titulo': 'Formulario Correcto', 'comentario': 'Gracias'}
    return render(request, 'app_de_in3501/added.html', context)

def deleted_curso(request):
    #Para evitar error en la recepción de los datos del formulario se usa .get()
    semestre = request.POST.get('semestre')

    #Se filtra por semestre.
    #values_list() retorna los resultados en forma de Array
    #la opción flat=TRUE entraga los valores indivuales: [1,2,3]
    #en caso contrario retorna un Array de tuplas de la forma: [(1,),(2,),(3,)]
    select_cursos_id = Cursos.objects.filter(semestres_id = semestre).values_list('id', flat=True)

    if select_cursos_id is not None:
        select_cursos_id = list(select_cursos_id)
        #SELECT cursos_id
        #FROM rol_usuario_curso
        #WHERE cursos_id IN %select_cursos%
        select_rol_usuario_curso = RolUsuarioCurso.objects.filter(cursos_id__in = select_cursos_id)

        #Eliminamos los registros ordenadamente para evitar problemas de referencias cruzadas
        select_rol_usuario_curso.delete()

        select_cursos = Cursos.objects.filter(id__in = select_cursos_id)
        select_cursos.delete()

    context = {'Titulo': 'Formulario Correcto', 'comentario': 'Gracias'}
    return render(request, 'app_de_in3501/added.html', context)

def loginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
    return render(request, 'app_de_in3501/login.html')

def logoutView(request):
    logout(request)
    return redirect('/')