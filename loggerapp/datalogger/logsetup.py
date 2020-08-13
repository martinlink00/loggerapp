#!/usr/bin/env python
# -*- mode: Python; coding: utf-8 -*-

# Copyright © 2016 Christian Gross

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This module handles the logging setup.

"""

import logging
import logging.config
import os.path as osp

LOGFILE = 'datalogger.log'

# using dictconfig to set up logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'format': '%(levelname)-4.4s %(asctime)s %(module)-10.10s %(funcName)-10.10s %(lineno)-4d proc:%(process)-4d thr:%(threadName).10s || %(message)s'
        },
        'detailed': {
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'format': '%(levelname)-4.4s %(asctime)s %(module)-10.10s %(funcName)-10.10s %(lineno)-4d ||  %(message)s'
        },
        'simple': {
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'format': '%(levelname)-4.4s || %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': LOGFILE,
            'mode': 'a',
            'maxBytes': 10000000,
            'backupCount': 1,
        }
    },
    'loggers': {
        'beamproflogger': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        }
    }
}

# configure logging
logging.config.dictConfig(LOGGING)

# instantiate a logger to be used in the application
log = logging.getLogger('beamproflogger')


def main():
    log = logging.getLogger('beamproflogger')
    log.debug('A test debug message')
    log.info('A test info message')
    log.warn('A test warning message')
    log.error('A test error message')
    log.critical('A test critical message')

if __name__ == '__main__':
    main()
