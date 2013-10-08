# -*- coding: utf-8 -*-

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

def mount(info):
  """
  mount, dev
  """
  mkdirs(info['mount'], 0755)
  call(['mount', info['dev'], info['mount']])

def umount(info):
  call(['umount', info['mount']])

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
