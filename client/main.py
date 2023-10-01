import sys
sys.path.append('.')

import grpc
import weather_pb2
import weather_pb2_grpc


def run(lat, lon):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = weather_pb2_grpc.WeatherServiceStub(channel)
        response = stub.GetCurrentWeather(weather_pb2.WeatherRequest(
            latitude=lat, 
            longitude=lon
            )
        )
        print(f"Weather: {response}")


if __name__ == "__main__":
    """
    Prompt the user for geocoordinates and return them as floats.

    Returns:
        tuple: A tuple containing latitude and longitude as floats.
    """
    try:
        # Provide a more detailed prompt
        coordinates = input("Enter geocoordinates as 'latitude,longitude' (e.g. 37.4979,-122.2663): ")
        lat, lon = coordinates.split(',')
        lat, lon = lat.strip(), lon.strip()
    
    except ValueError:
        # Handles both split error (not enough values to unpack) and float conversion error
        print("Invalid input. Please provide valid geocoordinates.")

    run(lat, lon)

