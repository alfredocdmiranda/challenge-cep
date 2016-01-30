# -*- coding: utf-8 -*-

import json

import requests
import restless
from restless.tnd import TornadoResource
from restless.preparers import FieldsPreparer
from restless.constants import *

from models import session, Endereco

API_URL = "http://api.postmon.com.br/v1/cep/"

def to_json(endereco):
    return {'cep': endereco.cep, 'logradouro': endereco.logradouro, 
            'bairro': endereco.bairro, 'cidade': endereco.cidade, 
            'estado': endereco.estado}

class CEPResource(TornadoResource):
    def __init__(self, *args, **kwargs):
         super(TornadoResource, self).__init__(*args, **kwargs)
    
    def is_authenticated(self):
        return True
    
    def list(self):
        address_list = [] 
        if 'limit' in self.data:
            query = session.query(Endereco).limit(self.data['limit'])
        else:
            query = query = session.query(Endereco)
        
        for q in query:
            address_list.append(to_json(q))
        
        return address_list

    def detail(self, pk):
        endereco = session.query(Endereco).get(pk)
        if endereco:
            return to_json(endereco)
        else:
            raise restless.exceptions.NotFound(u"CEP não encontrado.")

    def create(self):
        cep = self.data['cep']
        req = requests.get(API_URL+cep)

        if req.status_code == 200:
            addr = json.loads(req.text)
            new_addr = Endereco(logradouro=addr['logradouro'],
                                bairro=addr['bairro'],
                                cidade=addr['cidade'],
                                estado=addr['estado'],
                                cep=addr['cep'])
            
            session.add(new_addr)
            session.commit()
        elif req.status_code == 404:
            raise restless.exceptions.NotFound(u"CEP inválido.")

    def update(self, pk):
        endereco = session.query(Endereco).get(pk)
        if endereco:
            for d in self.data:
                if hasattr(endereco, d):
                    setattr(endereco, d, self.data[d])
        else:
            raise restless.exceptions.NotFound(u"CEP não encontrado.")

    def delete(self, pk):
        endereco = session.query(Endereco).filter(Endereco.cep==pk)[0]
        session.delete(endereco)
        session.commit()
