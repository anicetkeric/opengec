# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2017-TODAY
#    Author: Aek@(anicetkeric@gmail.com)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from datetime import datetime,date, timedelta
from odoo import models, fields
from odoo.exceptions import Warning


class Couriers(models.Model):
    _name='courier.couriers'
    _description='courier documents'
	

    name = fields.Char(string='Courier Number', required=True)
    subject = fields.Text(string='Subject', copy=False)
    is_confidential=fields.Boolean('Confidential', default=False)
    priority=fields.Selection([('h','Highest'),('hi','Hight'),('m','Medium'),('l','Lowest'),('l','Low')],'Priority', required=True)   
    courier_type = fields.Many2one('courier.type', string='Type', required=True)
    category=fields.Selection([('a','Arrival'),('l','Leaving'),('i','Internal'),('d','DMS documents')],'Category', required=True) 
    courier_nature = fields.Many2one('courier.nature', string='Nature', required=True)
    createdon_date = fields.Date(string='Created On', default=fields.datetime.now(), Required=True)
    arrival_date = fields.Date(string='Arrival On', default=fields.datetime.now())


   
   
    
class CouriersResources(models.Model):
    _name='courier.resources'
    _description='courier resources'
	

    employee_ref = fields.Many2one('hr.employee')
    partner_ref = fields.Many2one('res.partner')
    type=fields.Integer('type', default=1)
    courier_ref=fields.Many2one('courier.couriers')
   

