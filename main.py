import pandas as pd

# Função para registrar uma nova revendedora
def registrar_revendedora(df, nome, endereco, cpf, contato):
    nova_revendedora = {
        'Nome': nome,
        'Endereço': endereco,
        'CPF': cpf,
        'Contato': contato
    }
    df = df.append(nova_revendedora, ignore_index=True)
    return df

# Função para adicionar uma venda
def adicionar_venda(df, codigo, descricao, valor_unitario, quantidade, situacao):
    nova_venda = {
        'Código': codigo,
        'Descrição': descricao,
        'Valor Unitário': valor_unitario,
        'Quantidade': quantidade,
        'Situação': situacao
    }
    df = df.append(nova_venda, ignore_index=True)
    return df

# Função para calcular comissão
def calcular_comissao(valor_venda):
    if valor_venda >= 400:
        return valor_venda * 0.50
    elif valor_venda >= 100:
        return valor_venda * 0.30
    else:
        return 0

# Exemplo de uso
if __name__ == "__main__":
    # DataFrames para armazenar revendedoras e vendas
    df_revendedoras = pd.DataFrame(columns=['Nome', 'Endereço', 'CPF', 'Contato'])
    df_vendas = pd.DataFrame(columns=['Código', 'Descrição', 'Valor Unitário', 'Quantidade', 'Situação'])

    # Registrar revendedoras
    df_revendedoras = registrar_revendedora(df_revendedoras, 'Ana Silva', 'Rua A, 123', '123.456.789-00', '(11) 98765-4321')
    df_revendedoras = registrar_revendedora(df_revendedoras, 'João Oliveira', 'Rua B, 456', '987.654.321-00', '(21) 12345-6789')

    # Adicionar vendas
    df_vendas = adicionar_venda(df_vendas, '001', 'Anel de Ouro', 150.00, 2, 'Vendido')
    df_vendas = adicionar_venda(df_vendas, '002', 'Brinco de Prata', 80.00, 5, 'Devolvido')

    # Mostrar DataFrames
    print("Revendedoras:")
    print(df_revendedoras)
    print("\nVendas:")
    print(df_vendas)

    # Calcular e mostrar comissões
    valor_venda = 300
    comissao = calcular_comissao(valor_venda)
    print(f"\nComissão para uma venda de R${valor_venda}: R${comissao:.2f}")
