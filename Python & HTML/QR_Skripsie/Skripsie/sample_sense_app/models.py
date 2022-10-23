from django.db import models
from django.utils import timezone

# Create your models here.

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField('Client Name', max_length=120, blank=True)
    client_email = models.EmailField('Email Address', blank=True)
    client_phone = models.CharField('Contact Number', max_length=25, blank=True)

    def __str__(self):
        return self.client_name

#FEED SAMPLE
class Feed_sample(models.Model):
    # Admin related data
    sample_id = models.AutoField(primary_key=True)
    sample_date = models.DateTimeField(default=timezone.now, blank=True)
    sample_name = models.CharField('Sample Name', max_length=120, blank=True)
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE)
    sample_invoice = models.CharField('Sample Invoice Number', max_length=120, blank=True)
    required_tests = models.CharField('Required tests', max_length=120, blank=True)
    
    # Sample metrics
    AflatoxinB_present = models.CharField('Aflatoxin B concentration', max_length=120, blank=True)
    AflatoxinG_present = models.CharField('Aflatoxin G concentration', max_length=120, blank=True)
    Nivalenol_present = models.CharField('Nivalenol concentration', max_length=120, blank=True)
    Ochratoxin_present = models.CharField('Ochratoxin concentration', max_length=120, blank=True)
    Fumonisin_present = models.CharField('Fumonisin concentration', max_length=120, blank=True)
    Zearalenone_present = models.CharField('Zearalenone concentration', max_length=120, blank=True)
    Deoxynivalenol_present = models.CharField('Deoxynivalenol concentration', max_length=120, blank=True)
    
    def __str__(self):
        return self.sample_name

#RESIDUE SAMPLE
class Residue_sample(models.Model):  
    # Admin related data
    sample_id = models.AutoField(primary_key=True)
    sample_date = models.DateTimeField(default=timezone.now, blank=True)
    sample_name = models.CharField('Sample Name', max_length=120, blank=True)
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.CASCADE)
    sample_invoice = models.CharField('Sample Invoice Number', max_length=120, blank=True)
    required_tests = models.CharField('Required tests', max_length=120, blank=True)

    # Sample metrics to fill in
    Penicillin_present = models.CharField('Penicillin concentration', max_length=120, blank=True)
    Monensin_present = models.CharField('Monensin concentration', max_length=120, blank=True)
    Ampicillin_present = models.CharField('Ampicillin concentration', max_length=120, blank=True)
    Enrofloxacin_present = models.CharField('Enrofloxacin concentration', max_length=120, blank=True)
    Ciprofloxacin_present = models.CharField('Ciprofloxacin concentration', max_length=120, blank=True)
    Sulfadimidine_present = models.CharField('Sulfadimidine concentration', max_length=120, blank=True)
    Chloramphenicol_present = models.CharField('Chloramphenicol concentration', max_length=120, blank=True)

    def __str__(self):
        return self.sample_name