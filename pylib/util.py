# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

def get_mem_mb():
  p1 = Popen(["free", "-m"], stdout=PIPE)
  p2 = Popen(["awk", "FNR==2 {print $2}"], stdin=p1.stdout, stdout=PIPE)
  p1.stdout.close()
  return int(p2.communicate()[0].strip())

