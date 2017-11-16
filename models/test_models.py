# -*- coding: utf-8 -*-
from odoo import models, fields, api

class test_creation_asmt(models.Model):
    _name = 'assessment.test_creation_asmt'

    name = fields.Char()
    description = fields.Text()
    date = fields.Date()
    test_duration = fields.Integer()
    question_type = fields.Selection(
        [
            ('mcsa','Multiple Choice Single Answer'),
            ('mcma','Multiple Choice Multiple Answer'),
            ('o','Order'),
            ('fa','Free Answer')
        ], required=True
    )
    domain = fields.Many2one('assessment.domain_asmt', 'Domain')
    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain', domain="[('domain','=',domain)]")
    lesson = fields.Many2one('assessment.lesson_asmt', 'Lesson', domain="[('subdomain','=',subdomain)]")
    
     

class test_paper_asmt(models.Model):
    _name = 'assessment.test_paper_asmt'

    test_creation = fields.Many2one('assessment.test_creation_asmt')

class rubrics_asmt(models.Model):
    _name = 'assessment.rubric_asmt'

    grade_a = fields.Char()
    grade_b = fields.Char()
    grade_c = fields.Char()
    grade_d = fields.Char()
    grade_e = fields.Char()
    
    domain = fields.Many2one('assessment.domain_asmt', 'Domain')
    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain', domain="[('domain','=',domain)]")
    lesson = fields.Many2one('assessment.lesson_asmt', 'Lesson', domain="[('subdomain','=',subdomain)]")
    objective = fields.Many2one('assessment.objective_asmt', 'Objective', domain="[('lesson','=',lesson)]")
    