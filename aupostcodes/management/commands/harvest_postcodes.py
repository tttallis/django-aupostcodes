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
from aupostcodes.models import AUPostalArea, AUPostCode

class Command(NoArgsCommand):
    args = ''
    help = """Harvests Australian postcode data from csv file supplied by Australia Post"""


    def handle_noargs(self, **options):
        n = 0
        here = os.path.dirname(__file__)
        filepath = os.path.join(here, '../../data/pc-full_20110905.csv')
        reader = csv.reader(open(filepath, 'U'))
        reader.next() # skip headers
        for line in reader:
            postcode, locality, state = line[:3]
            au_postcode, created = AUPostCode.objects.get_or_create(postcode=postcode)
            au_postal_area = AUPostalArea(postcode=au_postcode, locality=locality, state=state)
            au_postal_area.save()        
            n += 1
            if n % 100 == 0:
                print "Processed %s postcodes." % n
