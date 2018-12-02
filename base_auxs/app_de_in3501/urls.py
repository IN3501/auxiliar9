from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	# formato: dirección_pag, función_asociada , name=nombre
    path('',views.index, name='index'),
	path('lista_usuarios',views.lista_usuarios, name='lista_usuarios'),
	path('lista_cursos', views.lista_cursos, name='lista_cursos'),
	path('inputs', views.inputs, name='inputs'),
    path('added', views.added, name='added'),
	path('formularios', views.formularios, name='formularios'),
	path('added_curso', views.added_curso, name='added_curso'),
	path('updated_curso', views.updated_curso, name='updated_curso'),
	path('deleted_curso', views.deleted_curso, name='deleted_curso'),
	path('login/', views.loginView, name='login'),
	path('logout/', views.logoutView, name='logout'),

]