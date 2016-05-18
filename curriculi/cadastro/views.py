from django.shortcuts import render
from models import Script

def index(request):
	data = Script.objects.all()
	if request.method == 'POST' and request.POST.get('action') == 'save':
		comment = Script()
		comment.nome = request.POST.get('name')
		comment.comentario = request.POST.get('comment')
		comment.save()
	elif request.method == 'POST' and request.POST.get('action') == 'delete':
		_id = request.POST.get('data')
		comment_to_delete = data.get(id=int(_id))
		comment_to_delete.delete()

	return render(request, 'cadastro/index.html', {'data':data})
