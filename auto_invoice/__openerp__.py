# -*- coding: utf-8 -*-

{
    'name': 'Auto Invioce',
    'version': '1.0',
    'category': 'sale',
    'description': u"""
    add an option in order_policy,with it you will creat invoice automatically!
    """,
    'author': 'ShineIT<contact@openerp.cn>',
    'website': 'http://www.openerp.cn/',
    'depends': ['sale_stock',],
    'data': [
        'sale_workflow.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
