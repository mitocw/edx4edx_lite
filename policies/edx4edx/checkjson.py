#!/usr/bin/python

import json


def check(fn):
    print "checking %s" % fn
    try:
        json.loads(open(fn).read())
        print "Ok"
    except Exception as err:
        raise

check('policy.json')
check('grading_policy.json')
