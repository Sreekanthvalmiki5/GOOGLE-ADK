import requests
def get_weather(city:str)->str:
    endpoint="https://wttr.in"
    response=requests.get(f"{endpoint}/{city}")
    return response.text