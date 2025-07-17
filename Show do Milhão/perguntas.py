import json

def carregar_perguntas():
    with open("perguntas.json", "r", encoding="utf-8") as f:
        return json.load(f)

def obter_dificuldade_por_nivel(nivel):
    if 1 <= nivel <= 3:
        return "facil"
    elif 4 <= nivel <= 9:
        return "medio"
    elif 10 <= nivel <= 14:
        return "dificil"
    elif 15 <= nivel <= 17:
        return "muito_dificil"
