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
    categorie_id = fields.Many2one(comodel_name='bibliotheque.categorie')
    auteur_id = fields.Many2many(comodel_name='bibliotheque.auteur', relation='livre_auteur_rel',
                                 column1='titre',
                                 column2='nom')
    emprunt_ids = fields.One2many(comodel_name='bibliotheque.emprunt', inverse_name='livre_id')
