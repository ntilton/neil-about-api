from django.db import models

# Create your models here.
class Company(models.Model):
    company = models.CharField(max_length=255)
    blurb = models.CharField(max_length=1000, null=True, blank=True)
    dateStart = models.DateField()
    dateEnd = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

class Role(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    dateStart = models.DateField()
    dateEnd = models.DateField(null=True, blank=True)
    skills = models.ManyToManyField('Skill', blank=True, related_name='duties')

    def __str__(self):
        return f"{self.company} | {self.title}"

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

class Duty(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)  

    def __str__(self):
        return f"{self.role} | {self.description}"

    class Meta:
        verbose_name = 'Duty'
        verbose_name_plural = 'Duties'

class Skill(models.Model):
    name = models.CharField(max_length=250)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'