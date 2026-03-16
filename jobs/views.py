from django.shortcuts import render, redirect
from .models import Job, Application

def home(request):
    jobs = Job.objects.all()
    return render(request, "home.html", {"jobs": jobs})


def post_job(request):

    if request.method == "POST":
        title = request.POST['title']
        company = request.POST['company']
        location = request.POST['location']
        salary = request.POST['salary']
        description = request.POST['description']

        Job.objects.create(
            title=title,
            company=company,
            location=location,
            salary=salary,
            description=description
        )

        return redirect('/')

    return render(request, "post_job.html")


def apply_job(request, id):

    job = Job.objects.get(id=id)

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        resume = request.FILES['resume']

        Application.objects.create(
            name=name,
            email=email,
            resume=resume,
            job=job
        )

        return redirect('/')

    return render(request, "apply_job.html", {"job": job})
