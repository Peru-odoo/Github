# Copyright (C) Softhealer Technologies.

from odoo import models,fields,api,_ #type:ignore
from odoo.exceptions import UserError #type:ignore


class ShSplitWizardLine(models.TransientModel):
    _name = "sh.split.wizard.line"

    sh_name = fields.Text()

    sh_product_template_id = fields.Many2one("product.template", string="Product")
    sh_product_uom_qty = fields.Float(string="Quantity")

    sh_sol_lot_no_ids = fields.Many2many("stock.lot", string="Lot/Sr no.")
    # sh_sol_expiry_date = fields.Date()
    
    sh_product_product_id = fields.Many2one("product.product")
        
    sh_order_line_id = fields.Many2one("sale.order.line")

    sh_is_narcotic_bool = fields.Boolean()


    
    