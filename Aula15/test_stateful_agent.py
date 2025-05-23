from stateful_agent import WeatherAgent

def test_weather_agent():
    agent = WeatherAgent("AgenteClima")
    resposta = agent.respond("Qual o clima em Lisboa?")
    assert "Temperatura atual" in resposta or "Não foi possível obter o clima." in resposta 