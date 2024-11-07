from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(
        selection=[
            ('draft', "Devis"),
            ('sent', "Envoyé"),
            ('sale', "Bon de commande"),
            ('cancel', "Annulé"),
            ('fence', "Clôturer"),
        ],
        string="Status",
        readonly=True, copy=False, index=True,
        tracking=3,
        default='draft')

    def action_progress(self):
        self.write({'state': 'fence'})
