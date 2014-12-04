__author__ = 'Patry'
from unittest import TestCase
from src.Departamento import *
from src.Empleado import *
from mockito import *


class TestDepartamento(TestCase):
    """
    Clase test de un departamento de una empresa
    """
    def test_get_salario_total(self):
        """
        Test salario total

        Simula 3 empleados de un departamento con 3 salarios anuales distintos y comprueba que el total se corresponde con su suma

        :return:
        """
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)
        when(emp1).get_salario().thenReturn(12000)
        when(emp2).get_salario().thenReturn(24000)
        when(emp3).get_salario().thenReturn(18000)
        depart1 = Departamento('Informatica', 1234)
        depart1.aniadir_empleado(emp1)
        depart1.aniadir_empleado(emp2)
        depart1.aniadir_empleado(emp3)
        self.assertEqual(depart1.get_salario_total(), 54000)

    def test_get_salario_total_mensual(self):
        """
        Test salario total mensual

        Simula 3 empleados de un departamento con 3 salarios mensuales distintos y comprueba que el total se corresponde con su suma

        :return:
        """
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)
        when(emp1).get_salario_mensual().thenReturn(1000)
        when(emp2).get_salario_mensual().thenReturn(2000)
        when(emp3).get_salario_mensual().thenReturn(1500)
        depart1 = Departamento('Informatica', 1234)
        depart1.aniadir_empleado(emp1)
        depart1.aniadir_empleado(emp2)
        depart1.aniadir_empleado(emp3)
        self.assertEqual(depart1.get_salario_total_mensual(), 1500)