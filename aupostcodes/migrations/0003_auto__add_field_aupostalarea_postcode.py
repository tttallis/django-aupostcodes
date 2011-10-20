# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'AUPostalArea.postcode'
        db.add_column('aupostcodes_aupostalarea', 'postcode', self.gf('django.db.models.fields.related.ForeignKey')(default='2000', related_name='postal_areas', to=orm['aupostcodes.AUPostCode']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'AUPostalArea.postcode'
        db.delete_column('aupostcodes_aupostalarea', 'postcode_id')


    models = {
        'aupostcodes.aupostalarea': {
            'Meta': {'object_name': 'AUPostalArea'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'postcode': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'postal_areas'", 'to': "orm['aupostcodes.AUPostCode']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'aupostcodes.aupostcode': {
            'Meta': {'object_name': 'AUPostCode'},
            'parcel_zone': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'})
        }
    }

    complete_apps = ['aupostcodes']
