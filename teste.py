

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
@app.route("/fases/fase3")
def fase3():
    return render_template("fase3.html")


if __name__ == "__main__":
    app.run(debug=True)