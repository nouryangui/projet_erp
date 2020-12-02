# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BibliothequeLivre(models.Model):
    _name = 'bibliotheque.livre'
    titre = fields.Char('Titre')
    nbPages = fields.Integer('Nombre de pages')
    dateEdition = fields.Date('Date Edition')
    nbExamplaire = fields.Integer('Nombre Examplaire')
    isbn = fields.Integer('isbn')
    prix = fields.Integer('prix')
