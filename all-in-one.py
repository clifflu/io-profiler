#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import dumps

import pylib
import pylib.util
import pylib.aws
from pylib.path import MY_LOG

# write instance info
with open("%s/instance.json" % MY_LOG, "w") as fp:
  fp.write(dumps(pylib.aws.get_instance_signature()))

# output fp
with pylib.util.get_log_fp() as fp:
  for test in pylib.tests:
    test.execute(fp)
    fp.flush()
