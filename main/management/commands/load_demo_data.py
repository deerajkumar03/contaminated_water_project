from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import PredictionHistory

class Command(BaseCommand):
    help = "Load demo users and prediction history"

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username="demo").exists():
            demo = User.objects.create_user(username="demo", password="demo1234")

            PredictionHistory.objects.create(user=demo, ph_input=7.1, tds_input=310, result="Safe")
            PredictionHistory.objects.create(user=demo, ph_input=9.0, tds_input=1200, result="Contaminated")

            self.stdout.write("Demo data loaded")
        else:
            self.stdout.write("Demo data already exists")
