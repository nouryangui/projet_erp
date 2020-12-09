from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError


class BibliothequeEmprunt(models.Model):
    _name = 'bibliotheque.emprunt'
    date_debut = fields.Date('Date Emprunte')
    date_fin = fields.Date('Date Retour')
    livre_id = fields.Many2one(comodel_name='bibliotheque.livre')
    adherent_id = fields.Many2one(comodel_name='bibliotheque.adherent')

    def name_get(self):
        result = []
        for emprunt in self:
            name = '[' + emprunt.livre_id.titre + ']' + emprunt.adherent_id.nom + ' ' + emprunt.adherent_id.prenom
            result.append((emprunt.id, name))
        return result
    @api.one
    @api.constrains('adherent_id')
    def checknbLivreEmprunté(self):
        if self.adherent_id.num_emprunt>3:
            raise UserError("Nb livre emprunté egale 3")

    @api.one
    @api.constrains('livre_id')
    def checknbLivreEmprunté(self):
        if self.livre_id.nbExamplaire <= 1:
            raise UserError("Nb d'examplaire insuffisant ")

    @api.one
    @api.constrains('date_debut', 'date_fin')
    def checkDateEmprunt(self):
        if self.date_fin < self.date_debut:
            raise ValueError('date début emprunt doit etre inférieur à la fin de l''emprunt')




