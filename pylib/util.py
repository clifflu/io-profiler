# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
from datetime import datetime

def get_mem_mb():
  p1 = Popen(["free", "-m"], stdout=PIPE)
  p2 = Popen(["awk", "FNR==2 {print $2}"], stdin=p1.stdout, stdout=PIPE)
  p1.stdout.close()
  return int(p2.communicate()[0].strip())

def get_log_fp():
  from os import makedirs
  from pylib.path import MY_LOG

  makedirs(MY_LOG, 0755)
  filename = "%s/%s.log" % (MY_LOG, datetime.now().isoformat())

  return open(filename, "w")

def list_drives(filter=None):
  from glob import glob

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

def unmount_drives():
  from subprocess import call
  for dr in list_drives():
    call(['unmount', '/dev/%s' % dr])
