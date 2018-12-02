from django import forms
from .models import Cursos

class FormularioCurso(forms.Form):
	nombre = forms.CharField(label='Ingrese curso',widget=forms.TextInput(
		attrs={
			'class':'form-control',
		}))

	codigo = forms.IntegerField(label='Ingrese codigo', widget=forms.TextInput(
		attrs={
			'class':'form-control',
		}))

	ud = forms.IntegerField(label='Ingrese  valor UD', widget=forms.TextInput(
		attrs={
			'class':'form-control',
		}))
	horario = forms.DateTimeField(label='Ingrese horario', widget=forms.TextInput(
		attrs={
			'class':'form-control',
		}))
	anho = forms.DateField(label='Ingrese año', widget=forms.TextInput(
		attrs={
			'class':'form-control',
		}))

	semestres=((1 , 'Otoño'),(2 , 'Primavera'))
	semestre = forms.ChoiceField(choices=semestres, label='Escoja semestre',widget=forms.Select(
		attrs={
			'class':'form-control',
		}))

	departamentos=((1 , 'Industrias'),(2 , 'Computación'))
	departamento = forms.ChoiceField(choices=departamentos, label='Escoja departamento',widget=forms.Select(
		attrs={
			'class':'form-control',
		}))

class FormularioUD(forms.Form):
	def __init__(self, *args, **kwargs):
		super(FormularioUD, self).__init__(*args, **kwargs)
		cursos = Cursos.objects.all().values_list('id', 'nombre')
		self.fields['curso'] = forms.ChoiceField(choices=cursos, label='Escoja curso',widget=forms.Select(
		attrs={
			'class':'form-control',
		}))

	ud = forms.IntegerField(label='Ingrese  valor UD', widget=forms.TextInput(
		attrs={
			'class': 'form-control',
		}))

class FormularioDelete(forms.Form):
	semestres=((1 , 'Otoño'),(2 , 'Primavera'))
	semestre = forms.ChoiceField(choices=semestres, label='Escoja semestre',widget=forms.Select(
		attrs={
			'class':'form-control',
		}))


