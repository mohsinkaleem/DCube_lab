from django.db import models

# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=250, blank=True, null=True)
    author=models.CharField(max_length=250, blank=True, null=True)
    date=models.DateTimeField(null=True,blank=True)
    blog= models.TextField(max_length=10000, null=True)
    image=models.FileField(null=True, upload_to='media', blank=True)

    def __str__(self):
        return str(self.id)+": " + str(self.title)

class Publications(models.Model):
    title=models.CharField(max_length=250,null=True,blank=True)
    year=models.IntegerField(max_length=4,null=True,blank=True)
    pdf_link=models.URLField(max_length=250,null=True,blank=True)
    page_link=models.URLField(max_length=250,null=True,blank=True)
    author=models.CharField(max_length=250,null=True)

    def __str__(self):
        return f"{self.year}-{self.title}"

