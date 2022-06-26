"""Baseado no exemplo do autor do módulo elsapy"""

import csv
from elsapy.elsclient import ElsClient
from elsapy.elsdoc import FullDoc
import json

## Carregar configurações
arquivo_configuracao = open("config.json")
config = json.load(arquivo_configuracao)
arquivo_configuracao.close()

## Inicializar cliente
cliente = ElsClient(config['apikey'])

## ScienceDirect (full-text) Recuperação de documento utilizando DOI
doi_doc = FullDoc(doi = '10.1016/j.commatsci.2022.111487')
if doi_doc.read(cliente):
    with open('data.txt', 'w') as f:
        f.write(doi_doc.title)
    print ("doi_doc.title: ", doi_doc.title)
    doi_doc.write()   
else:
    print ("Read document failed.")
