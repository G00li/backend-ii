import asyncio
import time
from typing import Callable, Any
from functools import wraps

class RateLimiter:
    def __init__(self, max_calls: int, time_period: float):
        """
        Inicializa o limitador de taxa.
        
        Args:
            max_calls: Número máximo de chamadas permitidas no período
            time_period: Período de tempo em segundos
        """
        self.max_calls = max_calls
        self.time_period = time_period
        self.calls = []
        self.lock = asyncio.Lock()

    async def acquire(self):
        """
        Adquire permissão para executar uma chamada.
        Aguarda se necessário até que uma chamada possa ser feita.
        """
        async with self.lock:
            now = time.time()
            
            # Remove chamadas antigas
            self.calls = [call_time for call_time in self.calls 
                         if now - call_time < self.time_period]
            
            if len(self.calls) >= self.max_calls:
                # Calcula o tempo de espera necessário
                sleep_time = self.calls[0] + self.time_period - now
                if sleep_time > 0:
                    await asyncio.sleep(sleep_time)
                    return await self.acquire()
            
            self.calls.append(now)

def rate_limit(max_calls: int, time_period: float):
    """
    Decorator para limitar a taxa de chamadas de uma função assíncrona.
    
    Args:
        max_calls: Número máximo de chamadas permitidas no período
        time_period: Período de tempo em segundos
    """
    limiter = RateLimiter(max_calls, time_period)
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            await limiter.acquire()
            return await func(*args, **kwargs)
        return wrapper
    return decorator

# Exemplo de uso
@rate_limit(max_calls=2, time_period=1.0)
async def example_task(task_id: int):
    print(f"Executando tarefa {task_id}")
    await asyncio.sleep(0.5)
    print(f"Tarefa {task_id} concluída")

async def main():
    # Executa 5 tarefas com limite de 2 chamadas por segundo
    tasks = [example_task(i) for i in range(5)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main()) 