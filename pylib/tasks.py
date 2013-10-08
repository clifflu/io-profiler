# -*- coding: utf-8 -*-
#
# 各種測試
#

from subprocess import check_output

def profile_tmpfs(mount_point):
  """
  perform tmpfs test
  """
  from pylib.path import BIN

  return check_output(["%s/test_tmpfs.sh"])

def profile_fio():
  pass
