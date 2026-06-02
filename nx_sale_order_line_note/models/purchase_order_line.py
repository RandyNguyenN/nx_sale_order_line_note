from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    internal_note = fields.Text(
        string='Internal Note',
        help='Internal note for this line — never printed on supplier-facing PDF reports.',
    )
