# -*- coding: utf-8 -*-
"""
    Contains Code for Agile part of Project Module

    Implements allowing Agile Development through Projects

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""

from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval
from trytond.pool import Pool

__all__=['Agile']

class Agile(ModelSQL, ModelView):
    'Agile'
    __name__ = 'project.work'
    type = fields.Selection([
            ('project','Project'),
            ('task','Task'),
            ('story','Story')
        ],'Type', required=True, select=True)
    parent = fields.Many2One('project.work','Parent',
        domain=[('type','=','project')])
