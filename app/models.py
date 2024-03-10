from django.db import models
class Pokemon(models.Model):
    pokemon_name = models.CharField(primary_key=True, max_length=100,  default='')
    def __str__(self):
        return f'Pokemon: {self.pokemon_name}'