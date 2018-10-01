Guia de início rápido
=====================

GitHub
------

Baixe o projeto do GitHub: https://github.com/bmorais21/sao



Pré-requisitos
--------------

Requerimentos
*************

**Atenção!** É necessário instalar os pré-requistos, favor leia :doc:`requirements` primeiro!

Migração
********

Para utilizar o projeto, é necessário executar o arquivo *migrations.sh*::

    $ ./migrations.sh

Este arquivo contém os comandos *makemigrations* e *migrate*, necessários para criação e migração do banco de dados.

Tradução
********

Para ativar a tradução do site, é necessário executar o arquivo *translate.sh*::

    $ ./translate.sh

População
*********

O sistema conta com arquivos de população da base de dados. Para utilizá-los, basta executar o arquivo *populate.sh*::

    $./populate.sh

Pronto :D
---------

O sistema está pronto para utilização, basta rodar o comando::

    $ python manage.py runserver
