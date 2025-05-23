from crewai import Agent

def test_agent_response():
    agent = Agent(name="AgenteSimples")
    resposta = agent.respond("Olá!")
    assert isinstance(resposta, str) 