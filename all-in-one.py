#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import dumps

import pylib
import pylib.util as util
import pylib.aws as aws

from pylib.tests import profile

DRIVE_COUNT = util.count_drives()

# write instance info
aws.log_instance_signature()

# prepare
util.umount_drives()

# single-disk tests
if DRIVE_COUNT['ebs'] > 0:
  profile({
    'name': 'singular ebs',
    'dev': util.list_drives('ebs')[0],
    'mount': '/mnt/ebs',
  })
