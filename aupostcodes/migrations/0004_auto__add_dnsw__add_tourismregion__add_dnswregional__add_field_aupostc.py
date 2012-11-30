# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DNSW'
        db.create_table('aupostcodes_dnsw', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('aupostcodes', ['DNSW'])

        # Adding model 'TourismRegion'
        db.create_table('aupostcodes_tourismregion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('aupostcodes', ['TourismRegion'])

        # Adding model 'DNSWRegional'
        db.create_table('aupostcodes_dnswregional', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('aupostcodes', ['DNSWRegional'])

        # Adding field 'AUPostCode.tourism_region'
        db.add_column('aupostcodes_aupostcode', 'tourism_region',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aupostcodes.TourismRegion'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'AUPostCode.dnsw'
        db.add_column('aupostcodes_aupostcode', 'dnsw',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aupostcodes.DNSW'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'AUPostCode.dnsw_regional'
        db.add_column('aupostcodes_aupostcode', 'dnsw_regional',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aupostcodes.DNSWRegional'], null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting model 'DNSW'
        db.delete_table('aupostcodes_dnsw')

        # Deleting model 'TourismRegion'
        db.delete_table('aupostcodes_tourismregion')

        # Deleting model 'DNSWRegional'
        db.delete_table('aupostcodes_dnswregional')

        # Deleting field 'AUPostCode.tourism_region'
        db.delete_column('aupostcodes_aupostcode', 'tourism_region_id')

        # Deleting field 'AUPostCode.dnsw'
        db.delete_column('aupostcodes_aupostcode', 'dnsw_id')

        # Deleting field 'AUPostCode.dnsw_regional'
        db.delete_column('aupostcodes_aupostcode', 'dnsw_regional_id')

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
            'dnsw': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aupostcodes.DNSW']", 'null': 'True', 'blank': 'True'}),
            'dnsw_regional': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aupostcodes.DNSWRegional']", 'null': 'True', 'blank': 'True'}),
            'parcel_zone': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '4', 'primary_key': 'True'}),
            'tourism_region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aupostcodes.TourismRegion']", 'null': 'True', 'blank': 'True'})
        },
        'aupostcodes.dnsw': {
            'Meta': {'object_name': 'DNSW'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aupostcodes.dnswregional': {
            'Meta': {'object_name': 'DNSWRegional'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aupostcodes.tourismregion': {
            'Meta': {'object_name': 'TourismRegion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['aupostcodes']