from django.shortcuts import render
from models import Nave, Pato

# Create your views here.

def home(request):
    return render(request,'home.html')

def naves(request):
    nova_nave = Nave()

    nova_nave.tamnanho = request.POST.get('tamanho')
    nova_nave.cor = request.POST.get('cor')
    nova_nave.local_queda = request.POST.get('local_queda')
    nova_nave.armamento = request.POST.get('armamento')
    nova_nave.combustivel = request.POST.get('combustivel')
    nova_nave.tripulantes = request.POST.get('tripulantes')
    nova_nave.avaria = request.POST.get('avaria')
    nova_nave.potencial_prospecção_tecnologico = request.POST.get('potencial_prospecção_tecnologico')
    nova_nave.periculosidade = request.POST.get('periculosidade')

    lista_etiquetas = []


    if "nenhum" in nova_nave.tripulantes.lower():
        lista_etiquetas.append("Nave de Fugitivos")

    if nova_nave.armamento in ["Nuclear", "Pesado"]:
        lista_etiquetas.append("Arsenal Alienígena")

    if nova_nave.combustivel in ["Antimatéria", "Plasma"]:
        lista_etiquetas.append("Fonte de Energia Alternativa")

    if nova_nave.periculosidade >= 7:
        if nova_nave.tamanho in ["Gigantesca", "Grande"]:
            lista_etiquetas.append("Estrela da Morte")
        else:
            lista_etiquetas.append("Ameaça em Potencial")

    if nova_nave.potencial_prospecção_tecnologico >= 7:
        if nova_nave.tamanho in ["Gigantesca", "Grande"]:
            lista_etiquetas.append("Apice da Tecnologia")
        else:
            lista_etiquetas.append("Joia Tecnológica")

    elif nova_nave.potencial_prospecção_tecnologico < 7 or nova_nave.avaria in ["Perda total", "Muito destruída"]:
        lista_etiquetas.append("Sucata Espacial")
    else:
        lista_etiquetas.append("Nave Espacial Normal")
    
    str_etiquetas = f"{', '.join(lista_etiquetas)}"
    nova_nave.etiquetas = str_etiquetas

    naves = {
        'naves': Nave.objects.all()
    }

    return render(request,'naves.html', naves)

def patos(request):
    novo_pato = Pato()

    novo_pato.pele_esverdeada = request.POST.get('pele_esverdeada')
    novo_pato.bico_pequeno = request.POST.get('bico_pequeno')
    novo_pato.sotaque_esquisito = request.POST.get('sotaque_esquisito')
    novo_pato.local = request.POST.get('local')
    novo_pato.quantidade = request.POST.get('quantidade')
    if novo_pato.pele_esverdeada and novo_pato.bico_pequeno and novo_pato.sotaque_esquisito:
        novo_pato.xenofago = True
        if novo_pato.quantidade == "Sozinho":
            if novo_pato.local in ["Lago", "Mar"]:
                novo_pato.plano_captura = "Usar a Rede de Titânio para capturar o pato."
            elif novo_pato.local in ["Floresta", "Parque"]:
                novo_pato.plano_captura = "Usar a Gaiola de Aço com iscas para capturar o pato."
            else:
                novo_pato.plano_captura = "Usar o Drone de Captura para capturar o pato."

        elif novo_pato.quantidade == "Em dupla":
            if novo_pato.local in ["Lago", "Mar"]:
                novo_pato.plano_captura = "Usar a Rede de Titânio em coordenação para cercar os patos."
            elif novo_pato.local in ["Floresta", "Parque"]:
                novo_pato.plano_captura = "Montar uma gaiola maior com iscas para capturar os patos."
            else:
                novo_pato.plano_captura = "Usar dois Drones de Captura para flanquear e capturar os patos."

        elif novo_pato.quantidade == "Em bando pequeno":
            if novo_pato.local in ["Lago", "Mar"]:
                novo_pato.plano_captura = "Usar a Rede de Titânio para capturar o bando pequeno."
            elif novo_pato.local in ["Floresta", "Parque"]:
                novo_pato.plano_captura = "Montar várias gaiolas com iscas para capturar o bando pequeno."
            else:
                novo_pato.plano_captura = "Usar drones para atrair e capturar o bando pequeno."

        else:
            if novo_pato.local in ["Lago", "Mar"]:
                novo_pato.plano_captura = "Usar uma grande Rede de Titânio para cercar o bando grande."
            elif novo_pato.local in ["Floresta", "Parque"]:
                novo_pato.plano_captura = "Montar armadilhas de gaiola interligadas para capturar o bando grande."
            else:
                novo_pato.plano_captura = "Usar uma frota de Drones de Captura para dispersar e capturar o bando grande."
    else:
        novo_pato.xenofago = False
        novo_pato.plano_captura = "Não é um pato xenofago, deixe ele fazer quack quack." 

    patos = {
        'patos': Pato.objects.all()
    }

    return render(request,'patos.html', patos)

