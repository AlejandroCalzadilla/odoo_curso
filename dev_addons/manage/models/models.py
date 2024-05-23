# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task(models.Model):
     _name = 'manage.task'  #namemodulo.namemodulo 
     _description = 'manage.manage'

     #campos o atributos 
     # si no se especifica el nombre del atributo tomara el que se pone
     #name = fields.Char()  # nombre de la tarea 
#    #de solo lectura y que sea obligatorio nonull  
     name = fields.Char(string="Nombre",readonly=False,required=True,help="introdusca el nombre")
     description = fields.Text()
     creation_date = fields.Date()
     start_date = fields.Datetime()
     end_date = fields.Datetime()
     ispaused = fields.Boolean()



#    
# 
# 
# 
# 
#  value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

