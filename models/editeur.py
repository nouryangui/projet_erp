# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliothequeEditeur(models.Model):
    _name = 'bibliotheque.editeur'
    _rec_name = 'nom'
    nom = fields.Char('nom')
    pays = fields.Char('pays')
    adresse = fields.Char('adresse')
    telephone=fields.Integer('telephone')
    livre_id = fields.One2many(comodel_name='bibliotheque.livre', inverse_name='editeur_id')
    num_livre = fields.Integer("nombre des livres", compute="comp_livre")
    def comp_livre(self):
        self.num_livre = len(self.livre_id)



