# -*- coding: utf-8 -*-
from odoo import models, fields


class DymCity(models.Model):
    _name = 'dym.city'

    id = fields.Integer("ID")
    create_uid = fields.Many2one('res.users', 'Created by', index=True, readonly=True)
    code = fields.Char("Kode City", size=128)
    create_date = fields.Datetime('Created on', index=True, readonly=True)
    name = fields.Char("Name", size=128)
    write_uid = fields.Many2one('res.users', 'Last Updated by', index=True, readonly=True)
    write_date = fields.Datetime('Last Updated on', index=True, readonly=True)
    state_id = fields.Char("ID State")