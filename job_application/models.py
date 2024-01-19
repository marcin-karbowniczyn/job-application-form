from django.db import models


# Blueprint of Form table in the database
# Jeśli chciałbym zmienić jakoś tę klasę, musiałbym ponownie wykonać komendy makemigration i migrate
class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
