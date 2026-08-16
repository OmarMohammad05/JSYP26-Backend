from django.db import models
from django.conf import settings
# Create your models here.
class  ChronicCondition(models.Model):
    # Types of diseases.
    name=models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name
class UserCondition(models.Model):
    chronic_condition=models.ForeignKey(ChronicCondition,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["user", "chronic_condition"],
                name ="unique_user_chronic_condition"
            )
        ]
    def __str__(self):
        return f"{self.user.username} - {self.chronic_condition.name}"