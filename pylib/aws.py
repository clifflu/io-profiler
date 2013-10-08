# -*- coding: utf-8 -*-

_conn = None
def get_conn():
  import boto
  if _conn is None:
    _conn = boto.connect_ec2()

  return _conn

def get_instance_id():
  import urllib
  return urllib.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read()

def get_instance(instance_id = None):
  if instance_id is None:
    instance_id = get_instance_id()
  return get_conn().get_all_instances(instance_ids=[instance_id])[0].instances[0]

def get_instance_signature(instance):
  return {
    'id': instance.id, 
    'type': instance.instance_type,
    'tags': instance.tags,
    'ebs_optimized': instance.ebs_optimized,
  }

