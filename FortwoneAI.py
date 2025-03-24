# Saudação
print("\n" + "="*50)
print("Olá, seja bem-vindo(a) ao Simulador de Investimentos da Fortwone.")
print("="*50 + "\n")

print("Estamos aqui para ajudá-lo(a) a tomar decisões financeiras mais assertivas e inteligentes.")
print("Nosso objetivo é fornecer ferramentas e informações para que você possa investir no seu futuro com confiança.\n")

print("Este simulador irá avaliar sua situação financeira atual e, com base nisso, oferecer as melhores opções de investimento.")
print("Com a nossa análise, você terá um direcionamento para alcançar seus objetivos financeiros de maneira mais eficiente!\n")

print("Vamos começar? Responda algumas perguntas e descubra os investimentos ideais para o seu perfil e situação.")
print("\n" + "="*50 + "\n")

def coletar_dados():
    # Perguntas para identificar o perfil de risco
    print("\nResponda as seguintes perguntas para determinar seu perfil de risco:\n")

    print("1. Quando o mercado financeiro está em queda, como você reage?")
    resposta_1 = input("  1) Fico muito preocupado(a) e vendo meus investimentos\n"
                       "  2) Não me preocupo muito, espero que o mercado se recupere\n"
                       "  3) Vejo isso como uma oportunidade para investir mais: ")

    print("\n2. Você está disposto(a) a correr riscos para tentar obter um retorno maior?")
    resposta_2 = input("  1) Não\n"
                       "  2) Sim, mas com cautela\n"
                       "  3) Sim, quero obter altos retornos: ")

    print("\n3. Qual seria sua reação se um de seus investimentos caísse 20% no valor em um curto período de tempo?")
    resposta_3 = input("  1) Venderia todos os investimentos\n"
                       "  2) Esperaria o mercado se recuperar\n"
                       "  3) Aproveitaria para comprar mais: ")

    print("\n4. Qual é o seu objetivo principal com investimentos?")
    resposta_4 = input("  1) Segurança e estabilidade financeira\n"
                       "  2) Crescimento com um pouco de risco\n"
                       "  3) Obter grandes lucros em pouco tempo: ")

    # Analisando o perfil com base nas respostas
    if "1" in [resposta_1, resposta_2, resposta_3, resposta_4]:
        perfil = "conservador"
    elif "2" in [resposta_1, resposta_2, resposta_3, resposta_4]:
        perfil = "moderado"
    else:
        perfil = "agressivo"

    # Coleta do objetivo financeiro
    objetivo = input("\nQual é o seu objetivo financeiro? (Exemplo: Aposentadoria, Compra de Imóvel, etc.): ").lower()

    # Agora, perguntamos quanto a pessoa pode investir
    print("\nAgora, vamos coletar algumas informações financeiras.\n")
    valor_investido_inicial = float(input("Quanto dinheiro você tem disponível para investir inicialmente (em R$)? "))
    valor_mensal = float(input("Quanto você pode investir mensalmente (em R$)? "))

    # Armazenamento de dados
    dados_usuario = {
        "valor_investido": valor_investido_inicial,
        "valor_mensal": valor_mensal,
        "perfil": perfil,
        "objetivo": objetivo
    }
    
    return dados_usuario

# Função para análise de perfil e recomendação de investimentos
def analisar_perfil(dados_usuario):
    perfil = dados_usuario["perfil"]
    
    # Definindo a alocação de investimentos com base no perfil
    if perfil == "conservador":
        recomendacoes = {
            "Renda Fixa": 70,
            "Fundos Imobiliários": 30,
            "Ações": 0
        }
    elif perfil == "moderado":
        recomendacoes = {
            "Renda Fixa": 40,
            "Fundos Imobiliários": 40,
            "Ações": 20
        }
    elif perfil == "agressivo":
        recomendacoes = {
            "Renda Fixa": 20,
            "Fundos Imobiliários": 30,
            "Ações": 50
        }
    else:
        recomendacoes = {
            "Renda Fixa": 0,
            "Fundos Imobiliários": 0,
            "Ações": 0
        }
        
    return recomendacoes

