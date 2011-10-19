# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AUPostCode'
        db.create_table('aupostcodes_aupostcode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=4, db_index=True)),
        ))
        db.send_create_signal('aupostcodes', ['AUPostCode'])

        # Adding model 'AUPostalArea'
        db.create_table('aupostcodes_aupostalarea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postcode', self.gf('django.db.models.fields.related.ForeignKey')(related_name='postal_areas', to=orm['aupostcodes.AUPostCode'])),
            ('locality', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('aupostcodes', ['AUPostalArea'])


    def backwards(self, orm):
        
        # Deleting model 'AUPostCode'
        db.delete_table('aupostcodes_aupostcode')

        # Deleting model 'AUPostalArea'
        db.delete_table('aupostcodes_aupostalarea')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '4', 'db_index': 'True'})
        }
    }

    complete_apps = ['aupostcodes']
