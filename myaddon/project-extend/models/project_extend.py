# -*- coding: utf-8 -*-

import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

from odoo import models, fields, api


class Project_Extend(models.Model):
    # _name = "exam.project"
    _inherit = 'exam.project'

    status = fields.Selection(string="Trạng thái", selection=[('init', 'Init'), ('finish', 'Finish'), ('fail', 'Fail')], )

    working_status = fields.Selection(string="Working status", compute='set_date',
                selection=[('chuabatdau', 'Chưa bắt đầu'), ('batdau', 'Đang hoạt động'), ('dabatdau','Đã kết thúc') ], required=False)

    @api.depends('start_date','due_date')
    def set_date(self):
        for d in self:
            if d.due_date and d.start_date:
                date_now = datetime.datetime.now()
                start_date = datetime.datetime.strptime(d.start_date, DEFAULT_SERVER_DATE_FORMAT)
                due_date = datetime.datetime.strptime(d.due_date, DEFAULT_SERVER_DATE_FORMAT)
                if date_now < start_date:
                    d.working_status ='chuabatdau'
                elif start_date < date_now < due_date:
                    d.working_status = 'batdau'
                else:
                    d.working_status ='dabatdau'


