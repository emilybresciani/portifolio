from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.sqlite3"
app.secret_key = "crud_biblioteca_super_secreta_e_forte"
db = SQLAlchemy(app)

# Livro
class Livro(db.Model):
    __tablename__ = "livro"
    id_livro = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(250), nullable=False)
    autor = db.Column(db.String(120), nullable=False)
    idioma = db.Column(db.String(40), nullable=False)
    npag = db.Column(db.Integer, nullable=False)

    def __init__(self, titulo, descricao, autor, idioma, npag):
        self.titulo = titulo
        self.descricao = descricao
        self.autor = autor
        self.idioma = idioma
        self.npag = npag

# Rota inicial
@app.route("/")
def principal():
    return render_template("index.html")

# Listagem paginada de livros
@app.route("/listar")
def listar():
    page = request.args.get("page", 1, type=int)
    per_page = 3
    livros_paginados = Livro.query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template("listar.html", livros=livros_paginados)

# Cadastro de novo livro
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        autor = request.form.get("autor")
        idioma = request.form.get("idioma")
        npag_str = request.form.get("npag")

        if not titulo or not descricao or not autor or not idioma or not npag_str:
            flash("Todos os campos devem ser preenchidos!", "danger")
        else:
            try:
                npag = int(npag_str)
                if npag <= 0:
                    flash("O número de páginas deve ser um número positivo!", "danger")
                else:
                    novo_livro = Livro(titulo, descricao, autor, idioma, npag)
                    db.session.add(novo_livro)
                    db.session.commit()
                    flash("Livro cadastrado com sucesso!", "success")
                    return redirect(url_for("listar"))
            except ValueError:
                flash("Número de páginas inválido. Insira um número inteiro.", "danger")
            except Exception as e:
                db.session.rollback()
                flash(f"Ocorreu um erro ao cadastrar o livro: {e}", "danger")

    return render_template("cadastrar.html")

# Exclusão de livro
@app.route("/excluir/<int:id_livro>", methods=["GET", "POST"])
def excluir(id_livro):
    livro = Livro.query.get(id_livro)

    if livro:
        try:
            db.session.delete(livro)
            db.session.commit()
            flash("Livro excluído com sucesso!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Erro ao excluir o livro: {e}", "danger")
    else:
        flash("Livro não encontrado para exclusão.", "warning")

    return redirect(url_for("listar"))

# Edição de livro
@app.route("/editar/<int:id_livro>", methods=["GET", "POST"])
def editar(id_livro):
    livro = Livro.query.get(id_livro)

    if not livro:
        flash("Livro não encontrado para edição.", "warning")
        return redirect(url_for("listar"))

    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        autor = request.form.get("autor")
        idioma = request.form.get("idioma")
        npag_str = request.form.get("npag")

        if not titulo or not descricao or not autor or not idioma or not npag_str:
            flash("Todos os campos devem ser preenchidos!", "danger")
        else:
            try:
                npag = int(npag_str)
                if npag <= 0:
                    flash("O número de páginas deve ser um número positivo!", "danger")
                else:
                    livro.titulo = titulo
                    livro.descricao = descricao
                    livro.autor = autor
                    livro.idioma = idioma
                    livro.npag = npag
                    db.session.commit()
                    flash("Livro atualizado com sucesso!", "success")
                    return redirect(url_for("listar"))
            except ValueError:
                flash("Número de páginas inválido. Insira um número inteiro.", "danger")
            except Exception as e:
                db.session.rollback()
                flash(f"Ocorreu um erro ao atualizar o livro: {e}", "danger")

    return render_template("editar.html", livro=livro)

# Inicialização da aplicação
if __name__ == "__main__":
    # Cria as tabelas no banco caso ainda não existam
    with app.app_context():
        db.create_all()

    # Inicia o servidor Flask em modo de desenvolvimento
    app.run(debug=True)
