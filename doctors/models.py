from django.db import models


class Doctor(models.Model):
    CATEGORY_CHOICES = [
        ("Internal Medicine", "Internal Medicine"),
        ("Pediatrics", "Pediatrics"),
        ("Gynecology", "Gynecology"),
        ("Surgery", "Surgery"),
        ("Laboratory", "Laboratory"),
        ("Neonatology", "Neonatology"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    experience_years = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.category}"
