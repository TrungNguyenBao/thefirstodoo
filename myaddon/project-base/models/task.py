# -*- coding: utf-8 -*-


from odoo import models, fields


class Task(models.Model):
    _name = "exam.task"

    name = fields.Char('Tên task')
    user_id = fields.Many2one(comodel_name="res.users", string="Người quản lý", )
    start_date = fields.Date(string="Ngày bắt đầu", required=False, )
    due_date = fields.Date(string="Ngày kêt thức", required=False, )
    project_id = fields.Many2one(comodel_name="exam.project", string="ID dự án")


