"""
Import postal area data from the Australia Post csv of same.

At time of writing, this was available at 
http://auspost.com.au/static/docs/pc-full_20110905.csv
or from http://auspost.com.au/apps/postcode.html.
"""

from django.core.management.base import NoArgsCommand
import csv
import sys
import os
from aupostcodes.models import AUPostCode, TourismRegion, DNSW, DNSWRegional

class Command(NoArgsCommand):
    args = ''
    help = """Harvests Australian postcode data from csv file supplied by Australia Post"""


    def handle_noargs(self, **options):
        n = 0
        here = os.path.dirname(__file__)
        filepath = os.path.join(here, '../../data/dnsw.csv')
        reader = csv.reader(open(filepath, 'U'))
        reader.next() # skip headers
        for line in reader:
            postcode, tourism, dnsw, regional = line[4:8]
            tourism_region, created = TourismRegion.objects.get_or_create(name=tourism)
            dnsw, created = DNSW.objects.get_or_create(name=tourism)
            dnsw_regional, created = DNSWRegional.objects.get_or_create(name=tourism)
            try:
                postcode = AUPostCode.objects.get(postcode=postcode)
                postcode.tourism_region = tourism_region
                postcode.dnsw = dnsw
                postcode.dnsw_regional = dnsw_regional
                postcode.save()
            except AUPostCode.DoesNotExist:
                print "WARNING: %s not found" % postcode
                
            
#             au_postcode, created = AUPostCode.objects.get_or_create(postcode=postcode, parcel_zone=parcel_zone)
#             au_postal_area = AUPostalArea(postcode=au_postcode, locality=locality, state=state)
#             au_postal_area.save()        
#             n += 1
#             if n % 100 == 0:
#                 print "Processed %s postcodes." % n
