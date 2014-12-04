__author__ = 'Patry'
from Empleado import *


class Departamento():
    """
    Representacion de un departamento de una empresa
    """
    def __init__(self, nombre_depto, id_depto):
        """
        Constructor de la clase Departamento

        Crea un nuevo departamento a partir de los parametros que recibe

        :param nombre_depto: nombre del departamento
        :type nombre_depto: str
        :param id_depto: id del departamento
        :type id_depto: str
        """
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.empleados = []

    def aniadir_empleado(self,empleado):
        """
        Aniadir un empleado

        Aniade un empleado a la lista de empleados

        """
        self.empleados.append(empleado)

    def get_salario_total(self):
        """
        Salario total

        Devuelve el salario total anual de todos los empleados del departamento

        :return: salario anual de los empleados
        :rtype: int
        """
        total = 0
        for emp in self.empleados:
            total += emp.get_salario()
        return total

    def get_nombre_depto(self):
        """
        Nombre del departamento

        Devuelve el nombre del departamento

        :return: nombre departamento
        :rtype: str
        """
        return self.nombre_depto

    def get_salario_total_mensual(self):
        """
        Salario total

        Devuelve el salario total mensual de todos los empleados del departamento

        :return: salario anual de los empleados
        :rtype: int
        """
        total = 0
        for emp in self.empleados:
            total += emp.get_salario_mensual()
        return total/len(self.empleados)