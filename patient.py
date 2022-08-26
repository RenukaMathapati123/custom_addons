from odoo import fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "hospital patient"

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    appointment_lines = fields.One2many('patient.appointment.lines', 'appointment_id', string='Appointment Lines')


class PatientAppointmentLines(models.Model):
    _name = "patient.appointment.lines"
    _description = "patient appointment lines"


    no_of_patients= fields.Integer(string='No_of_Patients')
    appointment_id = fields.Many2one('hospital.patient', string='Appointment Id')
