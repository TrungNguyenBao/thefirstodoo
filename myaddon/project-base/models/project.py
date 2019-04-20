# -*- coding: utf-8 -*-


from odoo import models, fields


class Project(models.Model):
    _name = "exam.project"
    name = fields.Char('Tên project')
    manager_user_id = fields.Integer(string="ID người quản lý", )
    start_date = fields.Date(string="Ngày bắt đầu", required=False, )
    due_date = fields.Date(string="Ngày hết hạn", required=False, )
    task_id = fields.One2many(comodel_name="exam.task", inverse_name="project_id", string="Danh sách task dự án")






