from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
# to import the custom user
from django.conf import settings


class UserProfile(models.Model):
    """
    User profile model with default new order information
    & history with previous orders
    """
    # reference to custom user
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    default_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)
    default_address1 = models.CharField(max_length=80,
                                        null=True, blank=True)
    default_address2 = models.CharField(max_length=80,
                                        null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_county = models.CharField(max_length=80,
                                      null=True, blank=True)
    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create new users profile or save new entries
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
 