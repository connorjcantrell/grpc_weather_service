import sys
sys.path.append('.')

import grpc
import json
import os
import requests
from concurrent import futures
import weather_pb2 
import weather_pb2_grpc


def get_weather(latitude, longitude, units='imperial'):

    API_KEY = os.environ.get('WEATHER_API_KEY')
    if not API_KEY:
        raise ValueError("No API key set. Please set the WEATHER_API_KEY environment variable.")

    endpoint = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&units={units}&appid={API_KEY}"
    
    try:
        resp = requests.get(endpoint)
        resp.raise_for_status()
        
        return resp.json()

    except requests.ConnectionError:
        raise Exception("There was a problem connecting to the Weather API.")

    except requests.Timeout:
        raise Exception("The request to the Weather API timed out.")

    except requests.HTTPError as http_err:
        raise Exception(f"HTTP error occurred: {http_err}")

    except requests.RequestException as req_err:
        raise Exception(f"An error occurred while fetching weather data: {req_err}")

    except json.JSONDecodeError:
        raise Exception("Failed to decode the response from the Weather API as JSON.")


class WeatherService(weather_pb2_grpc.WeatherServiceServicer):

    def GetCurrentWeather(self, weather_request, context):
        content = get_weather(
                weather_request.latitude, 
                weather_request.longitude
                )
        return weather_pb2.CurrentWeatherResponse(
                dt=content['current']['dt'],
                sunrise=content['current']['sunrise'],
                sunset=content['current']['sunset'],
                temperature=content['current']['temp'],
                pressure=content['current']['pressure'],
                humidity=content['current']['humidity'],
                dew_point=content['current']['dew_point'],
                uv_index=content['current']['uvi'],
                clouds=content['current']['clouds'],
                visibility=content['current']['visibility'],
                wind_speed=content['current']['wind_speed'],
                wind_degree=content['current']['wind_deg'],
                wind_gust=content['current'].get('wind_gust', 0.0),
                )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    weather_pb2_grpc.add_WeatherServiceServicer_to_server(WeatherService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

