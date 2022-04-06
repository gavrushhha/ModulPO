from django.contrib import admin
from .models import Genre
from .models import Person, Filmwork, GenreFilmWork, PersonFilmWork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(PersonFilmWork)
class PersonFilmWorkInLine(admin.ModelAdmin):
    model = PersonFilmWork


@admin.register(GenreFilmWork)
class GenreFilmWorkInLine(admin.ModelAdmin):
    model = GenreFilmWork

@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    # inlines = (GenreFilmWork,)
    list_display = ('title', 'type', 'creation_date', 'rating')
    list_filter = ('type',)
    search_fields = ('title', 'description', 'rating')

