######################################################################
#
# File: b2sdk/version.py
#
# Copyright 2019 Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################

import sys

try:
    from importlib.metadata import version, PackageNotFoundError
except ModuleNotFoundError:
    from importlib_metadata import version, PackageNotFoundError  # for python 3.7

try:
    VERSION = version('b2sdk')
except PackageNotFoundError:
    from pkg_resources import get_distribution, DistributionNotFound

    VERSION = get_distribution("b2sdk").version

PYTHON_VERSION = '.'.join(map(str, sys.version_info[:3]))  # something like: 3.9.1

USER_AGENT = 'backblaze-b2/%s python/%s' % (VERSION, PYTHON_VERSION)
