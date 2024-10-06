from django.contrib import admin
from .models import About, Skill, Resume, Education, Experience, PortfolioCategory, PortfolioItem

# Inline classes
class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1  # Number of empty forms to display

 # Number of empty forms to display

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1  # Number of empty forms to display

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1  # Number of empty forms to display

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    inlines = [SkillInline]



@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'about', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    inlines = [EducationInline, ExperienceInline]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year')
    search_fields = ('degree', 'institution')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_year', 'end_year')
    search_fields = ('job_title', 'company')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'about', 'proficiency')
    list_filter = ('about',)
    search_fields = ('skill_name',)

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Admin pour les items du portfolio
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description')
    search_fields = ('title', 'category__name')
    list_filter = ('category',)