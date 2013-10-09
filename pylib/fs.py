# -*- coding: utf-8 -*-

from os import makedirs
from subprocess import check_output
from glob import glob

def call(*args, **kwargs):
  """
  mockup to subprocess.call, 
  so we don't break anythin
  """
  #from subprocess import call
  print("call:")
  print(args)


def list_drives(filter=None):
  if filter is None:
    filter = []
  elif type(filter) is not list:
    filter = [filter]

  ebs = glob('/dev/xvd[f-p]')
  eph = glob('/dev/xvd[b-e]')
  md = glob('/dev/md*')

  output = []
  if [] == filter or 'ebs' in filter:
    output = output + ebs
  elif [] == filter or 'eph' in filter:
    output = ouptut + eph
  elif [] == filter or 'md' in filter:
    output = output + md

  return output

def count_drives():
  ebs = list_drives('ebs')
  eph = list_drives('eph')

  return {'ebs': len(ebs), 'eph': len(eph)}

def umount_drives():
  for dr in list_drives():
    call(['unmount', '/dev/%s' % dr])

def warm_ebs_drives():
  for d in list_drives('ebs'):
    call(['dd', 'if=%s' % d, 'of=/dev/null'])
#
#
#
def mount(info):
  """
  mount, dev
  """
  makedirs(info['mount'], 0755)
  call(['mount', info['dev'], info['mount']])

def umount(info):
  call(['umount', info['mount']])

#
#
#
def mk_ramfs(info):
  pass

def mk_raid(info):
  """
  dev, level, srcs
  fs
  """

  if type(info['srcs']) is not list:
    info['srcs']=[info['srcs']]

  call_params = [
    'mdadm', '-f',
    '--create', info['dev'],
    '--level', info['level'],
    '-n%d' % len(info['srcs'])
  ]

  call(call_params + info['srcs'])
  call(['mkfs', '-t', info.get('fs', 'ext3'), info['dev']])

def rm_raid(info):
  """
  dev
  """
  call(['mdadm', '--stop', info['dev']])
  call(['mdadm', '--remove', info['dev']])
