#Se importo la clase "Carro" y se agrego a la función original de Juan la línea 6 del código "carro = Carro(request)" porque por alguna razón
#tiraba un error de tipo "KeyError".

from .carro import Carro

def importe_total_carro(request):
    total = 0
    if not request.session.get('carro'):
        request.session['carro'] = {}

    for key, value in request.session["carro"].items():
        total += (float(value["precio"]) * value["cantidad"])

    return {"importe_total_carro": total}

