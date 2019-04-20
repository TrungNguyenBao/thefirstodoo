# -*- coding: utf-8 -*-
import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

from odoo import models, fields, api


class Task_Extend(models.Model):
    # _name = "exam.task.extend"
    _inherit = 'exam.task'
    _order = "priority desc"

    status = fields.Selection(string="Trạng thái",
                            selection=[('init', 'Init'), ('inprogress', 'In progress'), ('finish', 'Finish')], required=False, )

    working_status = fields.Selection(string="Working status", compute='set_date',
                                      selection=[('notstart', 'Not Start'), ('inworkingtime',
                                                'In working time'), ('finish', 'Finish'),('overdeadline','Over dead line')], required=False)
    tag_ids = fields.Many2many(comodel_name="exam.tag", string="Tag id", )
    priority = fields.Selection([('1', 'Low'), ('2', 'Normal'),('3', 'High'),('4', 'Very High')],'Priority', )

    @api.depends('start_date', 'due_date')
    def set_date(self):
        for d in self:
            if d.due_date and d.start_date:
                date_now = datetime.datetime.now()
                start_date = datetime.datetime.strptime(d.start_date, DEFAULT_SERVER_DATE_FORMAT)
                due_date = datetime.datetime.strptime(d.due_date, DEFAULT_SERVER_DATE_FORMAT)
                if d.working_status == 'finish':
                    d.working_status = 'finish'
                elif date_now < start_date:
                    d.working_status = 'notstart'
                elif start_date < date_now < due_date:
                    d.working_status = 'inworkingtime'
                else:
                    d.working_status = 'overdeadline'