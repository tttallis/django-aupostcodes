# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'AUPostCode.id'
        db.delete_column('aupostcodes_aupostcode', 'id')

        # Adding field 'AUPostCode.parcel_zone'
        db.add_column('aupostcodes_aupostcode', 'parcel_zone', self.gf('django.db.models.fields.CharField')(default='', max_length=3), keep_default=False)

        # Changing field 'AUPostCode.postcode'
        db.alter_column('aupostcodes_aupostcode', 'postcode', self.gf('django.db.models.fields.CharField')(max_length=4, primary_key=True))

        # Removing index on 'AUPostCode', fields ['postcode']
        db.delete_index('aupostcodes_aupostcode', ['postcode'])

        # Adding unique constraint on 'AUPostCode', fields ['postcode']
        db.create_unique('aupostcodes_aupostcode', ['postcode'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'AUPostCode', fields ['postcode']
        db.delete_unique('aupostcodes_aupostcode', ['postcode'])

        # Adding index on 'AUPostCode', fields ['postcode']
        db.create_index('aupostcodes_aupostcode', ['postcode'])

        # Adding field 'AUPostCode.id'
        db.add_column('aupostcodes_aupostcode', 'id', self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True), keep_default=False)

        # Deleting field 'AUPostCode.parcel_zone'
        db.delete_column('aupostcodes_aupostcode', 'parcel_zone')

        # Changing field 'AUPostCode.postcode'
        db.alter_column('aupostcodes_aupostcode', 'postcode', self.gf('django.db.models.fields.CharField')(max_length=4))


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
