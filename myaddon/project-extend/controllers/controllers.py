# -*- coding: utf-8 -*-
from odoo import http

# class Project-extend(http.Controller):
#     @http.route('/project-extend/project-extend/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project-extend/project-extend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project-extend.listing', {
#             'root': '/project-extend/project-extend',
#             'objects': http.request.env['project-extend.project-extend'].search([]),
#         })

#     @http.route('/project-extend/project-extend/objects/<model("project-extend.project-extend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project-extend.object', {
#             'object': obj
#         })