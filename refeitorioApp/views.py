from django.shortcuts import render, get_object_or_404
from refeitorioApp.forms import AlunoForms
from refeitorioApp.forms import AlunoEvento
from refeitorioApp.models import Aluno

# Create your views here.
def home(request):
    form = AlunoForms()
    context = {'form': form}
    return render(request, 'refeitorio/home.html', context)

def new_aluno(request):
    alunos = Aluno.objects.all()
    form= AlunoForms(request.POST, request.FILES)
    if request.method == "POST":
        #form=AlunoForms(request.POST, request.FILES)
        if form.is_valid():
            aluno=form.save()
            aluno.save()
            form=AlunoForms
    context={'form':form, 'alunos':alunos}
    return render(request, 'refeitorio/new_aluno.html',context)

#Usar esse caso quando o template for único para exibir alunos
def mostrar_aluno(request):
    alunos = Aluno.objects.all() #exibe todos objetos da classe Aluno
    context={'alunos': alunos}
    return render(request, 'refeitorio/new_aluno.html', context)

def evento(request):
    form = AlunoEvento()
    context = {'form': form}
    return render(request, 'refeitorio/evento.html', context)

def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form= AlunoForms(instance=aluno)
    if (request.method =='POST'):
        form = AlunoForms(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('new_aluno')
        else:
            return render(request, 'refeitorio/editar_aluno.html',{'form':form})
    else:
        return render(request, 'refeitorio/editar_aluno.html',{'form':form})

def excluir_aluno(request, id):
    aluno =get_object_or_404(Aluno, pk=id)
    form = AlunoForms(instance=aluno)
    alunos= Aluno.objects.all()
    if (request.method == 'POST'):
        form = AlunoForms(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('new_aluno')
        else:
            return render(request, 'refeitorio/excluir_aluno.html', {'form': form})
    else:
        return render(request, 'refeitorio/excluir_aluno.html', {'form': form})