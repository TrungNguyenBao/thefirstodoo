# -*- coding: utf-8 -*-


from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = "exam.wizard.tag"
    task_id = fields.Many2one(comodel_name="exam.task", string="Task")
    tags = fields.Char("Tags")
    update_option = fields.Selection(string="", selection=[('add', 'Add'),
                                                           ('replace', 'Replace'),
                                                           ('delete', 'Delete'), ], default="delete")

    def btn_update(self):
        list_tag = self.tags.split(',')
        rc_tag = self.env['exam.tag']
        list_name = []
        list_id = []
        for rc in rc_tag.search([]):
            list_name.append(rc.name)
        for tag in list_tag:
            if tag not in list_name:
                rc_tag.create({"name": tag})
        data_tag = rc_tag.search([('name', 'in', list_tag)])
        for _id in data_tag:
            list_id.append(_id.id)

        if self.update_option == "add":
            for db in data_tag:
                self.task_id.write({
                    "tag_ids": [([4, db.id])]
                })
        if self.update_option == "replace":
                self.task_id.write({
                    "tag_ids": [([6, 0, list_id])]
                })
        if self.update_option == "delete":
            for db in data_tag:
                self.task_id.write({
                    "tag_ids": [([3, db.id])]
                })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'exam.task',
            'view_mode': 'tree,form,kanban',
            'name': 'task view'
        }

