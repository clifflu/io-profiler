#!/usr/bin/env python

URI_META = "http://169.254.169.254/latest/meta-data"

def disks():
    from urllib import urlopen
    global URI_META

    for name in urlopen('%s/%s' % (URI_META, 'block-device-mapping')):
        print(name)
