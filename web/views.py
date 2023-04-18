from django.shortcuts import render, redirect
from django.db.models import Q
from crud.models import Member


# Create your views here.

def index(request):
    search_query = request.GET.get('search', '')  # Get the search query from the request
    if search_query:
        # If there is a search query, filter members based on the query
        members = Member.objects.filter(
            Q(firstname__icontains=search_query) | Q(lastname__icontains=search_query)
        )
    else:
        # If there is no search query, return all members
        members = Member.objects.all()

    context = {'members': members}
    return render(request, 'crud/index.html', context)


def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect('/')


def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)


def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return redirect('/crud/')


def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')


def index_redirect(request):
    return redirect('/crud/')


def SAttendance(request):
    return redirect('/crud/')


def Home():
    return redirect('/crud/')


def attendence():
    return redirect('/crud/')
