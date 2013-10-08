# -*- coding: utf-8 -*-

from pylib.aws import get_instance_id
from os.path import dirname

PROF = dirname(__file__)
BIN = "%s/bin" % PROF
MY_LOG = "%s/logs/%s/" % (PROF, get_instance_id())
