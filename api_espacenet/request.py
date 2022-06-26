import epo_ops

middlewares = [
    epo_ops.middlewares.Dogpile(),
    epo_ops.middlewares.Throttler(),
]

# Instancia cliente
client = epo_ops.Client(
    key = 'EmqeCDAwrYrYMMBFsZ9VydodZ0mlConQ', 
    secret = 'P5Cjct43cNdkjIYv',
    middlewares = middlewares)

resposta = client.published_data(  # Recupera dados bibliométricos
  reference_type = 'publication',  # publication, application, priority
  input = epo_ops.models.Docdb('1000000', 'EP', 'A1'),  # original, docdb, epodoc
  #endpoint = 'biblio',  # optional, defaults to biblio in case of published_data
  #constituents = []  # optional, list of constituents
)