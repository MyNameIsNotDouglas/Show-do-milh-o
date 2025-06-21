from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import random
import csv
from datetime import datetime

COR_PRIMARIA = "#004aad"
COR_SECUNDARIA = "#ffcc00"

premios = [
    1000, 2000, 3000, 4000, 5000,
    10000, 20000, 30000, 40000, 60000,
    80000, 100000, 200000, 300000, 400000,
    500000, 1000000
]

def nome_nivel(numero):
    if numero <= 5:
        return f"facil_{numero}"
    elif numero <= 10:
        return f"media_{numero}"
    elif numero <= 15:
        return f"dificil_{numero}"
    else:
        return f"muito_dificil_{numero}"

perguntas_por_nivel = {
    "facil_1": [
        {"pergunta": "Quanto é 1 + 1?", "opcoes": {"A": "1", "B": "2", "C": "3", "D": "4"}, "resposta": "B"},
        {"pergunta": "Qual cor representa o céu durante o dia?", "opcoes": {"A": "Azul", "B": "Verde", "C": "Roxo", "D": "Preto"}, "resposta": "A"},
        {"pergunta": "Qual o oposto de quente?", "opcoes": {"A": "Frio", "B": "Forte", "C": "Lento", "D": "Rápido"}, "resposta": "A"},
        {"pergunta": "Quantas patas tem um cachorro?", "opcoes": {"A": "2", "B": "3", "C": "4", "D": "5"}, "resposta": "C"},
        {"pergunta": "Qual é o plural de 'cão'?", "opcoes": {"A": "Cãos", "B": "Cãoses", "C": "Cães", "D": "Cãez"}, "resposta": "C"}
    ],
    "facil_2": [
        {"pergunta": "Qual desses é um vegetal?", "opcoes": {"A": "Carro", "B": "Cenoura", "C": "Mesa", "D": "Livro"}, "resposta": "B"},
        {"pergunta": "Qual o número que vem depois do 5?", "opcoes": {"A": "6", "B": "7", "C": "4", "D": "8"}, "resposta": "A"},
        {"pergunta": "Qual desses é um animal?", "opcoes": {"A": "Computador", "B": "Gato", "C": "Mesa", "D": "Telefone"}, "resposta": "B"},
        {"pergunta": "De que cor é a banana madura?", "opcoes": {"A": "Verde", "B": "Amarela", "C": "Azul", "D": "Roxa"}, "resposta": "B"},
        {"pergunta": "Qual a forma de uma bola?", "opcoes": {"A": "Quadrada", "B": "Triangular", "C": "Oval", "D": "Redonda"}, "resposta": "D"}
    ],
    "facil_3": [
        {"pergunta": "Qual o nome do nosso planeta?", "opcoes": {"A": "Marte", "B": "Júpiter", "C": "Terra", "D": "Vênus"}, "resposta": "C"},
        {"pergunta": "O que usamos para escrever?", "opcoes": {"A": "Martelo", "B": "Caneta", "C": "Colher", "D": "Tesoura"}, "resposta": "B"},
        {"pergunta": "Qual é o contrário de alto?", "opcoes": {"A": "Curto", "B": "Grande", "C": "Baixo", "D": "Fraco"}, "resposta": "C"},
        {"pergunta": "Qual parte do corpo usamos para ver?", "opcoes": {"A": "Mãos", "B": "Olhos", "C": "Pernas", "D": "Ouvidos"}, "resposta": "B"},
        {"pergunta": "Qual animal mia?", "opcoes": {"A": "Cachorro", "B": "Gato", "C": "Pássaro", "D": "Peixe"}, "resposta": "B"}
    ],
    "facil_4": [
        {"pergunta": "Qual o nome do líquido que bebemos?", "opcoes": {"A": "Ferro", "B": "Vento", "C": "Água", "D": "Areia"}, "resposta": "C"},
        {"pergunta": "Qual é o primeiro mês do ano?", "opcoes": {"A": "Dezembro", "B": "Julho", "C": "Janeiro", "D": "Março"}, "resposta": "C"},
        {"pergunta": "De qual cor é a laranja?", "opcoes": {"A": "Amarela", "B": "Roxa", "C": "Verde", "D": "Laranja"}, "resposta": "D"},
        {"pergunta": "Qual desses é um meio de transporte?", "opcoes": {"A": "Avião", "B": "Mesa", "C": "Travesseiro", "D": "Janela"}, "resposta": "A"},
        {"pergunta": "O que usamos para comer sopa?", "opcoes": {"A": "Garfo", "B": "Faca", "C": "Colher", "D": "Caneta"}, "resposta": "C"}
    ],
    "facil_5": [
        {"pergunta": "Qual o menor número natural?", "opcoes": {"A": "1", "B": "0", "C": "2", "D": "-1"}, "resposta": "B"},
        {"pergunta": "Qual animal produz leite?", "opcoes": {"A": "Galo", "B": "Cavalo", "C": "Vaca", "D": "Tigre"}, "resposta": "C"},
        {"pergunta": "Quem é o personagem principal da Bíblia?", "opcoes": {"A": "Moisés", "B": "Adão", "C": "Jesus", "D": "Noé"}, "resposta": "C"},
        {"pergunta": "O que fazemos quando estamos cansados?", "opcoes": {"A": "Dormimos", "B": "Comemos", "C": "Corremos", "D": "Pulamos"}, "resposta": "A"},
        {"pergunta": "Qual é a moeda usada no Brasil?", "opcoes": {"A": "Dólar", "B": "Peso", "C": "Real", "D": "Euro"}, "resposta": "C"}
    ],
        "media_6": [
        {"pergunta": "Qual a capital da França?", "opcoes": {"A": "Paris", "B": "Londres", "C": "Roma", "D": "Berlim"}, "resposta": "A"},
        {"pergunta": "Quem escreveu 'O Pequeno Príncipe'?", "opcoes": {"A": "Saint-Exupéry", "B": "Machado de Assis", "C": "J. K. Rowling", "D": "Monteiro Lobato"}, "resposta": "A"},
        {"pergunta": "Quantos segundos tem um minuto?", "opcoes": {"A": "60", "B": "90", "C": "30", "D": "100"}, "resposta": "A"},
        {"pergunta": "Qual é o símbolo químico da água?", "opcoes": {"A": "H2O", "B": "O2", "C": "CO2", "D": "NaCl"}, "resposta": "A"},
        {"pergunta": "Quem descobriu o Brasil?", "opcoes": {"A": "Pedro Álvares Cabral", "B": "Dom Pedro I", "C": "Tiradentes", "D": "Cabral Machado"}, "resposta": "A"}
    ],
    "media_7": [
        {"pergunta": "Quantos estados tem o Brasil?", "opcoes": {"A": "26", "B": "27", "C": "25", "D": "28"}, "resposta": "B"},
        {"pergunta": "Qual é o maior país do mundo em extensão territorial?", "opcoes": {"A": "Canadá", "B": "China", "C": "Rússia", "D": "EUA"}, "resposta": "C"},
        {"pergunta": "Qual é o planeta mais próximo do Sol?", "opcoes": {"A": "Vênus", "B": "Terra", "C": "Marte", "D": "Mercúrio"}, "resposta": "D"},
        {"pergunta": "Qual o valor de π (pi) aproximado?", "opcoes": {"A": "2,71", "B": "1,61", "C": "3,14", "D": "4,13"}, "resposta": "C"},
        {"pergunta": "Qual é o coletivo de lobos?", "opcoes": {"A": "Bando", "B": "Matilha", "C": "Cardume", "D": "Manada"}, "resposta": "B"}
    ],
    "media_8": [
        {"pergunta": "Qual é o maior oceano do planeta?", "opcoes": {"A": "Atlântico", "B": "Índico", "C": "Pacífico", "D": "Ártico"}, "resposta": "C"},
        {"pergunta": "Qual destes é um mamífero?", "opcoes": {"A": "Jacaré", "B": "Pinguim", "C": "Golfinho", "D": "Galinha"}, "resposta": "C"},
        {"pergunta": "Quem foi Albert Einstein?", "opcoes": {"A": "Pintor", "B": "Físico", "C": "Político", "D": "Músico"}, "resposta": "B"},
        {"pergunta": "Qual instrumento mede temperatura?", "opcoes": {"A": "Barômetro", "B": "Régua", "C": "Termômetro", "D": "Bússola"}, "resposta": "C"},
        {"pergunta": "Qual é o plural de lápis?", "opcoes": {"A": "Lápizes", "B": "Lápis", "C": "Lápises", "D": "Lápisus"}, "resposta": "B"}
    ],
    "media_9": [
        {"pergunta": "O que significa ONU?", "opcoes": {"A": "Organização Nacional Unida", "B": "Ordem Nacional Urbana", "C": "Organização das Nações Unidas", "D": "Oficina Nacional Unida"}, "resposta": "C"},
        {"pergunta": "Quem pintou a Mona Lisa?", "opcoes": {"A": "Van Gogh", "B": "Michelangelo", "C": "Leonardo da Vinci", "D": "Rafael"}, "resposta": "C"},
        {"pergunta": "Qual é o menor país do mundo?", "opcoes": {"A": "Monaco", "B": "Vaticano", "C": "Malta", "D": "Luxemburgo"}, "resposta": "B"},
        {"pergunta": "Quem inventou o telefone?", "opcoes": {"A": "Einstein", "B": "Galileu", "C": "Alexander Graham Bell", "D": "Edison"}, "resposta": "C"},
        {"pergunta": "Qual é a capital de Minas Gerais?", "opcoes": {"A": "Belo Horizonte", "B": "Vitória", "C": "Salvador", "D": "Goiânia"}, "resposta": "A"}
    ],
    "media_10": [
        {"pergunta": "Quem escreveu Dom Casmurro?", "opcoes": {"A": "José de Alencar", "B": "Machado de Assis", "C": "Manuel Bandeira", "D": "Clarice Lispector"}, "resposta": "B"},
        {"pergunta": "Quanto é a raiz quadrada de 81?", "opcoes": {"A": "8", "B": "9", "C": "10", "D": "7"}, "resposta": "B"},
        {"pergunta": "Qual é a capital do Canadá?", "opcoes": {"A": "Toronto", "B": "Ottawa", "C": "Vancouver", "D": "Montreal"}, "resposta": "B"},
        {"pergunta": "Quem descobriu a gravidade?", "opcoes": {"A": "Einstein", "B": "Kepler", "C": "Newton", "D": "Galileu"}, "resposta": "C"},
        {"pergunta": "Em qual continente está o Egito?", "opcoes": {"A": "Ásia", "B": "Europa", "C": "América", "D": "África"}, "resposta": "D"}
    ],
    "dificil_11": [
        {"pergunta": "Qual é o elemento químico de símbolo 'Au'?",
         "opcoes": {"A": "Prata", "B": "Ouro", "C": "Cobre", "D": "Alumínio"}, "resposta": "B"},
        {"pergunta": "Qual é a capital da Austrália?",
         "opcoes": {"A": "Sydney", "B": "Melbourne", "C": "Canberra", "D": "Brisbane"}, "resposta": "C"},
        {"pergunta": "Quem escreveu 'A Divina Comédia'?",
         "opcoes": {"A": "Dante Alighieri", "B": "Shakespeare", "C": "Homero", "D": "Maquiavel"}, "resposta": "A"},
        {"pergunta": "Qual país tem a maior população do mundo?",
         "opcoes": {"A": "Índia", "B": "China", "C": "EUA", "D": "Indonésia"}, "resposta": "B"},
        {"pergunta": "Qual a capital da Islândia?",
         "opcoes": {"A": "Oslo", "B": "Reykjavik", "C": "Helsinque", "D": "Estocolmo"}, "resposta": "B"}
    ],
    "dificil_12": [
        {"pergunta": "Qual é o maior osso do corpo humano?",
         "opcoes": {"A": "Fêmur", "B": "Tíbia", "C": "Úmero", "D": "Crânio"}, "resposta": "A"},
        {"pergunta": "Quantos cromossomos tem o ser humano?", "opcoes": {"A": "42", "B": "46", "C": "48", "D": "44"},
         "resposta": "B"},
        {"pergunta": "Qual é a unidade de medida da força?",
         "opcoes": {"A": "Joule", "B": "Pascal", "C": "Newton", "D": "Watt"}, "resposta": "C"},
        {"pergunta": "Quem criou a teoria da relatividade?",
         "opcoes": {"A": "Einstein", "B": "Newton", "C": "Tesla", "D": "Bohr"}, "resposta": "A"},
        {"pergunta": "Qual país tem mais vulcões ativos?",
         "opcoes": {"A": "Itália", "B": "Japão", "C": "Indonésia", "D": "Chile"}, "resposta": "C"}
    ],
    "dificil_13": [
        {"pergunta": "Qual a velocidade da luz no vácuo?",
         "opcoes": {"A": "3x10^6 m/s", "B": "3x10^8 m/s", "C": "1x10^7 m/s", "D": "3x10^5 m/s"}, "resposta": "B"},
        {"pergunta": "Qual oceano banha o Japão?",
         "opcoes": {"A": "Índico", "B": "Atlântico", "C": "Ártico", "D": "Pacífico"}, "resposta": "D"},
        {"pergunta": "Quem foi Marie Curie?",
         "opcoes": {"A": "Bióloga", "B": "Química e física", "C": "Astrônoma", "D": "Engenheira"}, "resposta": "B"},
        {"pergunta": "Qual é o nome da molécula do sal de cozinha?",
         "opcoes": {"A": "NaCl", "B": "CO2", "C": "C6H12O6", "D": "HCl"}, "resposta": "A"},
        {"pergunta": "Em qual continente está a Ucrânia?",
         "opcoes": {"A": "Ásia", "B": "Europa", "C": "América", "D": "África"}, "resposta": "B"}
    ],
    "dificil_14": [
        {"pergunta": "Quem escreveu 'Crime e Castigo'?",
         "opcoes": {"A": "Tolstói", "B": "Dostoiévski", "C": "Kafka", "D": "Pasternak"}, "resposta": "B"},
        {"pergunta": "Qual é o menor osso do corpo humano?",
         "opcoes": {"A": "Estribo", "B": "Fíbula", "C": "Esfenoide", "D": "Lacrimal"}, "resposta": "A"},
        {"pergunta": "Qual o nome da estrela mais próxima da Terra?",
         "opcoes": {"A": "Proxima Centauri", "B": "Sirius", "C": "Sol", "D": "Betelgeuse"}, "resposta": "C"},
        {"pergunta": "Qual filósofo escreveu 'A República'?",
         "opcoes": {"A": "Platão", "B": "Sócrates", "C": "Aristóteles", "D": "Descartes"}, "resposta": "A"},
        {"pergunta": "Qual o rio mais extenso do mundo?",
         "opcoes": {"A": "Nilo", "B": "Amazonas", "C": "Yangtzé", "D": "Mississippi"}, "resposta": "B"}
    ],
    "dificil_15": [
        {"pergunta": "O que significa DNA?",
         "opcoes": {"A": "Ácido desoxirribonucléico", "B": "Dado natural ácido", "C": "Ácido nucleico puro",
                    "D": "Duplicador natural de aminoácido"}, "resposta": "A"},
        {"pergunta": "Qual é a fórmula da velocidade média?",
         "opcoes": {"A": "v = d/t", "B": "v = m/a", "C": "v = f×λ", "D": "v = E/t"}, "resposta": "A"},
        {"pergunta": "Quem pintou o teto da Capela Sistina?",
         "opcoes": {"A": "Da Vinci", "B": "Rafael", "C": "Michelangelo", "D": "Caravaggio"}, "resposta": "C"},
        {"pergunta": "Quantos planetas têm o sistema solar?", "opcoes": {"A": "7", "B": "8", "C": "9", "D": "10"},
         "resposta": "B"},
        {"pergunta": "Qual é o idioma mais falado no mundo?",
         "opcoes": {"A": "Inglês", "B": "Espanhol", "C": "Chinês mandarim", "D": "Hindi"}, "resposta": "C"}
    ],
        "muito_dificil_16": [
        {"pergunta": "Quem formulou a Teoria do Big Bang?", "opcoes": {"A": "Stephen Hawking", "B": "Georges Lemaître", "C": "Albert Einstein", "D": "Isaac Newton"}, "resposta": "B"},
        {"pergunta": "Qual a equação da segunda lei de Newton?", "opcoes": {"A": "F = m/a", "B": "E = mc²", "C": "F = m×a", "D": "P = mv"}, "resposta": "C"},
        {"pergunta": "Quem escreveu 'O Ser e o Nada'?", "opcoes": {"A": "Sartre", "B": "Nietzsche", "C": "Heidegger", "D": "Foucault"}, "resposta": "A"},
        {"pergunta": "Quantos elétrons cabem na camada K de um átomo?", "opcoes": {"A": "2", "B": "8", "C": "18", "D": "32"}, "resposta": "A"},
        {"pergunta": "Quem desenvolveu o modelo atômico de 1913?", "opcoes": {"A": "Bohr", "B": "Thomson", "C": "Rutherford", "D": "Dalton"}, "resposta": "A"}
    ],
    "muito_dificil_17": [
        {"pergunta": "Qual é o valor da constante de Planck?", "opcoes": {"A": "6,63×10⁻³⁴ J·s", "B": "3,00×10⁸ m/s", "C": "1,60×10⁻¹⁹ C", "D": "9,81 m/s²"}, "resposta": "A"},
        {"pergunta": "O que é o número de Avogadro?", "opcoes": {"A": "6,02×10²³", "B": "1,38×10⁻²³", "C": "3,14", "D": "9,1×10⁻³¹"}, "resposta": "A"},
        {"pergunta": "Quem escreveu 'Crítica da Razão Pura'?", "opcoes": {"A": "Kant", "B": "Hegel", "C": "Nietzsche", "D": "Descartes"}, "resposta": "A"},
        {"pergunta": "Qual cientista descobriu os raios X?", "opcoes": {"A": "Wilhelm Röntgen", "B": "Marie Curie", "C": "James Clerk Maxwell", "D": "Rutherford"}, "resposta": "A"},
        {"pergunta": "Qual é a função dos ribossomos nas células?", "opcoes": {"A": "Síntese de proteínas", "B": "Respiração celular", "C": "Digestão celular", "D": "Produção de energia"}, "resposta": "A"}
    ]
}

