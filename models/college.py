from odoo import models,fields,api
from odoo.exceptions import ValidationError


class CollegeStudent(models.Model):
    _name = "college.student"
    _description = "College Student Information"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ], string='Gender')
    student_dob = fields.Date(string="Date of Birth")
    photo = fields.Image(string='Image')
    student_blood_group = fields.Selection([
        ('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
        ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')
    ], string='Blood Group')
    contact_no = fields.Char(string='Contact')
    address = fields.Char(string='Address')
    nationality = fields.Char(string='Nationality')
    date = fields.Date(string='Date', default=fields.Date.context_today)



    
    def action_confirm(self):
       
     return {
        'type': 'ir.actions.act_window',
        'name': 'Update Age',
        'res_model': 'college.wizard',
        'target': 'new',
        'view_mode': 'form',
        'context': {
            'default_user_id': self.id,
            'default_name': self.name,
            'default_age': self.age
            
        }
    }


    _sql_constraints = [
        ('unique_contact_no', 'UNIQUE(contact_no)', 'Contact number must be unique!'),
        ('check_age', 'CHECK(age >= 18)', 'Age must be at least 18 years old!'),
    ]

    

    """ @api.constrains('contact_no')
    def _check_contact_no(self):
        for record in self:
            if not record.contact_no.isdigit() or len(record.contact_no) != 10:
                raise ValidationError("Contact number must be a 10-digit number!")

    @api.constrains('student_dob')
    def _check_dob(self):
        for record in self:
            if record.student_dob:
                today = fields.Date.today()
                birth_year = record.student_dob.year
                current_year = today.year
                calculated_age = current_year - birth_year
                if calculated_age != record.age:
                    raise ValidationError("Age must match the Date of Birth!") """

