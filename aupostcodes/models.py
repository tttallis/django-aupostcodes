try:
    from django_localflavor_au.au_states import STATE_CHOICES # Django >= 1.5
except ImportError:
    from django.contrib.localflavor.au.au_states import STATE_CHOICES
from django.db import models


class AUPostCode(models.Model):
    """
    A valid Australian Post Code
    """
    postcode = models.CharField(primary_key=True, max_length=4)
    parcel_zone = models.CharField(max_length=3)
    tourism_region = models.ForeignKey('TourismRegion', blank=True, null=True)
    dnsw = models.ForeignKey('DNSW', blank=True, null=True)
    dnsw_regional = models.ForeignKey('DNSWRegional', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Australian Post Code'
        
    def __unicode__(self):
        return self.postcode
    
    @property
    def states(self):
        return tuple(set(pa.state for pa in self.postal_areas.all()))
    

class AUPostalArea(models.Model):
    """
    An Australian postal area
    """
    postcode    = models.ForeignKey(AUPostCode, related_name='postal_areas')
    locality    = models.CharField(max_length=255)
    state       = models.CharField(max_length=3, choices=STATE_CHOICES)
    
    class Meta:
        verbose_name = 'Australian postal area'
        
    def __unicode__(self):
        return "%s (%s)" % (self.locality, self.postcode)

class TourismRegion(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)

class DNSW(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)

class DNSWRegional(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)
