from django.forms import ValidationError

class TamanioMaximoValidator:

    def __init__(self, maxfile=3):
        self.maxfile = maxfile
    
    def __call__(self, value):
        tamanio = value.size
        maxfiletamanio = self.maxfile * 1048576

        if tamanio > maxfiletamanio:
            raise ValidationError(f"El tamanio maximo del archivo debe ser menor de {self.maxfile}MB")
        return value