"""clase persona"""
from loger_base import log
class Persona:
    #en el casod e log se le debe asignar un valor por defecto para evitar errores
    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        
        
    
    def __str__(self):
        return f"""id: {self._id_persona}, nombre: {self._nombre}, 
                    apellido: {self._apellido},  email: {self._email}
                """
    
    
    
    
    
    @property
    def id_persona(self):
        return self._id_persona
    @id_persona.setter
    def id_persona(self,id_persona):
        self._id_persona = id_persona
        
        
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,apellido):
        self._apellido =apellido
    
    
        
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,email):
        self._email = email
        
    
    
    
    
if __name__ == "__main__":
    persona1 = Persona(12,"martin","hermer","hermer@gmail")
    log.debug(persona1)
    #insert
    #para directamente omitir el valor del parametro persona se le debe espesificar el atributo a cada uno
    persona2 = Persona(nombre="martin",apellido="hermer",email="hermer@gmail")
    log.debug(persona2)
    
   
