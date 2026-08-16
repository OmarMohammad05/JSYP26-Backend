from django.db import models

# Create your models here.
class VerificationStatus(models.TextChoices):
    TRUE = "true", "True"
    FALSE = "false", "False"
    MISLEADING = "misleading", "Misleading"
    INSUFFICIENT = "insufficient", "Insufficient Evidence"
class RiskLevel(models.TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    CRITICAL = "critical", "Critical"

class MedicalReference(models.Model):
    title = models.CharField(max_length=255)

    source_name = models.CharField(max_length=255)

    evidence_summary = models.TextField()

    url = models.URLField(unique=True)

    publisher_year = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)


class MedicalClaim(models.Model):
    references = models.ManyToManyField(
        MedicalReference,
        related_name="claims"
    )

    claim_text = models.TextField()

    verification_status = models.CharField(
        max_length=20,
        choices=VerificationStatus.choices
    )

    risk_level = models.CharField(
        max_length=20,
        choices=RiskLevel.choices
    )

    explanation = models.TextField()

    search_keyword = models.CharField(
        max_length=255,
        db_index=True
    )

    created_at = models.DateTimeField(auto_now_add=True)