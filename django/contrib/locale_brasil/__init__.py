# -*- coding: utf-8 -*-

import os
import locale


#
# Defines the customized locale for Brazilian Portuguese
#
CURDIR = os.path.dirname(os.path.abspath(__file__))

os.environ['LOCPATH'] = os.path.join(CURDIR, '../../conf/locale/')
os.environ['NLSPATH'] = os.path.join(CURDIR, '../../conf/locale/')

locale.setlocale(locale.LC_ALL, b'pt_BR.UTF-8')
locale.setlocale(locale.LC_COLLATE, b'pt_BR.UTF-8')

os.environ['LANG'] = 'pt_BR.UTF-8'
os.environ['LC_ALL'] = 'pt_BR.UTF-8'
os.environ['LANGUAGE'] = 'pt_BR:en_US'
