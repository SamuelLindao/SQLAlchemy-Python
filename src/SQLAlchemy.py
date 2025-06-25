from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer,  primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo


class Livro(Base):
    __tablename__ = "livros"
    id = Column("id", Integer, primary_key=True,autoincrement=True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id"))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono


Base.metadata.create_all(bind=db)

#CRUD


#Create
# usuario = Usuario(nome='lira', email = 'qlqcoisa@email.com', senha = '123')
# session.add(usuario)
# session.commit()

#Read
usuario_lira = session.query(Usuario).filter_by(email = 'qlqcoisa@email.com').first()

# livro = Livro(titulo="Nome do Vento", qtde_paginas=1000, dono=usuario_lira.id)
# session.add(livro)
# session.commit()

#Update
usuario_lira.nome = "SamuelRx"
session.add(usuario_lira)
session.commit()

#Delete
session.delete(usuario_lira)
session.commit()