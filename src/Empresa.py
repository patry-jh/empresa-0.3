__author__ = 'Patry'


class Empresa():
    """
    Representacion de una empresa
    """
    def __init__(self, nombre_empresa, cif, razon_social):
        """
        Constructor de la clase Departamento

        Crea un nuevo departamento a partir de los parametros que recibe

        :param nombre_empresa: nombre de la empresa
        :type nombre_empresa: str
        :param cif: cif de la empresa
        :type cif: str
        :param razon_social: razon social de la empresa
        :type razon_social: str
        """
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.departamentos=[]