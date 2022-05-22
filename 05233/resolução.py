def fatia(texto, qtd_pedacos, tipo):
    """Função que fatia uma string na quantidade de pedaços pedidos (2,3 ou 4)
    e retorna uma lista ou tupla, de acordo com o último parametro.
    string, int, string -> lista"""
    tamanho_pedaco = len(texto)//qtd_pedacos
    if(tipo == "lista"):
        if(qtd_pedacos==2):
            lista = [texto[:tamanho_pedaco],texto[tamanho_pedaco:]]
            return lista
        if(qtd_pedacos==3):
            lista = [texto[:tamanho_pedaco],texto[tamanho_pedaco:tamanho_pedaco*2],texto[tamanho_pedaco*2:]]
            return lista
        if(qtd_pedacos==4):
            lista =[texto[:tamanho_pedaco],texto[tamanho_pedaco:tamanho_pedaco*2],
            texto[tamanho_pedaco*2:tamanho_pedaco*3],texto[tamanho_pedaco*3:]]
            return lista
    else:
        if(qtd_pedacos==2):
            tupla = (texto[:tamanho_pedaco],texto[tamanho_pedaco:])
            return tupla
        if(qtd_pedacos==3):
            tupla = (texto[:tamanho_pedaco],texto[tamanho_pedaco:tamanho_pedaco*2],texto[tamanho_pedaco*2:])
            return tupla
        if(qtd_pedacos==4):
            tupla =(texto[:tamanho_pedaco],texto[tamanho_pedaco:tamanho_pedaco*2],
            texto[tamanho_pedaco*2:tamanho_pedaco*3],texto[tamanho_pedaco*3:])
            return tupla
