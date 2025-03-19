from odoo import models, fields,api

class CollegeWizard(models.TransientModel):
    _name = 'college.wizard'
    

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
   

    
    def action_confirm(self):
        student_ids = self.env.context.get('active_ids', [])
        if student_ids:
            students = self.env['college.student'].browse(student_ids)
            students.write({'age': self.age}) 
        return {'type': 'ir.actions.act_window_close'}
    

    
   

