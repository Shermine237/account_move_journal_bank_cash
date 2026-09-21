# -*- coding: utf-8 -*-
from odoo import api, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _get_valid_journal_types(self):
        """Allow bank and cash journals on manual journal entries.

        Standard Odoo only allows type 'general' (Miscellaneous Operations) for
        move_type='entry'. We also accept bank and cash so a selected journal
        is not reset by _compute_journal_id.
        """
        journal_types = super()._get_valid_journal_types()
        if journal_types == ['general']:
            return ['general', 'bank', 'cash']
        return journal_types

    @api.depends('company_id', 'invoice_filter_type_domain')
    def _compute_suitable_journal_ids(self):
        """Extend the Journal dropdown on manual entries with bank and cash.

        The Journal field domain is [('id', 'in', suitable_journal_ids)].
        For invoices/bills, keep standard sale/purchase filtering.
        For journal entries (no invoice_filter_type_domain), show general,
        bank and cash journals.
        """
        super()._compute_suitable_journal_ids()
        for move in self:
            if move.invoice_filter_type_domain:
                continue
            company = move.company_id or self.env.company
            move.suitable_journal_ids = self.env['account.journal'].search([
                *self.env['account.journal']._check_company_domain(company),
                ('type', 'in', ['general', 'bank', 'cash']),
            ])
