from stdnum.at import uid

from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError


class BibliothequeEmprunt(models.Model):
    _name = 'bibliotheque.emprunt'
    date_debut = fields.Date('Date Emprunt')
    date_fin = fields.Date('Date Retour')
    livre_id = fields.Many2one(comodel_name='bibliotheque.livre')
    adherent_id = fields.Many2one(comodel_name='bibliotheque.adherent')

    # @api.model
    # def create(self, vals):
    #     new = super().create(vals)
    #     user_id = uid
    #     date_deadline = self.date_fin
    #
    #     data = {
    #         'res_id': new.id,
    #         'res_model_id': self.env['ir.model'].search([('model', '=', 'hr.applicant')]).id,
    #         # 'user_id': user_id.id,
    #         'summary': 'foo bar',
    #         'activity_type_id': self.env.ref('custom.activity_applicant').id,
    #         'date_deadline': date_deadline
    #     }
    #     self.env['mail.activity'].create(data)
    #     return new




    def name_get(self):
        result = []
        for emprunt in self:
            name = '[' + emprunt.livre_id.titre + ']' + emprunt.adherent_id.nom + ' ' + emprunt.adherent_id.prenom
            result.append((emprunt.id, name))
        return result
    @api.one
    @api.constrains('adherent_id','livre_id','date_debut', 'date_fin')
    def checknbLivreEmprunté(self):
        if self.date_fin < self.date_debut:
            raise ValueError('date début emprunt doit etre inférieur à la fin de l''emprunt')
        elif self.livre_id.nbExamplaire <= 1:
            raise ValueError("Nb d'examplaire insuffisant ")
        elif self.adherent_id.num_emprunt>3:
            raise ValueError("Nb livre emprunté egale 3")







