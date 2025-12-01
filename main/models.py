from django.db import models
from django.contrib.auth.models import User

class PredictionHistory(models.Model):
    # Link each prediction to a registered user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Store input values
    ph_input = models.FloatField()
    tds_input = models.FloatField()

    # Store only the ML prediction result: Safe / Moderate / Contaminated
    result = models.CharField(max_length=50)

    # Timestamp of prediction
    prediction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.result} ({self.prediction_date.strftime('%Y-%m-%d %H:%M')})"

    class Meta:
        verbose_name = "Prediction History"
        verbose_name_plural = "Prediction History"
        ordering = ['-prediction_date']
