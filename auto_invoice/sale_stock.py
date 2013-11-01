# -*- coding: utf-8 -*-

from osv import fields, osv


class sale_order(osv.osv):
    _inherit = "sale.order"

    _columns = {
         
             'order_policy': fields.selection([
                  ('manual', 'On Demand'),
                  ('picking', 'On Delivery Order'),
                  ('prepaid', 'Before Delivery'),
                  ('autoinv', 'Auto Invoice'),
            ], 'Create Invoice', required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
            help="""Auto Invoice: A draft invoice can be created from the sales order when you confirm the order. \nOn demand: A draft invoice can be created from the sales order when needed. \nOn delivery order: A draft invoice can be created from the delivery order when the products have been delivered. \nBefore delivery: A draft invoice is created from the sales order and must be paid before the products can be delivered."""),    
    }

    _defaults = {
    
             'order_policy': 'autoinv',
         }
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
