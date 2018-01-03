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
from odoo import models, fields

class CourierType(models.Model):
    _name='courier.type'
    _description='Courier Type'
    
    name=fields.Char('Name' , Required=True)    


class CourierNature(models.Model):
    _name='courier.nature'
    _description='Courier Nature'
    
    name=fields.Char('Name' , Required=True)  