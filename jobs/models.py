from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Application(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    resume = models.FileField(upload_to="resumes/")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.name