# Função para calcular o valor final do investimento com juros compostos
def calcular_valor_futuro(valor_investido, valor_mensal, taxa_juros, anos):
    """Calcula o valor futuro considerando o valor inicial e os aportes mensais"""
    # Fórmula para juros compostos com aportes mensais
    valor_futuro = valor_investido * (1 + taxa_juros) ** anos
    for i in range(anos * 12):
        valor_futuro += valor_mensal * (1 + taxa_juros) ** (anos - (i / 12))
    return valor_futuro

# Função para gerar o relatório personalizado
def gerar_relatorio(dados_usuario, recomendacoes):
    perfil = dados_usuario["perfil"]
    objetivo = dados_usuario["objetivo"]
    valor_investido = dados_usuario["valor_investido"]
    valor_mensal = dados_usuario["valor_mensal"]
    
    print("\n--- Relatório Personalizado ---")
    print(f"Perfil: {perfil.capitalize()}")
    print(f"Objetivo: {objetivo.capitalize()}")
    print(f"Valor Inicial para Investir: R${valor_investido:.2f}")
    print(f"Investimento Mensal: R${valor_mensal:.2f}")
    
    print("\nRecomendação de Alocação de Investimentos:")
    for tipo, percentual in recomendacoes.items():
        print(f"{tipo}: {percentual}%")
    
    # Taxas de retorno dos investimentos
    taxas_juros = {
        "Renda Fixa": 0.08,  # 8% ao ano
        "Fundos Imobiliários": 0.10,  # 10% ao ano
        "Ações": 0.12  # 12% ao ano
    }

    # Cálculos de projeção de ganhos em 10 e 15 anos
    print("\nProjeção de Ganhos:")
    for tipo, percentual in recomendacoes.items():
        valor_alocado = (valor_investido * percentual / 100) + (valor_mensal * percentual / 100)
        valor_futuro_10_anos = calcular_valor_futuro(valor_alocado, valor_mensal, taxas_juros[tipo], 10)
        valor_futuro_15_anos = calcular_valor_futuro(valor_alocado, valor_mensal, taxas_juros[tipo], 15)

        print(f"\nPara {tipo}:")
        print(f"  Valor Alocado: R${valor_alocado:.2f}")
        print(f"  Projeção após 10 anos: R${valor_futuro_10_anos:.2f}")
        print(f"  Projeção após 15 anos: R${valor_futuro_15_anos:.2f}")

# Função para finalizar a simulação
def finalizar_simulacao():
    print("\n--- Finalizando a Simulação ---")
    print("\nParabéns! Você concluiu a simulação e obteve uma visão detalhada sobre seus investimentos.")
    print("Com base nos resultados, você agora tem uma ideia mais clara de como pode alcançar seus objetivos financeiros.\n")
    
    # Opção para realizar nova simulação ou encerrar
    resposta = input("Deseja simular novamente? (s/n): ").lower()
    
    if resposta == "s":
        print("\nÓtimo! Vamos começar outra simulação.")
        main()  # Reinicia o processo de simulação
    else:
        print("\nAgradecemos por usar o Simulador de Investimentos da Fortwone. Boa sorte em seus investimentos!")
        print("Lembre-se: investir é um passo importante para alcançar a sua liberdade financeira!\n")
        print("="*50)
        print("Até logo!")
        print("="*50)

# Função principal
def main():
    # Coletando os dados do usuário
    dados_usuario = coletar_dados()
    
    # Analisando o perfil do usuário
    recomendacoes = analisar_perfil(dados_usuario)
    
    # Gerando o relatório final
    gerar_relatorio(dados_usuario, recomendacoes)
    
    # Finalizando a simulação
    finalizar_simulacao()

# Executar o programa
if __name__ == "__main__":
    main()
