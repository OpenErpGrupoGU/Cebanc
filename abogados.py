
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

class equipos_mg(osv.osv):

    _name = 'equipos.mg'
    _description = 'equipos.mg'
    _rec_name='nombre'
    _columns = {
            'nombre':fields.char('Modelo', size = 20, required = True, readonly = False),
            'pvp':fields.float('PVP sin IVA', digits = (6,2), required = True, readonly = False),
            'cpu':fields.char('Procesador', size = 40, required = True, readonly = False),
            'ram':fields.selection([
                ('0.5','512 MB'),
                ('1','1 GB'),
                ('2','2 GB'),
                ('4','4 GB'),
                ('6','6 GB'),
                ('8','8 GB'),
                 ],'Memoria RAM', select = False, readonly = False),
            'so':fields.selection([
                ('W7','Windows 7'),
                ('W8','Windows 8'),
                ('W7/8','Windows 7/8'),
                ('A4','Android 4'),
                ('A5','Android 5'),
                 ],'Sistema Operativo', select = False),
            'hd':fields.selection([
                ('8','8 GB'),
                ('16','16 GB'),
                ('32','32 GB'),
                ('64','64 GB'),
                ('64','64 GB SSD'),
                ('128','128 GB'),
                ('500','500 GB'),
                ('1000','1000 GB'),
                 ],'Disco Duro', select = False, readonly = False),
            'wc':fields.boolean('webcam'),
            'tipo':fields.selection([
                ('1','Portatil'),
                ('2','Ultrabook'),
                ('3','Tablet'),
                 ],'Tipo Dispositivo', select = False, readonly = False),
            'venta':fields.many2many('ventas.mg', 'ven_equ', 'id_equipo', 'id_venta', 'Venta'),
            
        }
equipos_mg()