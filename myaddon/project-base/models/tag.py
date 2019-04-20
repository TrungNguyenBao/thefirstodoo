# -*- coding: utf-8 -*-


from odoo import models, fields


class Tag(models.Model):
    _name = "exam.tag"

    name = fields.Char('Tên tag')

