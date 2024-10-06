from django.db import models
from django.core.exceptions import ValidationError

class About(models.Model):
    name = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    about_me = models.TextField()

    def __str__(self):
        return self.name

    def get_full_name(self):
        return self.name

class Skill(models.Model):
    about = models.ForeignKey(About, related_name='skills', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text='Proficiency in percentage (0-100)')

    def clean(self):
        if not (0 <= self.proficiency <= 100):
            raise ValidationError('Proficiency must be between 0 and 100.')

    def __str__(self):
        return self.skill_name

class Resume(models.Model):
    about = models.ForeignKey(About, related_name='resumes', on_delete=models.CASCADE, help_text="Le CV associé à la personne.")
    name = models.CharField(max_length=100)
    summary = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    start_year = models.IntegerField(help_text='Year education started')
    end_year = models.IntegerField(help_text='Year education ended')
    

    def __str__(self):
        return f"{self.degree} - {self.institution} ({self.start_year} - {self.end_year})"

class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name='experience', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True, help_text='Year job started')
    end_year = models.IntegerField(null=True, blank=True, help_text='Year job ended')
    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.job_title if self.job_title else 'No Job Title'


# Ajouter le portfolio ici
class PortfolioCategory(models.Model):
    
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    about = models.ForeignKey(About, related_name='portfolio_items', on_delete=models.CASCADE)  # Lien avec le modèle About
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank= True)
    image = models.ImageField(upload_to='portfolio_images/')
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, related_name='projects')
    detail_link = models.URLField(max_length=200, blank=True, null=True)
    gallery_image = models.ImageField(upload_to='portfolio_gallery/', blank=True, null=True)
    
    def __str__(self):
        return self.title
