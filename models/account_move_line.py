from odoo import fields, models, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    height = fields.Float(
        string = "Height (m)"
        )
    width = fields.Float(
        string = "width (m)"
        )
    m2 = fields.Float(
        string ="m2", 
        compute = '_compute_m2',
        store=True
        )
    net_total = fields.Monetary(
        string='Net Total',
        compute='_compute_net_total',
        store=True
        )

    @api.depends('height','width')
    def _compute_m2(self):
        for line in self:
                if line.height and line.width:
                    line.m2 = line.height * line.width
                else:
                      line.m2=0
                      
    @api.depends('m2','quantity','price_unit')
    def _compute_net_total(self):
            for line in self:
                  line.net_total = line.m2*line.quantity*line.price_unit

    @api.onchange('m2','quantity','price_unit')
    def _onchange_calculate_total(self):
          self.price_subtotal = self.net_total