from django.shortcuts import render
from .models import Match, Points, League, Sport

def index(request):
    live_matches = Match.objects.filter(live=True)
    upcoming_matches = Match.objects.filter(status='Not Started')
    completed_matches = Match.objects.filter(status='Completed')
    team_standings = Points.objects.all().order_by('-points', 'team__name')
    sports = Sport.objects.all()
    leagues = League.objects.all()
    return render(request, 'index.html', {'live_matches': live_matches, 'sports':sports, 'leagues': leagues, 'upcoming_matches': upcoming_matches, 'completed_matches': completed_matches, 'team_standings': team_standings})
