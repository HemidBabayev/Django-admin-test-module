from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete= models.CASCADE, verbose_name = "Muellif")
    title = models.CharField(max_length= 50, verbose_name = "Basliq")
    content = models.TextField(verbose_name = "Melumat")
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.title} {self.price} AZN"
    
     