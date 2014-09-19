# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SitewideMessages'
        db.create_table(u'main_sitewidemessages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('body', self.gf('markitup.fields.MarkupField')(no_rendered_field=True)),
            (u'_body_rendered', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'main', ['SitewideMessages'])


    def backwards(self, orm):
        # Deleting model 'SitewideMessages'
        db.delete_table(u'main_sitewidemessages')


    models = {
        u'main.sitewidemessages': {
            'Meta': {'object_name': 'SitewideMessages'},
            u'_body_rendered': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'body': ('markitup.fields.MarkupField', [], {u'no_rendered_field': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']