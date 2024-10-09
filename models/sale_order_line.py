from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    height = fields.Float(
        string = "Height (m)"
        )
    width = fields.Float(
        string = "width (m)"
        )
    m2 = fields.Float(
        string ="M^2", 
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
                line.m2 = line.height*line.width
            else:
                line.net_total = 0
                
    @api.depends('m2,product_uom_qty','price_unit')
    def _compute_net_total(self):
        for line in self:
            if line.m2 and line.product_uom_qty and line.price.unit:
                line.net_total = line.m2*line.product_uom_qty*line.price_unit
            else:
                line.net_total = 0

    @api.onchange('m2','product_uom_qty','price_unit')
    def _onchange_calculate_total(self):
        if self.m2 and self.product_uom_qty and self.price_unit:
            self.price_subtotal = self.net_total
        else:
            self.price_subtotal = 0
            