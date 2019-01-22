from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    qualification = models.CharField(max_length=150, null=True, blank=True)
    experience = models.CharField(max_length=150, null=True, blank=True)
    resume = models.FileField(null=True, blank=True, upload_to='resumes')
    details = models.TextField()

    def __str__(self):
        return "{0} - {1} - {2}".format(self.name, self.qualification, self.experience)


class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.company)




