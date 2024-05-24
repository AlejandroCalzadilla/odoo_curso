# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from odoo.exceptions import ValidationError
from odoo  import _

# class Project(models.Model):
#       _name = 'manage.project'  #namemodulo.namemodulo 
#       _description = 'manage.project'
#       name = fields.Char()
#       description = fields.Text()
#       histories = fields.One2many(comodel_name="manage.history",inverse_name="project")

# class history(models.Model):
#       _name = 'manage.history'  #namemodulo.namemodulo 
#       _description = 'manage.history'
#       name = fields.Char()
#       description = fields.Text()
#       project = fields.Many2one('manage.project',ondelete="set null")
#       tasks= fields.One2many(string="Tareas",comodel_name="manage.task",inverse_name="history")

class task(models.Model):
     _name = 'manage.task'  #namemodulo.namemodulo 
     _description = 'manage.manage'

     #campos o atributos 
     # si no se especifica el nombre del atributo tomara el que se pone
     #name = fields.Char()  # nombre de la tarea 
#    #de solo lectura y que sea obligatorio nonull  
     # history = fields.Many2one("manage.history",ondelete="set null",required=True,help="introdusca un nombre")
     code=fields.Char(compute="_get_code")
     name = fields.Char(string="Nombre",readonly=False,required=True,help="introdusca el nombre")
     description = fields.Text()
     start_date = fields.Datetime()
     end_date = fields.Datetime()
     ispaused = fields.Boolean() 
     sprint = fields.Many2one("manage.sprint",ondelete="set null",help="Sprint relacionado")   #llave foranea de uno a muchos
     #sprint = fields.Many2one("manage.sprint")
     technologies=fields.Many2many(comodel_name="manage.technology",
                                   realation="technologies_tasks",
                                   column1="task_id",
                                   column2="tecnology_id"
                                  )

      
     def _get_code(self):
         for task in self:
            try: 
                if len(task.sprint) == 0:
                 #task.code="TSK_"+str(task.id)
                  task.code="TSK_"+str(task.id)
                else:
                  task.code = str(task.sprint.name).upper()+"_"+str(task.id)      
            except:
               raise  ValidationError(_("Generacion de codigo erronea")) 
  
    # @api.multi
    # def action_save_and_redirect(self):
        # Lógica para guardar los datos aquí
        # ...
    #    return {
     #        'type': 'ir.actions.act_window',
     #        'name': 'manage.task_list',
     #        'res_model': 'manage.task',
     #        'view_mode': 'form',
     #        'view_type': 'form',
     #        'res_id': self.id,
     #        'target': 'current',
     #    }
     def pruebabuttom():
          raise  ValidationError(_("Generacion de codigo erronea")) 
     

class sprint(models.Model):
     _name = 'manage.sprint'  #namemodulo.namemodulo 
     _description = 'manage.sprint'
      
     #campos o atributos 
     # si no se especifica el nombre del atributo tomara el que se pone
     #name = fields.Char()  # nombre de la tarea 
#    #de solo lectura y que sea obligatorio nonull  
     name = fields.Char()
     description = fields.Text()
     # project =fields.Many2one("manage.project")
     duration= fields.Integer()
     start_date = fields.Datetime()
     end_date = fields.Datetime(compute="_get_end_date",store=True)#store guarda en base de datos
     ispaused = fields.Boolean()
     #tasks=fields.One2many("manage.task",'sprint') # se le pasa  el nombre que se le puso a la otra tabla 
     tasks=fields.One2many(string="Tareas ale", comodel_name="manage.task",inverse_name='sprint') # para ponerle nombre de etiqueta en este caso tareas ale
  
     @api.depends('start_date','duration') #si alguno cambia la fecha cambia
     def _get_end_date(self):
          for sprint in self:
               if  isinstance(sprint.start_date,datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration) 
               else: 
                  sprint.end_date =sprint.start_date
      



class technology(models.Model):
     _name = 'manage.technology'  #namemodulo.namemodulo 
     _description = 'manage.technology'
     

     name = fields.Char()
     description = fields.Text()
     photo=fields.Image(max_width=200,max_heigth=200)
     tasks=fields.Many2many(comodel_name="manage.task",
                            realation="technologies_tasks",
                            column1="tecnology_id",  
                            column2="task_id"
                            
                           )  


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

