from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    internal_note = fields.Text(
        string='Internal Note',
        help='Internal note for this line — never printed on customer-facing PDF reports.',
    )
