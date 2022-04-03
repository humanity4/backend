from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    description = models.CharField(blank=True, max_length=2048)

class NeighborhoodImages(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    link = models.ImageField()

class SisterOrg(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    description = models.CharField(blank=True, max_length=2048)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True)

class Supporter(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(primary_key=True, max_length=512)
    affiliation = models.ForeignKey(SisterOrg, on_delete=models.SET_NULL, null=True)
    join_date = models.DateField()

class Donation(models.Model):
    donor = models.ForeignKey(Supporter, on_delete=models.PROTECT)
    recipient = models.ForeignKey(Neighborhood, on_delete=models.PROTECT)
    amount_cents = models.IntegerField()
    currency = models.CharField(max_length=3, choices=(("USD", "US Dollars"),("CAD","Canadian Dollars")))
    recurring = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField(null=True)

class FundingGoal(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE) 
    cost_cents = models.IntegerField()
    recurring = models.BooleanField()

class FundingGoalImages(models.Model):
    funding_goal = models.ForeignKey(FundingGoal, on_delete=models.CASCADE)
    link = models.ImageField()
