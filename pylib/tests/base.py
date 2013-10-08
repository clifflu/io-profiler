# -*- coding: utf-8 -*-

class BaseTest(object):
  def applicable(self):
    return False

  def run(self, fp):
    raise Exception('Not Implemented')

  def run_tmpfs(self, fp):
    pass


  def run_fio(self, fp):
    pass


  def execute(self, fp):
    if not self.applicable():
      return False

    return self.run(fp)

class VanillaTest(BaseTest):
  """
  Basic test for single drives
  """

  def applicable(self):
    return True

  def run(self, fp):
    from subprocess import call
    from pylib.util import umount_drives, list_drives

    # mount ebs drive
    disk_mp = '/mnt/ebs'
    dev_name = list_drives('ebs')[0]
    call(['mount', '/dev/%s' % dev_name , disk_mp])

    # umount ebs drive
