# -*- coding: utf-8 -*-
"""
    __init__

    Initialization for Agile Module of Project Module

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""

from trytond.pool import Pool
from .agile import *

def register():
    Pool.register(
        Agile,
        module='agile', type_='model'
    )
