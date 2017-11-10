# -*- coding: utf-8 -*-

from odoo import models, fields, api

class domain_asmt(models.Model):
    _name = 'assessment.domain_asmt'

    name = fields.Char()
    description = fields.Text()
    enabled = fields.Boolean()

class subdomain_asmt(models.Model):
    _name = 'assessment.subdomain_asmt'

    name = fields.Char()
    description = fields.Text()
    enabled = fields.Boolean()

    domain = fields.Many2one('assessment.domain_asmt', 'Domain')


class lesson_asmt(models.Model):
    _name = 'assessment.lesson_asmt'

    name = fields.Char()
    description = fields.Text()
    enabled = fields.Boolean()

    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain')
    domain = fields.Many2one('assessment.domain_asmt', 'Domain')

class objective_asmt(models.Model):
    _name = 'assessment.objective_asmt'

    name = fields.Char()
    description = fields.Text()
    enabled = fields.Boolean()

    lesson = fields.Many2one('assessment.lesson_asmt', 'Lesson')
    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain')
    domain = fields.Many2one('assessment.domain_asmt', 'Domain')

class question_asmt(models.Model):
    _name = 'assessment.question_asmt'

    statement = fields.Char()
    explanation = fields.Text()
    question_type = fields.Selection(
        [
            ('Multiple Choice Single Answer', 1),
            ('Multiple Choice Multiple Answer', 2),
        ]
    )
    question_difficulty = fields.Selection(
        [
            ('Easy', 1),
            ('Medium', 2),
            ('Difficult', 3),
        ]
    )
    enabled = fields.Boolean()
    time_required = fields.Integer()
    objective = fields.Many2one('assessment.objective_asmt', 'Objective')
    lesson = fields.Many2one('assessment.lesson_asmt', 'Lesson')
    subdomain = fields.Many2one('assessment.subdomain_asmt', 'Subdomain')
    domain = fields.Many2one('assessment.domain_asmt', 'Domain')

class answer_asmt(models.Model):
    _name = 'assessment.answer_asmt'

    description = fields.Text()
    explanation = fields.Text()
    is_right = fields.Boolean()
    question = fields.Many2one('assessment.question_asmt', 'Question')

