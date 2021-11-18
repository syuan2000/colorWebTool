from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
import random
from json import dumps

from django.views.decorators.cache import cache_control
from django.db import connection

def test(request):
    with connection.cursor() as cursor:
        with open('test.sql') as f:
            lines = f.readlines()
            query = cursor.execute(lines[0])
            result = cursor.fetchall()
            # movie = Movie.objects.raw('''SELECT * FROM "Movie" ''')[0]
            # print(movie)

    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    output = field_names

    for r in result:
        output+= r    
    return HttpResponse(output)

def home(response):
    return render(response, 'main/home.html', {})

def instruction(response):
    return render(response, 'main/instruction.html', {})

def assessment(request):
    movies = random.randint(1,55)
    movie = Movie.objects.filter(id=movies)
    movie_palette = list(Movie.objects.filter(id=1).values_list('top10_palette','kmeans_palette','random_palette'))
    palette =dumps({'top10_palette':movie_palette[0][0], 'kmeans_palette': movie_palette[0][1], 'random_palette':movie_palette[0][2] })
    frames_l = list(Frame.objects.filter(movieid=1).values_list('image').order_by('?')[:10])
    frames={}
    i=1
    for f in frames_l:
        frames[i]=f[0]
        i+=1
    frames = dumps(frames)
    frame_l = list(Frame.objects.filter(movieid=1).values_list('id','image','top10_palette','kmeans_palette','random_palette').order_by('?')[:1])
    frame=dumps({'id':frame_l[0][0],'image':frame_l[0][1], 'top10_palette':frame_l[0][2], 'kmeans_palette': frame_l[0][3], 'random_palette':frame_l[0][4] })

    context={
        'movie_id':movies,
        'movie': movie,
        'frame' : frame,
        'frames' : frames,
        'palette': palette
    }
    if request.method == 'GET':
        return render(request, 'main/assessment.html', context)
    # elif request.method == 'POST':
    #    single = request.POST.get("single")
    #    multiple = request.POST.get("multiple")
    #    if 'top10' in single:
    #        single = 'top10'

    #    Participate.objects.filter(id=1).update(movieid=movies, single_frameid = frame, single_choise = single, multi_choice=multiple)
    #    return redirect('thankYou')

    
def thankYou(response):
    return render(response, 'main/thankYou.html', {})

def assessment_api(request):
    if request.method == 'POST':
        single = request.POST.get("single")
        multiple = request.POST.get("multiple")
        frame_id = request.POST.get("frame_id")
        movie_id = request.POST.get("movie_id")
        if 'top10' in single:
            single = 'top10'
        elif 'random' in single:
            single = 'random'
        else:
            single = 'kmeans'

        if 'top10' in multiple:
            multiple = 'top10'
        elif 'random' in multiple:
            multiple = 'random'
        else: 
            multiple = 'kmeans'
        
        id = Participant.objects.latest('id')
        Participant.objects.update(movieid=movie_id, single_frameid = frame_id, single_choise = single, multi_choice=multiple)
        return redirect('thankYou')
