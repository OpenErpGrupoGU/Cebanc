
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

class grupo_ce(osv.osv):

    _name = 'grupo.ce'
    _description = 'grupo.ce'
    _rec_name='codigo'
    _columns = {
            'codigo':fields.char('Código', size = 20, required = True, readonly = False),
            'nombre':fields.char('Nombre', size = 30, required = True, readonly = False),
            'aula':fields.char('Aula', size = 30, required = True, readonly = False),
            'tutor':fields.many2one('profesor.ce','Tutor'),
            'alumnos':fields.one2many('alumno.ce', 'grupo', 'Alumno', readonly=False),
        
        }
grupo_ce()

class profesor_ce(osv.osv):

    _name = 'profesor.ce'
    _description = 'profesor.ce'
    _rec_name='dni'
    _columns = {
            'dni':fields.char('DNI', size = 20, required = True, readonly = False),
            'nombre':fields.char('Nombre', size = 30, required = True, readonly = False),
            'apellido1':fields.char('Primer apellido', size = 30, required = True, readonly = False),
            'apellido2':fields.char('Segundo apellido', size = 30, required = True, readonly = False),
            'aula':fields.char('Aula', size = 10, required = True, readonly = False),
            'tutor_de':fields.many2one('grupo.ce','Tutor de'),
            'asignaturas':fields.one2many('asignatura.ce', 'profesor', 'Asignaturas', readonly=False),
            'entrevista_a':fields.many2many('alumno.ce', 'entrevista_al_pr', 'dni_profesor', 'dni_alumno', 'Entrevista a'),
        
        }
profesor_ce()

class asignatura_ce(osv.osv):

    _name = 'asignatura.ce'
    _description = 'asignatura.ce'
    _rec_name='codigo'
    _columns = {
            'codigo':fields.char('Código', size = 20, required = True, readonly = False),
            'nombre':fields.char('Nombre', size = 30, required = True, readonly = False),
            'profesor':fields.many2one('profesor.ce','Profesor de'),
            'alumnos':fields.many2many('alumno.ce', 'asignatura_alumnos', 'codigo_asignatura', 'dni_alumno', 'Lo atienten'),
        
        }
asignatura_ce()

class alumno_ce(osv.osv):

    _name = 'alumno.ce'
    _description = 'alumno.ce'
    _rec_name='dni'
    _columns = {
            'dni':fields.char('DNI', size = 20, required = True, readonly = False),
            'nombre':fields.char('Nombre', size = 30, required = True, readonly = False),
            'apellido1':fields.char('Primer apellido', size = 30, required = True, readonly = False),
            'apellido2':fields.char('Segundo apellido', size = 30, required = True, readonly = False),
            'fecha_nac': fields.date('Fecha de nacimiento', required = True, readonly = False),
            'grupo':fields.many2one('grupo.ce','Grupo'),
            'asignaturas':fields.many2many('asignatura.ce', 'asignatura_alumnos', 'dni_alumno', 'codigo_asignatura', 'Atiende a'),
            'entrevista_con':fields.many2many('profesor.ce', 'entrevista_al_pr', 'dni_alumno', 'dni_profesor', 'Entrevista con        '),        
        }
alumno_ce()
