# -*- coding: utf-8 -*-
{
    'name': "Project-Extend",

    'summary': """
        Extend to Project-Base""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project-base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv'
        'views/views.xml',
        'views/templates.xml',
        'views/project_extend.xml',
        'views/task_extend.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}