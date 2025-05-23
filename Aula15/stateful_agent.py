from crewai import Agent
import requests

class WeatherAgent(Agent):
    def __init__(self, name):
        super().__init__(name)
    
    def respond(self, query):
        if "clima" in query.lower():
            # Exemplo: API pública de clima (Open-Meteo)
            resp = requests.get("https://api.open-meteo.com/v1/forecast?latitude=38.72&longitude=-9.13&current_weather=true")
            if resp.status_code == 200:
                temp = resp.json()["current_weather"]["temperature"]
                return f"Temperatura atual em Lisboa: {temp}°C"
            return "Não foi possível obter o clima."
        return "Pergunta não reconhecida."

def main():
    agent = WeatherAgent("AgenteClima")
    print(agent.respond("Qual o clima em Lisboa?"))

if __name__ == "__main__":
    main() 