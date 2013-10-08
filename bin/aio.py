#!/usr/bin/env python
import boto
import urllib

conn = boto.connect_ec2()
my_id = urllib.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read()

def get_instance():
  global conn, my_id
  return conn.get_all_instances(instance_ids=[my_id])[0].instances[0]

def get_sig():
  i = get_instance()
  return {
    'id': i.id, 
    'type': i.instance_type,
    'tags': i.tags,
    'ebs_optimized': i.ebs_optimized,
  }


