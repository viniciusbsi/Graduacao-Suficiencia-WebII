Guia de início rápido
=====================

GitHub
------

Baixe o projeto do GitHub: https://github.com/viniciusbsi/web1.git



Pré-requisitos
--------------

Requerimentos
*************

**Atenção!** É necessário instalar os pré-requistos, favor leia o arquivo :doc:`requirements` antes de inicir a instalação!


Migração
********

Para utilizar o projeto, é necessário executar o arquivo *migrations.sh*::

    $ ./migrations.sh

Este arquivo contém os comandos *makemigrations* e *migrate*, necessários para criação e migração do banco de dados.

Tradução
********

Para ativar a tradução do site, é necessário executar o arquivo *translate.sh*::

    $ ./translate.sh


A instalação foi concluída !!
-----------------------------

O sistema está pronto para utilização, basta executá-lo com o comando::

    $ python manage.py runserver
