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

### Testes de Aceitação (TA)

| Código        | Descrição
|---------------|----------
| **TA01.01** | O gerente informa na tela de cadastrar produto, todos os dados que são pedidos e ao clicar em salvar uma mensagem de sucesso é mostrada. Mensagem: Produto cadastrado com sucesso!
| **TA01.02** | O gerente informa na tela de cadastrar produto os dados incorretamente, ao clicar em salvar ele é informado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente!

## User Story US02 - Manter Gerente

|               |                             |
|---------------|-----------------------------|
| **Descrição** | O sistema deve manter um cadastro de gerentes, onde o perfil poderá ser criado por outro gerente. Um gerente tem os atributos, id, nome, email, data de nascimento, endereço e cpf.

Requisitos Envolvidos   |               |
------------------------|---------------|
RF005                   | Adicionar Gerente
RF006                   | Alterar Gerente
RF007                   | Excluir Gerente
RF008                   | Listar Gerente

|         |                                   |
| --------|-----------------------------------|
| **Prioridade**            | Essencial
| **Estimativa**            | 8 h
| **Tempo Gasto (real):**   |
| **Tamanho Funcional**     | 7 PF

### Testes de Aceitação (TA)

| Código        | Descrição
|---------------|----------
| **TA02.01** | O gerente informa na tela de cadastrar um novo gerente, todos os dados que são pedidos e ao clicar em salvar uma mensagem de sucesso é mostrada. Mensagem: Gerente cadastrado com sucesso!
| **TA02.02** | O gerente informa na tela de cadastrar um novo gerente com os dados incorretos, ao clicar em salvar ele é informado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente!
| **TA02.03** | O gerente informa na tela de cadastrar um novo gerente com os dados existentes, ao clicar em salvar ele é informado com uma mensagem de erro. Mensagem: Cadastro não realizado, o gerente que você está tentando cadastrar já existe!
| **TA02.04** | O gerente clica em excluir um outro gerente ele é informado por um alerta se realmente quer excluir o gerente selecionado, se clicar em sim irá aparecer uma mensagem de sucesso. Mensagem: Gerente excluído com sucesso!
| **TA02.05** | O gerente não pode excluir o próprio cadastro se só tiver ele. Mensagem: Você não pode excluir sua conta, o sistema precisa de no mínimo um gerente!

## User Story US03 - Manter Vendedor

|               |                             |
|---------------|-----------------------------|
| **Descrição** | O sistema deve manter um cadastro de vendedores, onde o perfil poderá ser criado por um gerente. Um vendedor tem os atributos, id, nome, email, data de nascimento, endereço e cpf.

Requisitos Envolvidos   |               |
------------------------|---------------|
RF009                   | Adicionar Vendedor
RF010                   | Alterar Vendedor
RF011                   | Excluir Vendedor
RF012                   | Listar Vendedor

|         |                                   |
| --------|-----------------------------------|
| **Prioridade**            | Essencial
| **Estimativa**            | 8 h
| **Tempo Gasto (real):**   |
| **Tamanho Funcional**     | 7 PF

### Testes de Aceitação (TA)

| Código        | Descrição
|---------------|----------
| **TA03.01** | O gerente informa na tela de cadastrar um novo vendedor, todos os dados que são pedidos e ao clicar em salvar uma mensagem de sucesso é mostrada. Mensagem: Vendedor cadastrado com sucesso!
| **TA03.02** | O gerente informa na tela de cadastrar um novo vendedor com os dados incorretos, ao clicar em salvar ele é informado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente!
| **TA03.03** | O gerente informa na tela de cadastrar um novo vendedor com os dados existentes, ao clicar em salvar ele é informado com uma mensagem de erro. Mensagem: Cadastro não realizado, o vendedor que você está tentando cadastrar já existe!
| **TA03.04** | O gerente clicar em excluir um vendedor ele é informado por um alerta se realmente quer excluir o vendedor selecionado, se clicar em sim irá aparecer uma mensagem de sucesso. Mensagem: Vendedor excluído com sucesso!

## User Story US04 - Abrir Caixa

|               |                             |
|---------------|-----------------------------|
| **Descrição** | O sistema deve abrir o caixa "zerado" para começar a receber os produtos e comtabilizar as vendas, onde o Caixa será aberto por um gerente.

Requisitos Envolvidos   |               |
------------------------|---------------|
RF013                   | Abrir Caixa

|         |                                   |
| --------|-----------------------------------|
| **Prioridade**            | Essencial
| **Estimativa**            | 8 h
| **Tempo Gasto (real):**   |
| **Tamanho Funcional**     | 7 PF

### Testes de Aceitação (TA)

| Código        | Descrição
|---------------|----------
| **TA04.01** | O gerente informa na tela de Caixa o caixa aberto, todos os dados que são pedidos e ao clicar em "Abrir" uma mensagem de sucesso é mostrada. Mensagem: Caixa aberto com sucesso!
| **TA04.02** | O gerente informa na tela de Caixa o caixa aberto, com os dados incorretos, ao clicar em "Abrir" ele é informado com uma mensagem de erro. Mensagem: Caixa não Aberto, o campo “xxxx” não foi informado corretamente!
| **TA04.03** | O gerente informa na tela de Caixa um caixa já aberto, ao clicar em "Abrir" ele é informado com uma mensagem de erro. Mensagem: O Caixa já está aberto!

## User Story US05 - Fechar Caixa

|               |                             |
|---------------|-----------------------------|
| **Descrição** | O sistema deve Fechar o caixa com o valor colocado inicialmente mais os das vendas feitas até aquele momento, onde o Caixa será fechado por um gerente.

Requisitos Envolvidos   |               |
------------------------|---------------|
RF014                   | Fechar Caixa

|         |                                   |
| --------|-----------------------------------|
| **Prioridade**            | Essencial
| **Estimativa**            | 8 h
| **Tempo Gasto (real):**   |
| **Tamanho Funcional**     | 7 PF

### Testes de Aceitação (TA)

| Código        | Descrição
|---------------|----------
| **TA05.01** | O gerente clica em "Fechar Caixa" na tela de Caixa. É informado data e hora de abertura e fechamento do caixa com o valor areecadado no período. Mensagem: Caixa aberto com sucesso!


## User Story US06 - Vender Produto

|               |                             |
|---------------|-----------------------------|
| **Descrição** | Ao colocar o código do produto na tela de venda ele irá identificar e mostrar os atributos e ao vendedor clicar em fechar venda o produto é retirado do estoque e adicionado ao cadastro do cliente.

Requisitos Envolvidos   |               |
------------------------|---------------|
RF015                   | Vender Produto

|         |                                   |
| --------|-----------------------------------|
| **Prioridade**            | Essencial
| **Estimativa**            | 8 h
| **Tempo Gasto (real):**   |
| **Tamanho Funcional**     | 7 PF

### Testes de Aceitação (TA)

| Código        | Descrição
|---------------|----------
| **TA06.01** | O vendedor informa na tela de venda o código do produto, todos os dados são mostrados na tela.
| **TA06.02** | O vendedor informa na tela de venda o código do produto errado, ao clicar em "Fechar Venda" ele é informado com uma mensagem de erro. Mensagem: Produto não cadastrado ou código errado!

