import tkinter as tk
from tkinter import messagebox, ttk
import random
import os
import json

COR_FUNDO = "#003366"
COR_DESTAQUE = "#FFD700"
COR_TEXTO = "#FFFFFF"

with open("perguntas.json", "r", encoding="utf-8") as f:
    perguntas_por_categoria = json.load(f)

premios = [
    1000, 2000, 3000, 4000, 5000,
    10000, 20000, 30000, 40000, 60000,
    80000, 100000, 200000, 300000, 400000,
    500000, 1000000
]

def obter_dificuldade_por_nivel(nivel):
    if 1 <= nivel <= 3:
        return "facil"
    elif 4 <= nivel <= 9:
        return "medio"
    elif 10 <= nivel <= 14:
        return "dificil"
    elif 15 <= nivel <= 17:
        return "muito_dificil"

def salvar_ranking(nome, pontuacao):
    with open("ranking.txt", "a", encoding="utf-8") as f:
        f.write(f"{nome}:{pontuacao}\n")

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

class ShowDoMilhao:
    def __init__(self, root):
        self.root = root
        self.root.title("Show do Milhão")
        self.root.configure(bg=COR_FUNDO)

        self.nome_jogador = ""
        self.total = 0
        self.nivel = 1
        self.categorias_escolhidas = []
        self.ajudas = {"cartas": True, "universitarios": True, "plateia": True}
        self.tempo_restante = 20
        self.timer_id = None
        self.perguntas_ja_usadas = {}
        self.pulos_restantes = 3

        self.frame = tk.Frame(root, bg=COR_FUNDO)
        self.frame.pack(pady=20)

        self.tela_menu()

    def limpar_tela(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        for widget in self.frame.winfo_children():
            widget.destroy()

    def tela_menu(self):
        self.limpar_tela()
        tk.Label(self.frame, text="SHOW DO MILHÃO", font=("Helvetica", 24, "bold"), fg=COR_DESTAQUE, bg=COR_FUNDO).pack(pady=20)

        ttk.Button(self.frame, text="Jogar", command=self.tela_nome).pack(pady=5)
        ttk.Button(self.frame, text="Ranking", command=self.tela_ranking).pack(pady=5)
        ttk.Button(self.frame, text="Instruções", command=self.tela_instrucoes).pack(pady=5)
        ttk.Button(self.frame, text="Sair", command=self.root.quit).pack(pady=5)

    def tela_nome(self):
        self.limpar_tela()
        tk.Label(self.frame, text="Digite seu nome:", fg=COR_TEXTO, bg=COR_FUNDO).pack()
        self.nome_entry = ttk.Entry(self.frame)
        self.nome_entry.pack(pady=10)
        ttk.Button(self.frame, text="Próximo", command=self.tela_categorias_multiplas).pack()

    def tela_categorias_multiplas(self):
        self.nome_jogador = self.nome_entry.get().strip().title()
        if not self.nome_jogador:
            messagebox.showwarning("Aviso", "Digite um nome antes de continuar.")
            return

        self.limpar_tela()
        tk.Label(self.frame, text="Escolha 5 categorias:", fg=COR_TEXTO, bg=COR_FUNDO, font=("Helvetica", 14)).pack(pady=10)

        self.categoria_vars = {}
        categorias = list(perguntas_por_categoria.keys())

        for cat in categorias:
            var = tk.BooleanVar()
            self.categoria_vars[cat] = var
            ttk.Checkbutton(self.frame, text=cat.title(), variable=var).pack(anchor="w", padx=10)

        ttk.Button(self.frame, text="Começar Jogo", command=self.verificar_categorias_escolhidas).pack(pady=10)

    def verificar_categorias_escolhidas(self):
        selecionadas = [cat for cat, var in self.categoria_vars.items() if var.get()]
        if len(selecionadas) != 5:
            messagebox.showwarning("Aviso", "Selecione exatamente 5 categorias.")
            return
        self.categorias_escolhidas = selecionadas
        self.total = 0
        self.nivel = 1
        self.ajudas = {"cartas": True, "universitarios": True, "plateia": True}
        self.perguntas_ja_usadas = {}
        self.pulos_restantes = 3
        self.proxima_pergunta()

    def proxima_pergunta(self):
        self.limpar_tela()
        self.tempo_restante = 20

        dificuldade = obter_dificuldade_por_nivel(self.nivel)
        pergunta = None
        tentativa = 0

        while tentativa < 20:
            categoria = random.choice(self.categorias_escolhidas)
            perguntas_disponiveis = perguntas_por_categoria[categoria][dificuldade]
            usadas = self.perguntas_ja_usadas.get(self.nivel, [])
            restantes = [p for p in perguntas_disponiveis if p not in usadas]

            if restantes:
                pergunta = random.choice(restantes)
                self.pergunta_atual = pergunta
                self.perguntas_ja_usadas.setdefault(self.nivel, []).append(pergunta)
                break
            tentativa += 1

        if not pergunta:
            messagebox.showinfo("Erro", "Sem perguntas restantes para este nível.")
            self.tela_menu()
            return

        tk.Label(self.frame, text=f"Nível {self.nivel} – Prêmio: R${premios[self.nivel - 1]:,}", fg=COR_DESTAQUE, bg=COR_FUNDO, font=("Helvetica", 14)).pack(pady=10)
        tk.Label(self.frame, text=pergunta["pergunta"], wraplength=500, fg=COR_TEXTO, bg=COR_FUNDO).pack(pady=10)

        self.timer_label = tk.Label(self.frame, text="", fg=COR_TEXTO, bg=COR_FUNDO)
        self.timer_label.pack()
        self.progress = ttk.Progressbar(self.frame, length=200, maximum=20)
        self.progress.pack(pady=5)
        self.iniciar_timer()

        self.resposta_escolhida = tk.StringVar()
        for letra, opcao in pergunta["opcoes"].items():
            ttk.Radiobutton(self.frame, text=f"{letra}) {opcao}", variable=self.resposta_escolhida, value=letra).pack(anchor="w")

        ttk.Button(self.frame, text="Confirmar", command=self.confirmar_resposta).pack(pady=10)

        if self.pulos_restantes > 0:
            ttk.Button(self.frame, text=f"Pular Pergunta ({self.pulos_restantes} restantes)", command=self.pular_pergunta).pack(pady=5)

        if any(self.ajudas.values()):
            frame_ajuda = tk.Frame(self.frame, bg=COR_FUNDO)
            frame_ajuda.pack(pady=5)
            if self.ajudas["cartas"]:
                ttk.Button(frame_ajuda, text="Cartas", command=self.ajuda_cartas).pack(side="left", padx=5)
            if self.ajudas["universitarios"]:
                ttk.Button(frame_ajuda, text="Universitários", command=self.ajuda_universitarios).pack(side="left", padx=5)
            if self.ajudas["plateia"]:
                ttk.Button(frame_ajuda, text="Plateia", command=self.ajuda_plateia).pack(side="left", padx=5)

        ttk.Button(self.frame, text="Desistir", command=self.desistir).pack(pady=10)

    def iniciar_timer(self):
        self.timer_label.config(text=f"Tempo restante: {self.tempo_restante}s")
        self.progress['value'] = 20 - self.tempo_restante
        if self.tempo_restante > 0:
            self.tempo_restante -= 1
            self.timer_id = self.root.after(1000, self.iniciar_timer)
        else:
            messagebox.showinfo("Tempo esgotado", f"Você não respondeu a tempo!\nSua pontuação final foi de R${self.total:,}")
            salvar_ranking(self.nome_jogador, self.total)
            self.tela_menu()

    def confirmar_resposta(self):
        resposta = self.resposta_escolhida.get()
        if not resposta:
            messagebox.showwarning("Aviso", "Escolha uma opção antes de confirmar.")
            return

        correta = self.pergunta_atual["resposta"]
        if resposta == correta:
            self.total = premios[self.nivel - 1]
            self.nivel += 1
            if self.nivel > 17:
                self.fim_de_jogo("Parabéns! Você venceu o jogo!")
            else:
                self.proxima_pergunta()
        else:
            self.total //= 2
            self.fim_de_jogo(f"Resposta errada! A correta era '{correta}'.")

    def pular_pergunta(self):
        if self.pulos_restantes > 0:
            self.pulos_restantes -= 1
            messagebox.showinfo("Pergunta Pulada", f"Você pulou a pergunta! ({self.pulos_restantes} pulos restantes)")
            self.proxima_pergunta()
        else:
            messagebox.showwarning("Limite de pulos", "Você já usou todos os seus pulos.")

    def desistir(self):
        if messagebox.askyesno("Desistir", f"Tem certeza que deseja desistir com R${self.total:,}?"):
            self.fim_de_jogo("Você desistiu do jogo.")

    def fim_de_jogo(self, mensagem):
        salvar_ranking(self.nome_jogador, self.total)
        messagebox.showinfo("Fim de Jogo", f"{mensagem}\nPontuação final: R${self.total:,}.")
        self.tela_menu()

    def ajuda_cartas(self):
        self.ajudas["cartas"] = False
        correta = self.pergunta_atual["resposta"]
        opcoes = self.pergunta_atual["opcoes"]
        erradas = [k for k in opcoes if k != correta]
        eliminadas = random.sample(erradas, 2)
        texto = "Eliminando duas opções erradas:\n"
        for letra in opcoes:
            if letra not in eliminadas:
                texto += f"{letra}) {opcoes[letra]}\n"
        messagebox.showinfo("Cartas", texto)

    def ajuda_universitarios(self):
        self.ajudas["universitarios"] = False
        correta = self.pergunta_atual["resposta"]
        sugestao = correta if random.random() < 0.8 else random.choice([l for l in "ABCD" if l != correta])
        messagebox.showinfo("Universitários", f"Acredito que a resposta correta seja: {sugestao}")

    def ajuda_plateia(self):
        self.ajudas["plateia"] = False
        correta = self.pergunta_atual["resposta"]
        porcentagens = {"A": 0, "B": 0, "C": 0, "D": 0}
        correta_chance = random.randint(60, 80)
        restantes = [l for l in "ABCD" if l != correta]
        restantes_chances = sorted([random.randint(5, 20) for _ in range(3)])
        random.shuffle(restantes)
        porcentagens[correta] = correta_chance
        for letra, chance in zip(restantes, restantes_chances):
            porcentagens[letra] = chance

        texto = "Votos da plateia:\n"
        for letra, perc in porcentagens.items():
            texto += f"{letra}) {perc}%\n"
        messagebox.showinfo("Plateia", texto)

    def tela_ranking(self):
        self.limpar_tela()
        tk.Label(self.frame, text="Ranking dos Jogadores", font=("Helvetica", 16, "bold"), fg=COR_DESTAQUE, bg=COR_FUNDO).pack(pady=10)

        ranking = exibir_ranking()
        for i, (nome, pontos) in enumerate(ranking, 1):
            tk.Label(self.frame, text=f"{i}. {nome} – R${pontos:,}", fg=COR_TEXTO, bg=COR_FUNDO).pack()

        ttk.Button(self.frame, text="Voltar", command=self.tela_menu).pack(pady=10)

    def tela_instrucoes(self):
        self.limpar_tela()
        instrucoes = (
            "• O jogo possui 17 níveis de dificuldade crescente.\n"
            "• Cada nível sorteia 1 pergunta da categoria escolhida.\n"
            "• Você tem 3 ajudas disponíveis (1 uso por jogo):\n"
            "   - CARTAS: elimina 2 opções erradas\n"
            "   - UNIVERSITÁRIOS: dá uma sugestão de resposta\n"
            "   - PLATÉIA: mostra uma estimativa de votos do público\n"
            "• Você pode pular até 3 perguntas por jogo.\n"
            "• Ao errar, você perde metade da sua pontuação atual.\n"
            "• Ao desistir, você leva a pontuação acumulada."
        )
        tk.Label(self.frame, text="Instruções", font=("Helvetica", 16, "bold"), fg=COR_DESTAQUE, bg=COR_FUNDO).pack(pady=10)
        tk.Label(self.frame, text=instrucoes, wraplength=500, justify="left", fg=COR_TEXTO, bg=COR_FUNDO).pack(pady=10)
        ttk.Button(self.frame, text="Voltar", command=self.tela_menu).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShowDoMilhao(root)
    root.mainloop()
