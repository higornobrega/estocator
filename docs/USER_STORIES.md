# Documento Lista de User Stories

## Histórico de revisões

Data        | Versão        | Descrição     | Autor
------------|---------------|---------------|------
30/03/2021  | 0.0.1         | Template e descrição do documento | Bruno de Souza

## User Story US01 - Manter Produto

|               |                             |
|---------------|-----------------------------|
| **Descrição** | O sistema deve manter um cadastro de produtos, onde um produto poderá ser vendido a um perfil cliente pelo perfil vendedor. Um produto tem os atributos, id, nome, marca, preço, quantidade e código.

Requisitos Envolvidos   |               |
------------------------|---------------|
RF001                   | Adicionar produtos
RF002                   | Alterar produtos
RF003                   | Excluir produtos
RF004                   | Listar produtos

|         |                                   |
| --------|-----------------------------------|
| **Prioridade**            | Essencial
| **Estimativa**            | 8 h
| **Tempo Gasto (real):**   |
| **Tamanho Funcional**     | 7 PF

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | O gerente informa na tela de cadastrar produto, todos os dados que são pedidos e ao clicar em salvar uma mensagem de sucesso é mostrada. Mensagem: Produto cadastrado com sucesso!
| **TA01.02** | O gerente informa na tela de cadastrar produto os dados incorretamente, ao clicar em salvar ele é informado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente!
