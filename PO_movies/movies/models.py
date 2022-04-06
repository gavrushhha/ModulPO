from django.db import models
import uuid
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _

class UUIMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class DateTimeField(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Genre(UUIMixin, DateTimeField):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = _('genre')
        verbose_name_plural = _('genres')

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(_('full_name'), max_length=255) 
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"person"
        verbose_name = _('person')
        verbose_name_plural = _('persons')

class TypeChoices(models.TextChoices):
    MOVIE = 'MOVIE', 'movie'
    TV_SHOW = 'TV_SHOW', 'tv_show'


class Filmwork(UUIMixin):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True)
    rating = models.FloatField(_('rating'), blank = True, \
        validators=[MinLengthValidator(0), MaxLengthValidator(100)])
    type = models.CharField(_('type'), choices = TypeChoices.choices, max_length=255)
    creation_date = models.DateField(_('created_date'))

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = _('filmwork')
        verbose_name_plural = _('filmworks')

class GenreFilmWork(UUIMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = _('filmwork/genre')
        verbose_name_plural = _('filmworks/genres')


class PersonFilmWork(UUIMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    role = models.TextField(_('role'), blank=True)

    def __str__(self):
        return self.role

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = _('filmwork/person')
        verbose_name_plural = _('filmworks/persons')
