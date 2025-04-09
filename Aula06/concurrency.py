from asyncio import PriorityQueue
import asyncio
import random

# === CONFIGURAÇÕES === #
NUM_PEDIDOS = 50                # Alta demanda: muitos pedidos chegando rápido
NUM_COZINHEIROS = 3             # Quantidade de cozinheiros disponíveis
TIMEOUT = 5                     # Tempo máximo para preparar um pedido (segundos)
PRIORIDADE_VIP = 0              # Prioridade mais alta
PRIORIDADE_NORMAL = 1           # Prioridade mais baixa

# === FILA E BANCO SIMULADO === #
fila_de_pedidos: asyncio.PriorityQueue = asyncio.PriorityQueue()
banco_simulado = []  # Simula o banco de dados para registrar os pedidos

# === GERADOR DE PEDIDOS === #
async def gerar_pedidos():
    for i in range(1, NUM_PEDIDOS + 1):
        # Define se o pedido é VIP (20% de chance)
        prioridade = PRIORIDADE_VIP if random.random() < 0.2 else PRIORIDADE_NORMAL
        tipo = "VIP" if prioridade == PRIORIDADE_VIP else "Comum"

        # Coloca o pedido na fila com prioridade
        await fila_de_pedidos.put((prioridade, i))
        print(f"📥 Pedido {i} ({tipo}) entrou na fila com prioridade {prioridade}")

        # Simula chegada rápida dos pedidos (Black Friday)
        await asyncio.sleep(0.01)

# === COZINHEIRO (consumidor da fila) === #
async def cozinheiro(nome: str):
    while True:
        # Espera um pedido da fila
        prioridade, pedido_id = await fila_de_pedidos.get()

        try:
            # Simula tempo de preparo aleatório
            tempo = random.randint(1, 7)
            print(f"👨‍🍳 {nome} pegou Pedido {pedido_id} (leva {tempo}s)")

            # Aplica timeout para cancelar pedidos demorados
            await asyncio.wait_for(asyncio.sleep(tempo), timeout=TIMEOUT)

            print(f"✅ {nome} finalizou Pedido {pedido_id}")
            banco_simulado.append((pedido_id, "concluído", nome))

        except asyncio.TimeoutError:
            print(f"⏱️ {nome} cancelou Pedido {pedido_id} (demorou demais!)")
            banco_simulado.append((pedido_id, "cancelado", nome))

        fila_de_pedidos.task_done()  # Marca o pedido como resolvido

# === FUNÇÃO PRINCIPAL === #
async def main():
    print("🍽️ Restaurante abrindo... Pedidos chegando!")

    # Cria tarefa para gerar pedidos
    produtor = asyncio.create_task(gerar_pedidos())

    # Cria os cozinheiros
    cozinheiros = [
        asyncio.create_task(cozinheiro(f"Cozinheiro-{i+1}"))
        for i in range(NUM_COZINHEIROS)
    ]

    # Espera todos os pedidos serem gerados e processados
    await produtor
    await fila_de_pedidos.join()

    # Cancela os cozinheiros (loop infinito precisa ser interrompido)
    for c in cozinheiros:
        c.cancel()

    print("\n🏁 Restaurante fechou! Todos os pedidos foram tratados.")

    # Mostra os dados salvos no banco simulado
    print("\n📦 BANCO DE DADOS (simulado):")
    for pedido_id, status, nome_cozinheiro in sorted(banco_simulado):
        print(f"Pedido {pedido_id:02} - {status.upper():10} - por {nome_cozinheiro}")

# === EXECUTA O PROGRAMA === #
if __name__ == "__main__":
    asyncio.run(main())
