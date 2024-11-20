from flask import Flask,render_template,url_for,request


app = Flask(__name__,template_folder="templates")

#rota raiz
@app.route("/")
def homepage():
    return render_template("index.html")


#rota das fases
@app.route("/fases")
def fases():
    return render_template("fases.html")

# Rota da fase1
@app.route("/fases/fase1", methods=["GET", "POST"])
def fase1():
    # Dados do Quiz
    quiz_data = [
        {"question": "Para começar a fazer um programa, é necessário que se entenda a lógica de como ele funciona. Assim como uma receita de bolo, você deve construir uma sequência de ações para chegar no resultado final (o bolo). Como você faria a receita de um bolo?",
         "options": ["assar, preparar, separar ingredientes, comer", "preparar, separar ingredientes, assar, comer", "separar ingredientes, preparar, assar, comer","comer, preparar, assar, separar ingredientes"],
         "answer": "separar ingredientes, preparar, assar, comer"},




        {"question": "Existem algumas estruturas lógicas na programação que vão nos ajudar com isso. Por exemplo, SE não haver fermentos na separação dos ingredientes ENTÃO bolo não irá crescer SENÃO bolo irá ficar fofinho. Qual estrutura lógica seria essa?",
         "options": ["if...else... (condicional)", "while (repetição)", "for (repetição)","do-while (repetição)"],
         "answer": "if...else... (condicional)"},




        {"question": "Além disso, possuímos estruturas de looping, para que o programa execute a mesma tarefa a quantidade de vezes desejada, utilizando-se um for, while, do-while, entre outras. Qual alternativa se aplicaria para a utilização dessa estrutura?",
         "options": ["SE o ônibus atrasar ENTÃO perderei a aula", "ESCOLHER as opções do menu de um restaurante", "ir todo dia a escola ENQUANTO eu não me formar","SE eu passar no vestibular ENTAO entrarei na faculdade SENAO farei cursinho."],
         "answer": "ir todo dia a escola ENQUANTO eu não me formar"},


        {"question": "Na programação, possuímos \"variáveis\", que são espaços reservados para guardar alguma informação específica. Por exemplo, se eu perguntar ao usuário sua idade e quiser exibí-la depois, guardarei ela em uma variável. Na matemática, o que podemos dizer que se comporta como variáveis?",
         "options": ["Ângulos agudos", "Incógnitas", "Operação de soma","Medida dos lados de um triângulo"],
         "answer": "Incógnitas"}
    ]


    if request.method == "POST":
        # Obter respostas enviadas pelo usuário
        user_answers = [request.form.get(f"answer{i}") for i in range(len(quiz_data))]

        # Contar respostas corretas
        correct_answers = sum(1 for i, question in enumerate(quiz_data) if user_answers[i] == question["answer"])

        # Mensagem de feedback
        message = "Parabéns! Você passou na Fase 1!" if correct_answers == len(quiz_data) else "Tente novamente. Responda todas as questões corretamente!"
        return render_template("fase1.html", quiz_data=quiz_data, message=message, enumerate=enumerate)

    return render_template("fase1.html", quiz_data=quiz_data, enumerate=enumerate)


#rota da fase2
@app.route("/fases/fase2")
def fase2():
    return render_template("fase2.html")

#rota da fase3
@app.route("/fases/fase3",methods=["GET", "POST"])
def fase3():
    questions = [
        {
            "question": "O que é uma variável em programação?",
            "options": [
                "Um tipo de dado fixo",
                "Um espaço na memória para armazenar valores",
                "Um comando para executar um programa",
                "Nenhuma das alternativas"
            ],
            "answer": "Um espaço na memória para armazenar valores"
        },
        {
            "question": "Qual destas é uma estrutura de repetição?",
            "options": [
                "if-else",
                "while",
                "print",
                "return"
            ],
            "answer": "while"
        },
        {
            "question": "O que significa 'debugar' um código?",
            "options": [
                "Executar o código para ver o resultado",
                "Escrever comentários no código",
                "Encontrar e corrigir erros no código",
                "Apagar linhas de código desnecessárias"
            ],
            "answer": "Encontrar e corrigir erros no código"
        },
        {
            "question": "O que é um algoritmo?",
            "options": [
                "Um tipo de dado usado em Java",
                "Uma sequência de passos para resolver um problema",
                "Uma função específica em Python",
                "Um erro no programa"
            ],
            "answer": "Uma sequência de passos para resolver um problema"
        },
        {
            "question": "Qual é o propósito de um comentário no código?",
            "options": [
                "Melhorar o desempenho do código",
                "Ajudar o programador a documentar o que o código faz",
                "Substituir linhas de código desnecessárias",
                "Esconder erros no programa"
            ],
            "answer": "Ajudar o programador a documentar o que o código faz"
        }
    ]

    if request.method == 'POST':
        # Process the quiz submission
        total_corretas = 0
        message = "Tente novamente. Responda todas as questões corretamente!"

        for idx, question in enumerate(questions):
            selected_option = request.form.get(f'question-{idx}')
            if selected_option == question['answer']:
                total_corretas +=1

        if total_corretas == 5:
            return render_template('result.html', total=len(questions)) # tirei o score = score
        else:
            return render_template('fase3.html', questions=questions,enumerate=enumerate,message=message)

    return render_template('fase3.html', questions=questions,enumerate=enumerate)


if __name__ == "__main__":
    app.run(debug=True)