# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _
"""    
class sale_order(models.Model):

    _inherit = 'sale.order'

    @api.constrains('order_line')
    def _check_order_lines_sequence(self):

        all_sequences = self.order_line.mapped('sequence')
        sequences = list(set(all_sequences))
        if len(all_sequences) != len(sequences):
            raise ValidationError(
                _('The sequence must be unique per purchase order!') + ".\n" +
                _('The next sequence numbers are already used') + ":\n" +
                str(sequences))
"""            
              
class sale_order_line(models.Model):
    _inherit = 'sale.order.line'
    _order = "sequence"
        
    sequence = fields.Integer(
        string='Pos',
        help="Gives the sequence of this line when displaying the order.")

    @api.model
    def default_get(self, fields_list):
        test = 'hallo'
        """Overwrite the default value of the sequence field taking into account
        the current number of lines in the purchase order. If is not call from
        the purchase order will use the default value.
        """
        res = super(sale_order_line, self).default_get(fields_list)
        res.update({'sequence': len(self._context.get('order_line', [])) + 1})
        return res