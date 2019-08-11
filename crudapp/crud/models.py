from django.db import models

class Programming(models.Model):
    language = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    creator = models.CharField(max_length=100)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.language

    def get_absolute_url(self):
        return f"/list/{self.slug}"

