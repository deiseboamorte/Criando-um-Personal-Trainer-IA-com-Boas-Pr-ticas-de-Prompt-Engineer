def gerar_plano_treino(biotipo, dias_disponiveis, tipo_exercicio):
    plano = ""
    
    # Aquecimento
    plano += "1. **Aquecimento**: 5-10 minutos de exercícios leves como corrida ou polichinelos.\n\n"
    
    # Plano de Exercícios
    if dias_disponiveis == "1 dia":
        plano += "2. **Treino Full Body**:\n"
        if biotipo == "Ectomorfo":
            plano += "   - **Supino com barra**: 3 séries de 10 repetições\n"
            plano += "   - **Agachamento com barra**: 3 séries de 10 repetições\n"
            plano += "   - **Remada com halteres**: 3 séries de 10 repetições\n"
            plano += "   - **Abdominais**: 3 séries de 15 repetições\n"
        elif biotipo == "Mesomorfo":
            plano += "   - **Puxada na frente**: 4 séries de 8-12 repetições\n"
            plano += "   - **Leg Press**: 4 séries de 8-12 repetições\n"
            plano += "   - **Desenvolvimento com halteres**: 4 séries de 8-12 repetições\n"
            plano += "   - **Prancha**: 3 séries de 30-60 segundos\n"
        elif biotipo == "Endomorfo":
            plano += "   - **Supino inclinado**: 3 séries de 12 repetições\n"
            plano += "   - **Agachamento livre**: 3 séries de 12 repetições\n"
            plano += "   - **Remada baixa**: 3 séries de 12 repetições\n"
            plano += "   - **Abdominais e prancha**: 3 séries de 15 repetições e 30 segundos\n"
    
    elif dias_disponiveis == "3 dias":
        plano += "2. **Treino ABC**:\n"
        if tipo_exercicio == "Funcional":
            plano += "   - **Dia A (Peito e Tríceps)**: Flexões, dips\n"
            plano += "   - **Dia B (Costas e Bíceps)**: Pull-ups, kettlebell swings\n"
            plano += "   - **Dia C (Pernas e Ombros)**: Agachamentos, burpees\n"
        elif tipo_exercicio == "Maquinário":
            plano += "   - **Dia A (Peito e Tríceps)**: Supino reto na máquina, tríceps na polia\n"
            plano += "   - **Dia B (Costas e Bíceps)**: Puxada na frente, bíceps na máquina\n"
            plano += "   - **Dia C (Pernas e Ombros)**: Leg Press, elevações laterais na máquina\n"
    
    elif dias_disponiveis == "5 dias":
        plano += "2. **Treino ABCDE**:\n"
        if tipo_exercicio == "Peso Livre":
            plano += "   - **Dia A (Peito)**: Supino reto, inclinado\n"
            plano += "   - **Dia B (Costas)**: Remada com barra, pull-ups\n"
            plano += "   - **Dia C (Pernas)**: Agachamentos, levantamento terra\n"
            plano += "   - **Dia D (Ombros)**: Desenvolvimento militar, elevações laterais\n"
            plano += "   - **Dia E (Braços e Abdômen)**: Bíceps curls, tríceps extensões, abdominais\n"
    
    # Progressão e Recuperação
    plano += "\n3. **Progressão**: Aumente o peso gradualmente e ajuste as repetições conforme o progresso.\n"
    plano += "4. **Recuperação**: Realize alongamentos após os treinos e mantenha-se hidratado.\n"

    return plano

# Solicita informações do usuário
biotipo = input("Digite seu biotipo corporal (Ectomorfo, Mesomorfo, Endomorfo): ")
dias_disponiveis = input("Digite o número de dias disponíveis para treinar por semana (1, 3, 5): ")
tipo_exercicio = input("Digite o tipo de exercício preferido (Funcional, Maquinário, Peso Livre, Cardio, HIIT): ")

# Gera o plano de treino
plano_treino = gerar_plano_treino(biotipo, dias_disponiveis, tipo_exercicio)
print("\n**Plano de Treino Personalizado:**\n")
print(plano_treino)
