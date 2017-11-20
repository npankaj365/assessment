# -*- coding: utf-8 -*-
{
    'name': "Assessment",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Pankaj Niroula",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assessment_menu.xml',
        'views/test_creations_view.xml',
        'views/domain_view.xml',
        'views/subdomain_view.xml',
        'views/lesson_view.xml',
        'views/objective_view.xml',
        'views/question_view.xml',
        # 'views/answer_view.xml',
        'views/templates.xml',
        'reports/reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}