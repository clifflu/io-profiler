# -*- coding: utf-8 -*-

from subprocess import call

import pylib.fs as fs
import pylib.util as util

def profile(info, raidinfo=None):
  if raidinfo:
    raidinfo.update(info)

  if raidinfo:
    fs.mk_raid(raidinfo)

  fs.mount(info)

  if (util.get_mem_mb() > 1536):
    profile_ramfs(info)

  profile_fio(info)

  fs.umount(info)

  if raidinfo:
    fs.rm_raid(raidinfo)

def profile_ramfs(info):
  FILE_BLK="1k"
  FILE_COUNT="64"
  RAMFS_SZ="1024M"




def profile_fio(info):
  pass
