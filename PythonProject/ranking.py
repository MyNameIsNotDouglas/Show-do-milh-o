def salvar_ranking(nome, pontuacao):
    ranking = []
    try:
        with open("ranking.txt", "r", encoding="utf-8") as f:
            for linha in f:
                if ":" in linha:
                    n, p = linha.strip().split(":")
                    ranking.append((n, int(p)))
    except FileNotFoundError:
        pass

    atualizado = False
    for i, (n, p) in enumerate(ranking):
        if n == nome:
            if pontuacao > p:
                ranking[i] = (nome, pontuacao)
            atualizado = True
            break

    if not atualizado:
        ranking.append((nome, pontuacao))

    with open("ranking.txt", "w", encoding="utf-8") as f:
        for n, p in ranking:
            f.write(f"{n}:{p}\n")

def exibir_ranking():
    try:
        with open("ranking.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
            ranking = []
            for linha in linhas:
                if ":" in linha:
                    nome, pontos = linha.strip().split(":")
                    ranking.append((nome, int(pontos)))
            ranking.sort(key=lambda x: x[1], reverse=True)
            return ranking[:20]
    except FileNotFoundError:
        return []

def remover_jogador_do_ranking(nome):
    try:
        with open("ranking.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        novas_linhas = [linha for linha in linhas if not linha.lower().startswith(nome.lower() + ":")]

        with open("ranking.txt", "w", encoding="utf-8") as f:
            f.writelines(novas_linhas)

        return len(novas_linhas) < len(linhas)
    except FileNotFoundError:
        return False
