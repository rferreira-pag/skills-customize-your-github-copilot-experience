# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprender a criar e estruturar uma API REST utilizando o framework FastAPI em Python. O estudante irá construir endpoints básicos, manipular dados e testar a API localmente.

## 📝 Tarefas

### 🛠️ Criar Estrutura Básica da API

#### Description
Inicie um projeto FastAPI e crie um endpoint GET simples que retorna uma mensagem de boas-vindas.

#### Requirements
Completed program should:

- Iniciar um app FastAPI básico
- Criar endpoint GET `/` que retorna um JSON com mensagem de boas-vindas
- Rodar localmente usando Uvicorn


### 🛠️ CRUD de Itens

#### Description
Implemente endpoints para criar, listar, atualizar e deletar itens em memória (CRUD).

#### Requirements
Completed program should:

- Criar modelo de dados para "Item" (ex: nome, descrição, preço)
- Implementar endpoints POST, GET, PUT, DELETE para manipular itens
- Armazenar itens em uma lista em memória
- Retornar respostas apropriadas para cada operação

### 🛠️ Documentação Interativa

#### Description
Utilize os recursos automáticos de documentação do FastAPI.

#### Requirements
Completed program should:

- Permitir acesso à documentação Swagger em `/docs`
- Permitir acesso à documentação Redoc em `/redoc`
