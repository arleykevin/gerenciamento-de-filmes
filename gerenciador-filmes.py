# PROJETO: Análise e Gerenciamento de Filmes

# Lista de filmes (dados iniciais)
filmes = [
    {"titulo": "A Origem", "ano": 2010, "genero": "Ficção Científica", "nota": 9.0},
    {"titulo": "Pulp Fiction", "ano": 1994, "genero": "Crime", "nota": 8.9},
    {"titulo": "Interestelar", "ano": 2014, "genero": "Ficção Científica", "nota": 8.6},
    {"titulo": "O Poderoso Chefão", "ano": 1972, "genero": "Crime", "nota": 9.2},
    {"titulo": "A Chegada", "ano": 2016, "genero": "Ficção Científica", "nota": 7.9},
    {"titulo": "Forrest Gump", "ano": 1994, "genero": "Drama", "nota": 8.8},
    {"titulo": "O Cavaleiro das Trevas", "ano": 2008, "genero": "Ação", "nota": 9.0},
    {"titulo": "A Vida é Bela", "ano": 1997, "genero": "Comédia", "nota": 8.6},
    {"titulo": "Matrix", "ano": 1999, "genero": "Ficção Científica", "nota": 8.7},
    {"titulo": "O Senhor dos Anéis: O Retorno do Rei", "ano": 2003, "genero": "Fantasia", "nota": 9.0},
    {"titulo": "Star Wars: Episódio V - O Império Contra-Ataca", "ano": 1980, "genero": "Ficção Científica", "nota": 8.7},
    {"titulo": "A Origem dos Guardiões", "ano": 2012, "genero": "Animação", "nota": 7.3},
]

# Função para coletar dados de um novo filme a partir do usuário
def coleta_dados_novo_filme():
    """Coleta os dados do usuário para um novo filme e retorna um dicionário."""
    print("\n--- Adicionar Novo Filme ---")
    titulo = input("Título do filme: ")
    ano = int(input("Ano de lançamento: "))
    genero = input("Gênero: ")
    nota = float(input("Nota (de 0 a 10): "))
    
    return {
        "titulo": titulo,
        "ano": ano,
        "genero": genero,
        "nota": nota
    }

# 1. Função com List Comprehension
# Mapeamento do requisito: Filtro por nota mínima
# Este requisito será implementado na função 'filtra_por_nota_minima' usando list comprehension.
def filtra_por_nota_minima(lista_de_filmes, nota_minima):
    """
    Filtra filmes que possuem nota igual ou superior à nota_minima.
    Utiliza uma list comprehension.
    """
    filmes_filtrados = [
        filme for filme in lista_de_filmes if filme["nota"] >= nota_minima
    ]
    return filmes_filtrados

# 2. Função de Alta Ordem e Função Lambda
# Mapeamento do requisito: Filtro por gênero
# Este requisito será implementado na função 'filtra_por_genero' usando a função de alta ordem 'filter' e uma lambda.
def filtra_por_genero(lista_de_filmes, genero_alvo):
    """
    Filtra filmes que pertencem ao gênero_alvo.
    Utiliza a função de alta ordem filter() e uma função lambda.
    """
    filmes_filtrados = list(filter(lambda filme: filme["genero"] == genero_alvo, lista_de_filmes))
    return filmes_filtrados

# 3. Closure
# Mapeamento do requisito: Criação de um filtro customizado
# Este requisito será implementado na função 'gerar_filtro_por_nota' que retorna uma closure.
def gerar_filtro_por_nota(nota_minima):
    """
    Cria e retorna uma função (Closure) que já possui a nota_minima 'memorizada'.
    """
    def filtro_customizado(filme):
        return filme["nota"] >= nota_minima
    return filtro_customizado

# 4. Função Adicional: Adiciona um novo filme de forma funcional
# Mapeamento do requisito: Cadastro de filmes
# Este requisito será implementado na função 'cadastra_filme'.
def cadastra_filme(lista_atual, novo_filme):
    """Adiciona um novo filme à lista de forma funcional (imutável)."""
    return lista_atual + [novo_filme]

# 5. Função Adicional: Exibe os filmes
# Mapeamento do requisito: Exibição de dados
def exibe_filmes(lista_de_filmes):
    """Exibe os filmes de forma legível no console."""
    if not lista_de_filmes:
        print("Nenhum filme encontrado.")
        return
    
    print("\n--- FILMES ---")
    for filme in lista_de_filmes:
        print(f"Título: {filme['titulo']}")
        print(f"Ano: {filme['ano']}")
        print(f"Gênero: {filme['genero']}")
        print(f"Nota: {filme['nota']}")
        print("-" * 20)

# --- EXECUÇÃO DO PROGRAMA ---

if __name__ == "__main__":

    # Teste para mostrar que a lista original não mudou
    print("--- Lista de filmes ORIGINAL (não modificada) ---")
    exibe_filmes(filmes)

    
    print("Iniciando o programa de Análise de Filmes...")
    
    # Testando a list comprehension (filtra por nota mínima)
    print("\n1. Testando filtro de filmes com nota >= 8.8:")
    filmes_bons = filtra_por_nota_minima(filmes, 8.8)
    exibe_filmes(filmes_bons)

    # Testando a função de alta ordem e lambda (filtra por gênero)
    print("\n2. Testando filtro de filmes de Ficção Científica:")
    filmes_ficcao = filtra_por_genero(filmes, "Ficção Científica")
    exibe_filmes(filmes_ficcao)

    # Testando a closure
    print("\n3. Testando filtro de filmes com nota >= 9.0 usando uma closure:")
    filtro_nota_9 = gerar_filtro_por_nota(9.0)
    filmes_excelentes = list(filter(filtro_nota_9, filmes))
    exibe_filmes(filmes_excelentes)
    
    # Testando o cadastro de um novo filme
    print("\n4. Testando o cadastro de um novo filme (imutabilidade):")
    novo_filme = {"titulo": "Interiores", "ano": 2024, "genero": "Drama", "nota": 7.5}
    filmes_atualizado = cadastra_filme(filmes, novo_filme)
    print("--- Nova lista de filmes (original não foi modificada) ---")
    exibe_filmes(filmes_atualizado)
