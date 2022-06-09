from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')


def secondpage(request):
	return HttpResponse('I just wanted to show you how much I know!')

def count(request):
	text=request.GET['usertext']
	words = text.split()
	words_counts = {}
	for w in words:
		if w not in words_counts:
			words_counts[w]=1
		else:
			words_counts[w]+=1
	sorted_word_counts = sorted(words_counts.items(), reverse=True, key=operator.itemgetter(1))
	print(sorted_word_counts)
	repetition_no = 0
	for w,c in words_counts.items():
		if c>repetition_no:
			repetition_no=c
			most_repited=w

	return render(request, 'count.html',{'usertext':text, 'count':len(words),'most_reppitted':most_repited,'repetition_no':repetition_no, 'sorted_word_counts':sorted_word_counts})