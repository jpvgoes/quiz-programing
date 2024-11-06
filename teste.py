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
        {"question": "Qual linguagem é usada para estilizar páginas web?", "options": ["CSS", "Python", "HTML"],
         "answer": "CSS"},
        {"question": "Qual a linguagem principal para interatividade em páginas web?",
         "options": ["JavaScript", "HTML", "C++"], "answer": "JavaScript"},
        {"question": "Python é uma linguagem...", "options": ["Compilada", "Interpretada", "Marcada"],
         "answer": "Interpretada"}
    ]


    if request.method == "POST":
        # Obter respostas enviadas pelo usuário
        user_answers = [request.form.get(f"answer{i}") for i in range(len(quiz_data))]

        # Contar respostas corretas
        correct_answers = sum(1 for i, question in enumerate(quiz_data) if user_answers[i] == question["answer"])

        # Mensagem de feedback
        message = "Parabéns! Você passou em todas as fases!" if correct_answers == len(quiz_data) else "Tente novamente. Responda todas as questões corretamente!"
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
            "question": "What does HTML stand for?",
            "options": ["Hyper Text Markup Language", "High Text Markup Language", "Hyper Tabular Markup Language",
                        "None of these"],
            "answer": "Hyper Text Markup Language"
        },
        {
            "question": "Which language is used for styling web pages?",
            "options": ["HTML", "CSS", "JavaScript", "PHP"],
            "answer": "CSS"
        },
        {
            "question": "Which is not a programming language?",
            "options": ["Python", "Java", "HTML", "C++"],
            "answer": "HTML"
        }
    ]
    if request.method == 'POST':
        # Process the quiz submission
        score = 0
        for idx, question in enumerate(questions):
            selected_option = request.form.get(f'question-{idx}')
            if selected_option == question['answer']:
                score +=1
        return render_template('result.html', score=score, total=len(questions))

    return render_template('fase3.html', questions=questions,enumerate=enumerate)


if __name__ == "__main__":
    app.run(debug=True)