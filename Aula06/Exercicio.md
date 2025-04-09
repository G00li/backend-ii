# 🍽️ Restaurante Assíncrono com Prioridades, Alta Demanda e Registro de Pedidos

## 💼 Enunciado do Desafio

Você foi contratado para simular o sistema de pedidos de um restaurante digital durante um evento de alta demanda, como uma **Black Friday**. O sistema deve ser capaz de:

1. **Gerenciar múltiplos pedidos simultaneamente**.
2. **Priorizar clientes VIPs**.
3. **Cancelar pedidos que demoram demais para serem preparados**.
4. **Registrar o status de cada pedido em um "banco de dados" simulado.**

Essa simulação tem como objetivo treinar conceitos avançados de **concorrência assíncrona** com Python, preparando você para cenários reais de sistemas escaláveis.

---

## 🎯 Objetivos

- Criar um sistema de filas assíncronas com **prioridades**.
- Simular **alta concorrência** de pedidos.
- Cancelar tarefas automaticamente com **timeout**.
- Armazenar o resultado de cada pedido em um **banco simulado**.

---

## 🛠️ Tecnologias e Conceitos Utilizados

| Ferramenta / Conceito     | Utilidade |
|---------------------------|-----------|
| `asyncio` (Python 3.8+)   | Gerenciamento assíncrono de tarefas concorrentes. |
| `asyncio.PriorityQueue`   | Fila de pedidos com suporte a prioridades (VIPs). |
| `asyncio.create_task()`   | Criação de múltiplas tarefas simultâneas (cozinheiros). |
| `asyncio.wait_for()`      | Cancelamento de tarefas que ultrapassam um tempo limite. |
| `asyncio.sleep()`         | Simulação de tempo de espera realista (ex: preparo de pedidos). |
| Banco Simulado (`list`)   | Armazenamento temporário dos pedidos tratados (concluídos ou cancelados). |

---

## 📦 Requisitos

- Python 3.8 ou superior
- Biblioteca padrão `asyncio` (não é necessário instalar nada)
- Editor de código (VS Code, PyCharm ou outro)

---

## 📜 Como funciona?

- Pedidos VIP têm prioridade na fila.
- A alta demanda é simulada com dezenas de pedidos chegando em milissegundos.
- Cozinheiros processam os pedidos conforme a ordem de prioridade.
- Se o preparo ultrapassar um tempo limite, o pedido é automaticamente cancelado.
- Um banco de dados simulado registra o status final de cada pedido.

---

## 🧪 Extensões sugeridas (nível avançado)

- 💾 Persistir os dados em um **banco real** como SQLite (com SQLAlchemy ou Prisma para Python).
- 🌐 Criar uma **API com FastAPI** para consultar e inserir pedidos.
- 🧪 Implementar **testes assíncronos** com `pytest-asyncio`.
- 📊 Visualizar dados com gráficos (ex: tempo médio de preparo com Matplotlib).

---

## ✅ Resultado esperado

Ao rodar o código, você verá:

- Pedidos VIP sendo processados antes dos comuns.
- Cancelamentos automáticos de pedidos que demoraram demais.
- Impressão do status final de cada pedido com registro no "banco de dados" simulado.

---

## 🚀 Execute o projeto

```bash
python restaurante_async.py
