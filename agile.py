# -*- coding: utf-8 -*-
"""
Contains Code for Agile part of Project Module

Implements allowing Agile Development through Projects

:copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
:license: BSD, see LICENSE for more details.
"""

from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval


__all__ = ['Agile']


class Agile(ModelSQL, ModelView):
    'Agile'
    __name__ = 'project.work'
    type = fields.Selection([
        ('project', 'Project'),
        ('task', 'Task'),
        ('story', 'Story')],
        'Type', required=True, select=True
    )

    parent = fields.Many2One(
        'project.work', 'Parent', domain=[('type', '=', 'project')]
    )

    category = fields.Selection([
        ('task', 'General Task'),
        ('bug', 'Defect/Bug'),
        ('test', 'Test')], 'Category',
        states={'invisible': Eval('type') != 'task'}, depends=['type'])

    children_story = fields.One2Many(
        'project.work', 'parent', 'Children',
        domain=[('type', '=', 'task')]
    )
