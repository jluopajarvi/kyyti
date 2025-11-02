from django.db import models
from django.contrib.auth.models import User


class Organizer(models.Model):
    """
    Model representing a sports event organizer.
    Each organizer can manage VIP rides for their events.
    """
    name = models.CharField(max_length=255, unique=True)
    contact_details = models.TextField(
        help_text="Contact information (phone, email, etc.)"
    )
    address = models.TextField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class OrganizerUser(models.Model):
    """
    Junction table mapping users to organizers with specific roles.
    Allows a user to have different roles for different organizers.
    """
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
        ('viewer', 'Viewer'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organizer_roles')
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name='users')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'organizer']
        ordering = ['organizer', 'user']

    def __str__(self):
        return f"{self.user.username} - {self.organizer.name} ({self.role})"


class Customer(models.Model):
    """
    Model representing a customer mapped to an organizer.
    Customers are associated with specific organizers.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_profiles')
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name='customers')
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, help_text="Additional notes about the customer")

    class Meta:
        unique_together = ['user', 'organizer']
        ordering = ['organizer', 'user']

    def __str__(self):
        return f"{self.user.username} - {self.organizer.name}"
