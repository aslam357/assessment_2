from odoo import models,fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_dimension_pricing = fields.Boolean(
        string = "Enable Price Calculation Based On Dimensions",
        config_parameter = 'sales.dimension_pricing'
        )