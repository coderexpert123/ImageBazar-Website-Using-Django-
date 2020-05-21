from django.db import models

# Create your models here.

# crate categiory models
class Category (models.Model):
    tittle=models.CharField(max_length=100)
    dscription=models.TextField()

    def __str__(self):
        return self.tittle

# Create Images Models
class Image(models.Model):
    tittle=models.CharField(max_length=100)
    dscription=models.TextField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle




