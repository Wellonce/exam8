from django.contrib import admin
from .models import Form, League, Match, Round, Sport, Statistics, Team, Points, User

@admin.register(Points)
class PointsAdmin(admin.ModelAdmin):
    list_display = ('team', 'points')

admin.site.register(User)
admin.site.register(Sport)
admin.site.register(League)
admin.site.register(Round)
admin.site.register(Team)
admin.site.register(Form)
admin.site.register(Statistics)
admin.site.register(Match)