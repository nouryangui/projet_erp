from typing import Any

from stdnum.at import uid

from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError, _logger

class BibliothequeEmprunt(models.Model):
    _name = 'bibliotheque.emprunt'
    date_debut = fields.Date('Date Emprunt')
    date_fin = fields.Date('Date Retour')
    today = fields.Date.today()
    # print(type(date_fin))
    # print(today)
    # print(type(today))
    livre_id = fields.Many2one(comodel_name='bibliotheque.livre')
    adherent_id = fields.Many2one(comodel_name='bibliotheque.adherent')
    state = fields.Selection(
        [
        ('lancee','Livre emprunté'),
        ('fini','Livre retourné'),
        ('expiree','Expiré'),
        ],
        string='Status', readonly=True,default='lancee')

    def action_done(self):
        for rec in self:
            rec.state = 'fini'

    @api.onchange('today')
    def change_state_to_expired(self):
        if self.today > self.date_fin:
            self.state = 'expiree'
        else:
            print("the emprunt is still valid")




   # def _create(self, data_list):
   #      for data in data_list:
   #          print(data)
   #          for x in data :
   #              if(x=="stored"):
   #                  print("clé" + x)
   #                  print(data[x])
   #                  for element in data[x]:
   #                      if element=="livre_id":
   #                         # self.livre_id=data[x][element]
   #                          print(self.livre_id.nbExamplaire)

        #return super()._create(data_list)

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
    @api.constrains('adherent_id', 'livre_id', 'date_debut', 'date_fin')
    def checknbLivreEmprunté(self):
        if self.date_fin < self.date_debut:
            raise ValueError('date début emprunt doit etre inférieur à la fin de l''emprunt')
        elif self.livre_id.nbExamplaire <= 1:
            raise ValueError("Nb d'examplaire insuffisant ")
        elif self.adherent_id.num_emprunt > 3:
            raise ValueError("Nb livre emprunté egale 3")
