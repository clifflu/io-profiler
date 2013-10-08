# -*- coding: utf-8 -*-
#
# 整合 AWS 提供之各種服務
#

import boto
import urllib
from datetime import datetime

#
# Instance
#
def get_instance_id():
  return urllib.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read()

def get_instance(instance_id=None):
  if instance_id is None:
    instance_id = get_instance_id()
  return boto.connect_ec2().get_all_instances(instance_ids=[instance_id])[0].instances[0]

def get_instance_signature(instance=None):
  if type(instance) is str:
    instance = get_instance(instance)
  elif instance is None:
    instance = get_instance(instance)

  return {
    'id': instance.id,
    'type': instance.instance_type,
    'name': instance.tags['Name'],
    'ebs_optimized': instance.ebs_optimized,
  }

#
# Log with DynamoDB
#

def _log(table_name, hash_key_name, attrs, range_key_name=None):
  conn = boto.connect_dynamodb()

  table = conn.get_table(table_name)

  hash_key = attrs[hash_key_name]
  del attrs[hash_key_name]

  if range_key_name is None:
    item = table.new_item(hash_key=hash_key, attrs=attrs)
  else:
    range_key = attrs[range_key_name]
    del attrs[range_key_name]
    item = table.new_item(hash_key=hash_key, range_key=range_key, attrs=attrs)

  conn.put_item(item)

def log_instance_signature(instance=None):
  attrs = get_instance_signature(instance)
  _log('instances', 'id', attrs)

def log_test_result(instance, test_name, result):
  payload = {
    'instance_id': instance['id'],
    'created': datetime.now().isoformat(),
    'test_name': test_name,
    'result': result,
  }

  _log('results', 'instance_id', payload, range_key_name="created")


