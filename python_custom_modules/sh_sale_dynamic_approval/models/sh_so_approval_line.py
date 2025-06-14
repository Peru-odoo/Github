# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import models,fields,api,_,Command #type:ignore

class ShSoApprovalLine(models.Model):
    _name = "sh.so.approval.line"

    name = fields.Char("")

    sh_so_id = fields.Many2one("sale.order")

    sh_approval_level = fields.Integer("Approval", store=True)

    sh_user_record_count = fields.Integer("Users")

    sh_group_record_count = fields.Integer("Groups")

    sh_status = fields.Boolean("Status")

    sh_approved_date = fields.Datetime("Approved Date")

    sh_approved_by = fields.Many2one("res.users", string="Approved By")

