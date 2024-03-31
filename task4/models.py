from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.db.models import (
    Model,
    DateField,
    CharField,
    ImageField,
    ManyToManyField,
    TextField,
    ForeignKey,
    CASCADE,
    DateTimeField,
)
from django.forms import IntegerField

class AbstractModel(Model):
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractModel):
    username = CharField(max_length=128)
    password = CharField(max_length=128)

    def __str__(self):
        return self.username



class Sport(AbstractModel):
    name = models.CharField(max_length = 128)

    def __str__(self):
        return self.name

class League(AbstractModel):
    sport = models.ForeignKey(Sport, models.CASCADE)
    name = CharField(max_length=128)
    cover = ImageField(upload_to="media",)

    def __str__(self):
        return self.name
    
class Round(AbstractModel):
    name = CharField(max_length=128)
    number = IntegerField()

    def __str__(self):
        return self.name


class Team(models.Model):
    sport = models.ForeignKey(Sport, models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Form(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Statistics(AbstractModel):
    team_id = ManyToManyField("Team", related_name="statistics")
    mp = IntegerField()
    w = IntegerField()
    d = IntegerField()
    l = IntegerField()
    gd = IntegerField()
    pts = IntegerField()

    def __str__(self):
        return self.team_id
    
    class Meta:
        verbose_name = "Statistics"
        verbose_name_plural = "Statistics"



class Match(models.Model):
    sport = models.ForeignKey(Sport, models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    date = models.DateTimeField()
    score = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=20, default='Not Started')
    live = models.BooleanField(default=False)


@receiver(post_save, sender=Match)
def update_points(sender, instance, created, **kwargs):
    if created:
        home_team_points = Points.objects.get_or_create(team=instance.home_team)[0]
        away_team_points = Points.objects.get_or_create(team=instance.away_team)[0]

        if instance.score:
            home_score, away_score = map(int, instance.score.split('-'))
            if home_score > away_score:
                home_team_points.points += 3
            elif home_score == away_score:
                home_team_points.points += 1
                away_team_points.points += 1
            else:
                away_team_points.points += 3

            home_team_points.save()
            away_team_points.save()


    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
    
class Points(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team} - Points: {self.points}"

    class Meta:
        verbose_name = "Points"
        verbose_name_plural = "Points"


