__author__ = 'Patry'


class Empleado():
    """
    Representacion de un empleado de una empresa
    """
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """
        Constructor de la clase Empleado

        Crea un nuevo empleado a partir de los parametros que recibe

        :param nombre: nombre del empleado
        :type nombre: str
        :param apellidos: apellidos del empleado
        :type apellidos: str
        :param dni: dni del empleado
        :type dni: str
        :param direccion: direccion del empleado
        :type direccion: str
        :param edad: edad del empleado
        :type edad: int
        :param email: correo electronico del empleado
        :type email: str
        :param salario: salario anual del empleado
        :type salario: int
        :return:
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """
        Salario del empleado

        Devuelve el salario anual del empleado

        :return: salario anual del empleado
        :rtype: int
        """
        return self.salario

    def get_dni(self):
        """
        Dni del empleado

        Devuelve el dni de un empleado

        :return: dni de un empleado
        :rtype: str
        """
        return self.dni

    def get_nombre_apellidos(self):
        """
        Nombre y apellidos

        Devuelve el nombre y apellidos de un empleado

        :return: nombre y apellidos
        :rtype: str
        """
        return self.nombre + " " + self.apellidos

    def get_edad(self):
        """
        Edad de un empleado

        Devuelve la edad de un empleado

        :return: edad de un empleado
        :rtype: int
        """
        return self.edad

    def get_email(self):
        """
        Email de un empleado

        Devuelve el email de un empleado

        :return: email de un empleado
        :rtype: str
        """
        return self.email

    def get_direccion(self):
        """
        Direccion de un empleado

        Devuelve la direccion de un empleado

        :return: direccion de un empleado
        :rtype: str
        """
        return self.direccion

    def get_salario_mensual(self):
        """
        Salario mensual de un empleado

        Calcula y devuleve el salario mensual de un empleado

        :return: salario mensual de un empleado
        :rtype: int
        """
        return self.get_salario()/12