# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliothequeLivre(models.Model):
    _name = 'bibliotheque.livre'
    _rec_name = 'titre'
    titre = fields.Char('Titre')
    nbPages = fields.Integer('Nombre de pages')
    dateEdition = fields.Date('Date Edition')
    nbExamplaire = fields.Integer('Nombre Examplaire')
    isbn = fields.Integer('isbn')
    prix = fields.Integer('prix')
    editeur_id = fields.Many2one(comodel_name='bibliotheque.editeur')
    auteur_id = fields.Many2many(comodel_name='bibliotheque.auteur', relation='livre_auteur_rel',
                                 column1='titre',
                                 column2='nom')
    categorie_id = fields.Many2one(comodel_name='bibliotheque.categorie')
    emprunts_id = fields.One2many(comodel_name='bibliotheque.emprunt', inverse_name='livre_id')
    num_auteur = fields.Integer("nombre des auteurs du livre", compute="comp_auteur")
    def comp_auteur(self):
        self. num_auteur = len(self.auteur_id)
