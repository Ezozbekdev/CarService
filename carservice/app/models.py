from django.db import models


class About_Md(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class Furnitures(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='Lib/fu-imgs')
    about = models.TextField()

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    img = models.ImageField(upload_to='Lib/te-imgs')
    name = models.CharField(max_length=120)
    ceo = models.CharField(max_length=120)
    about = models.TextField()

    def __str__(self):
        return self.name


class ConatactUs(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    massage = models.TextField()

    def __str__(self):
        return self.full_name


class Main(models.Model):
    main = "Main model"
    Ab = models.ManyToManyField(About_Md)
    Fu = models.ManyToManyField(Furnitures)
    Te = models.ManyToManyField(Testimonial)
    Co = models.ManyToManyField(ConatactUs)

    def __str__(self):
        return self.main
