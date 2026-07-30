from django.db import models

class Celebrity(models.Model):
    photo = models.ImageField(upload_to="celebrities/", blank=True, null=True)
    name = models.CharField(max_length=100)
    free_text = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    

class Package(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE, related_name="packages")
    package_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="packages/", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    benefits = models.TextField()


class WebsiteSettings(models.Model):
    support_link = models.CharField(max_length=500)

    support_text = models.CharField(
        max_length=100,
        default="Support"
    )
    def __str__(self):
        return "Website Settings"