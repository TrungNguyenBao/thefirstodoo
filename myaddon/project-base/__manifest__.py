# -*- coding: utf-8 -*-
{
    'name': "Project-Base",

    'summary': """
        Project Test""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Hole in One",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/project.xml',
        'views/task.xml',
        'views/tag.xml',
        'wizard/wizard.xml',
        'views/menu.xml',
        'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}