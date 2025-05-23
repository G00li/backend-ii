from crewai import Agent

def main():
    agent = Agent(name="AgenteSimples")
    resposta = agent.respond("Olá!")
    print(resposta)

if __name__ == "__main__":
    main() 