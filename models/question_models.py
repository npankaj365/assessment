# -*- coding: utf-8 -*-

from odoo import models, fields, api

class domain_asmt(models.Model):
    _name = 'assessment.domain_asmt'

    name = fields.Char()
    description = fields.Text()
    enabled = fields.Boolean()

    subdomain = fields.One2many('assessment.subdomain_asmt', 'domain')
    

class subdomain_asmt(models.Model):
    _name = 'assessment.subdomain_asmt'

    name = fields.Char()
    description = fields.Text()
    enabled = fields.Boolean()

    lesson = fields.One2many('assessment.lesson_asmt', 'subdomain')

    domain = fields.Many2one('assessment.domain_asmt', 'Domain')


class lesson_asmt(models.Model):
    _name = 'assessment.lesson_asmt'

    name = fields.Char()
    description = fields.Text()
    enabled = fields.Boolean()

    objective = fields.One2many('assessment.objective_asmt', 'lesson')

    domain = fields.Many2one('assessment.domain_asmt', 'Domain', required=True)
    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain', domain="[('domain','=',domain)]", required=True)
    

class objective_asmt(models.Model):
    _name = 'assessment.objective_asmt'

    name = fields.Char()
    description = fields.Text()
    enabled = fields.Boolean()

    question = fields.One2many('assessment.question_asmt', 'objective')

    domain = fields.Many2one('assessment.domain_asmt', 'Domain')
    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain', domain="[('domain','=',domain)]", required=True)
    lesson = fields.Many2one('assessment.lesson_asmt', 'Lesson', domain="[('subdomain','=',subdomain)]", required=True)
    

class question_asmt(models.Model):
    _name = 'assessment.question_asmt'
    _rec_name = 'statement'

    statement = fields.Char(string="Statement", required=True)
    explanation = fields.Text(string="Description of the Question")
    question_type = fields.Selection(
        [
            ('mcsa','Multiple Choice Single Answer'),
            ('mcma','Multiple Choice Multiple Answer'),
            ('o','Order'),
            ('fa','Free Answer')
        ], required=True
    )
    question_difficulty = fields.Selection(
        [
            ('1','Easy'),
            ('2','Medium'),
            ('3','Difficult'),
        ], required=True
    )
    choice1 = fields.Char()
    choice2 = fields.Char()
    choice3 = fields.Char()
    choice4 = fields.Char()
    correct_choice = fields.Char()
    enabled = fields.Boolean()
    time_required = fields.Integer(string="Time Required", required=True)
    domain = fields.Many2one('assessment.domain_asmt', 'Domain', required=True)
    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain', required=True, domain="[('domain','=',domain)]")
    lesson = fields.Many2one('assessment.lesson_asmt', 'Lesson', required=True, domain="[('subdomain','=',subdomain)]")
    objective = fields.Many2one('assessment.objective_asmt', 'Objective', required=True, domain="[('lesson','=',lesson)]")
