def salva_produto(nome_p, valor_p, quant_p, tipo_p, val_p):

    
    print("Chegou no local de salvar (Backup em Arquivo de Texto)")
    
    with open('dados_doadores.txt', 'a') as arquivo:

        arquivo.write(f"Doador: {nome_p}, CPF/Info: {valor_p}, Peso: {quant_p}kg, Sexo: {tipo_p}, Nasc: {val_p}\n")
        
    return "Sucesso"