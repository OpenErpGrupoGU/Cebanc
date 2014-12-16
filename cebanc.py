
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP , Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv
from osv import fields

class visitas_ab(osv.osv):

    _name = 'visitas.ab'
    _description = 'visitas.ab'
    _rec_name='codigo'
    _columns = {
            'codigo':fields.char('Código', size = 20, required = True, readonly = False),
            'fecha_hora':fields.datetime('Fecha/Hora', required = True, readonly = False),
            'estado':fields.selection([
                ('1','Programada'),
                ('2','Realizada'),
                ('3','Anulada'),
                 ],'Estado', select = False, readonly = False),
            'duracion':fields.char('Duración', size = 30, required = True, readonly = False),
            'caso':fields.many2one('casos.ab','Caso'),
            'descripcion':fields.char('Descripción', size = 40, required = True, readonly = False),
            'situacion':fields.char('Situación', size = 60, required = True, readonly = False),
        
        }
visitas_ab()
