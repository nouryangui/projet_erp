# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliothequeAuteur(models.Model):
    _name = 'bibliotheque.auteur'
    _rec_name = 'nom'
    nom = fields.Char('nom')
    prenom = fields.Char('prenom')
    biographie = fields.Char('bigraphie')
    livre_ids = fields.Many2many(comodel_name='bibliotheque.livre',
                                     relation='livre_auteur_rel',
                                     column1='nom',
                                     column2='titre', inverse_name="auteur_id")
    num_livre = fields.Integer("numbers of livres", compute="comp_livre")

    def comp_livre(self):
        self.num_livre = len(self.livre_ids)
