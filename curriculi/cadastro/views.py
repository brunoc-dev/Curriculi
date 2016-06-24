from django.shortcuts import render
<<<<<<< HEAD
from models import Script
import json

data = Script.objects.all()


def save(request):
    print json.loads(request.body)['name']
    if request.method == 'POST':
        comment = Script()
        comment.nome = json.loads(request.body)['name']
        comment.comentario = json.loads(request.body)['comment']
        comment.save()

    return render(request, 'cadastro/index.html', {'data': data})


def delete(request):
    if request.method == 'POST':
        _id = json.loads(request.body)['data']
        comment_to_delete = data.get(id=int(_id))
        comment_to_delete.delete()


def index(request):
    return render(request, 'cadastro/index.html', {'data': data})
=======


# Create your views here.

def index(request):
	return render(request, 'cadastro/base_html',{})
>>>>>>> bdcb33a421f4c76d5b4aef65749b1120855a3125
