from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
db = SQLAlchemy()
db.init_app(app)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique = True)
    
    def __repr__(self):
        return f"<{self.nome}>"

"""class Paciente(db.Model):
    __tablename__ = 'pacientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique = True)
    
class Profissional(db.Model):
    __tablename__ = 'profissionais'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique = True)
    
class Consulta(db.Model):
    __tablename__ = 'consultas'
    
    id = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    id_profissional = db.Column(db.Integer, db.ForeignKey('profissional.id'), nullable=False)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    
    paciente = db.relationship('Paciente', foreign_keys=id_paciente)
    profissional = db.relationship('Profissional', foreign_keys=id_profissional)
"""""
@app.route('/')
def index():
    return 'Olá Mundo!'

if __name__ == '__main__':
    with app.app_context():
        usuarios = db.session.query(Usuario).all()
        for usuario in usuarios:
            print(usuario)
    app.run(debug=True)