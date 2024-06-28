import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)



class vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    #hair_color = Column(String(250), nullable=False)



class planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    #hair_color = Column(String(250), nullable=False)





class usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)



class Favoritos_personajes(Base):
    __tablename__ = 'favoritos_personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
    #street_name = Column(String(250))
    #street_number = Column(String(250))
    #Personajes_relacion = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    personajes_relacion = Column(Integer, ForeignKey('personajes.id'),nullable = False)
    usuarios_relacion = Column(Integer, ForeignKey('usuarios.id'),nullable = False)
    Personajes = relationship(Personajes)
    usuarios = relationship(usuarios)


class Favoritos_vehiculos(Base):
    __tablename__ = 'favoritos_vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
    #street_name = Column(String(250))
    #street_number = Column(String(250))
    #Personajes_relacion = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    vehiculos_relacion = Column(Integer, ForeignKey('vehiculos.id'),nullable = False)
    usuarios_relacion = Column(Integer, ForeignKey('usuarios.id'),nullable = False)
    vehiculos = relationship(vehiculos)
    usuarios = relationship(usuarios)


class Favoritos_planetas(Base):
    __tablename__ = 'favoritos_planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
    #street_name = Column(String(250))
    #street_number = Column(String(250))
    #Personajes_relacion = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    planetas_relacion = Column(Integer, ForeignKey('planetas.id'),nullable = False)
    usuarios_relacion = Column(Integer, ForeignKey('usuarios.id'),nullable = False)
    planetas = relationship(planetas)
    usuarios = relationship(usuarios)
























    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