def salvar_pontuacao(nome, pontuacao):
    with open("ranking.csv", mode="a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, pontuacao, datetime.now().strftime("%d/%m/%Y %H:%M")])

def mostrar_ranking():
    try:
        with open("ranking.csv", "r", encoding="utf-8") as arquivo:
            linhas = list(csv.reader(arquivo))
            linhas.sort(key=lambda x: int(x[1]), reverse=True)
            top = "\n".join([f"{l[0]} - R$ {l[1]}" for l in linhas[:5]])
            messagebox.showinfo("Ranking", f"🏆 TOP 5 JOGADORES:\n\n{top}")
    except FileNotFoundError:
        messagebox.showinfo("Ranking", "Ainda não há pontuações salvas.")


def ajuda_cartas(opcoes, correta):
    erradas = [k for k in opcoes if k != correta]
    eliminadas = random.sample(erradas, 2)
    restantes = [l for l in opcoes if l not in eliminadas]
    return "\n".join([f"{l}) {opcoes[l]}" for l in restantes])

def ajuda_universitarios(correta):
    sugestao = correta if random.random() < 0.8 else random.choice([l for l in "ABCD" if l != correta])
    return f"Acho que a resposta é: {sugestao}"

def ajuda_plateia(correta):
    porcentagens = {"A": 0, "B": 0, "C": 0, "D": 0}
    correta_chance = random.randint(60, 80)
    restantes = [l for l in "ABCD" if l != correta]
    restantes_chances = sorted([random.randint(5, 20) for _ in range(3)])
    random.shuffle(restantes)
    porcentagens[correta] = correta_chance
    for letra, chance in zip(restantes, restantes_chances):
        porcentagens[letra] = chance
    return "\n".join([f"{l}) {porcentagens[l]}%" for l in "ABCD"])

class ShowDoMilhao:
    def __init__(self, root):
        self.root = root
        self.root.title("Show do Milhão")
        self.root.geometry("600x500")
        self.root.configure(bg=COR_PRIMARIA)

        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure("TButton", font=("Arial", 12), padding=10, background=COR_SECUNDARIA)

        self.frame = Frame(root, bg=COR_PRIMARIA)
        self.frame.pack(expand=True)

        self.label_titulo = Label(self.frame, text="SHOW DO MILHÃO", font=("Arial Black", 20), bg=COR_PRIMARIA, fg=COR_SECUNDARIA)
        self.label_titulo.pack(pady=20)

        self.botao_jogar = ttk.Button(self.frame, text="Jogar", command=self.iniciar_jogo)
        self.botao_jogar.pack(pady=10)

        self.botao_ranking = ttk.Button(self.frame, text="Ranking", command=mostrar_ranking)
        self.botao_ranking.pack(pady=10)

        self.botao_sair = ttk.Button(self.frame, text="Sair", command=root.quit)
        self.botao_sair.pack(pady=10)

    def iniciar_jogo(self):
        self.frame.destroy()
        self.nome_jogador = simpledialog.askstring("Nome", "Digite seu nome:")
        if not self.nome_jogador:
            self.root.quit()
        self.total = 0
        self.ajudas = {"cartas": True, "universitarios": True, "plateia": True}
        self.nivel = 1
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        if self.nivel > 17:
            messagebox.showinfo("Parabéns", f"🎉 {self.nome_jogador}, você venceu e ganhou R${self.total:,}!")
            salvar_pontuacao(self.nome_jogador, self.total)
            self.root.quit()
            return

        chave = nome_nivel(self.nivel)
        self.pergunta_atual = random.choice(perguntas_por_nivel.get(chave, []))
        if not self.pergunta_atual:
            messagebox.showwarning("Erro", "Sem perguntas disponíveis.")
            self.root.quit()
            return

        self.frame = Frame(self.root, bg=COR_PRIMARIA)
        self.frame.pack(expand=True, fill="both")

        label_nivel = Label(self.frame, text=f"Nível {self.nivel} – R$ {premios[self.nivel - 1]:,}", bg=COR_PRIMARIA, fg="white", font=("Arial", 14))
        label_nivel.pack(pady=10)

        label_pergunta = Label(self.frame, text=self.pergunta_atual["pergunta"], bg=COR_PRIMARIA, fg="white", font=("Arial", 16), wraplength=500)
        label_pergunta.pack(pady=20)

        for letra, opcao in self.pergunta_atual["opcoes"].items():
            btn = ttk.Button(self.frame, text=f"{letra}) {opcao}", command=lambda l=letra: self.verificar_resposta(l))
            btn.pack(pady=5)

        ajuda_frame = Frame(self.frame, bg=COR_PRIMARIA)
        ajuda_frame.pack(pady=10)
        for tipo in ["cartas", "universitarios", "plateia"]:
            if self.ajudas[tipo]:
                btn = ttk.Button(ajuda_frame, text=tipo.upper(), command=lambda t=tipo: self.usar_ajuda(t))
                btn.pack(side=LEFT, padx=5)

    def usar_ajuda(self, tipo):
        correta = self.pergunta_atual["resposta"]
        opcoes = self.pergunta_atual["opcoes"]
        if tipo == "cartas":
            msg = ajuda_cartas(opcoes, correta)
        elif tipo == "universitarios":
            msg = ajuda_universitarios(correta)
        elif tipo == "plateia":
            msg = ajuda_plateia(correta)
        else:
            return

        self.ajudas[tipo] = False
        messagebox.showinfo("Ajuda", msg)

    def verificar_resposta(self, resposta):
        correta = self.pergunta_atual["resposta"]
        if resposta == correta:
            self.total = premios[self.nivel - 1]
            self.nivel += 1
            self.frame.destroy()
            self.mostrar_pergunta()
        else:
            messagebox.showinfo("Fim de jogo", f"❌ Errado! A resposta era '{correta}'.\nVocê ganhou R${self.total:,}.")
            salvar_pontuacao(self.nome_jogador, self.total)
            self.root.quit()

root = Tk()
app = ShowDoMilhao(root)
root.mainloop()
