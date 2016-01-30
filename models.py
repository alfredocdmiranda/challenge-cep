# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///challenge.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Endereco(Base):
    __tablename__ = "endereco"
    
    #id = Column(Integer, primary_key=True)
    logradouro = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    estado = Column(String)
    cep = Column(String, primary_key=True)
    __table_args__ = (UniqueConstraint('cep'),)
    
    def __repr__(self):
        return "{}".format(self.cep)

Base.metadata.create_all(engine)
