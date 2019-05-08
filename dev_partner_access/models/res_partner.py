# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################
from odoo import models, fields, api, _
class res_partner(models.Model):
    _inherit = 'res.partner'
    
    user_ids = fields.Many2many('res.users',string='Allow Sales Person')
    
    
    @api.model
    def default_get(self, fields_list):
        res = super(res_partner, self).default_get(fields_list)                
        res.update({
            'user_ids': [(6,0,[self.env.user.id])]
            })       
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
