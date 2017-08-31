from django.shortcuts import render
from .models import Poll


def index(request):
	all_poll = Poll.objects.all()
	context = {
		'title': 'Django | Poll',
		'polls': all_poll,
	}
	return render(request, 'poll/polls.html', context)
