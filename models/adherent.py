# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliothequeAdherent(models.Model):
    _name = 'bibliotheque.adherent'
    _rec_name = 'combination'
    _inherit = 'mail.thread'
    cin = fields.Integer('cin')
    nom=fields.Char('nom')
    prenom=fields.Char('prenom')
    emprunt_id = fields.One2many(comodel_name='bibliotheque.emprunt', inverse_name='adherent_id')
    combination = fields.Char(string='Combination', compute='_compute_fields_combination')
    num_emprunt = fields.Integer("nombre des livres  emprunts", compute="comp_emprunt")

    def _compute_fields_combination(self):
        for test in self:
            test.combination = test.nom + ' ' + test.prenom


    def comp_emprunt(self):
        self.num_emprunt  = len(self.emprunt_id)






