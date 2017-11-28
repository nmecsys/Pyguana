pyguana
--------

Pacote que conecta o Python a API Iguana

Para utilizar, execute::

    >>> import pyguana
 
Inicialize a classe passando um token válido::

    >>> requisicao = pyguana.Iguana('token_valido')

Exemplo simples de requisição:

    >>> noticias = requisicao.get()
    >>> print(noticias)
