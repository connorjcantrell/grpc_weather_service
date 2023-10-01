# gRPC Weather Service

A gRPC service that provides current weather data based on provided geocoordinates. This service fetches data from the OpenWeatherMap API and delivers it to clients via a gRPC interface.

## Features

- **GetCurrentWeather**: An RPC call that returns current weather details for a given latitude and longitude.
- Uses OpenWeatherMap API for accurate and real-time weather data.
- Built-in error handling for various scenarios like invalid geocoordinates, network errors, etc.
- Easily extensible to support more features like forecasts, historical data, etc.

## Prerequisites

- Python 3.8+
- gRPC and Protocol Buffers
- OpenWeatherMap API Key
- [Poetry](https://python-poetry.org/): Dependency management tool for Python.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/connorjcantrell/grpc_weather_service.git
   cd grpc_weather_service
   ```

2. Install required dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Activate the poetry environment:
   ```bash
   poetry shell
   ```

4. Set the OpenWeatherMap API key as an environment variable:
   ```bash
   export WEATHER_API_KEY=your_api_key
   ```

## Usage

1. Start the gRPC server:
   ```bash
   python server/main.py
   ```

2. [Optional] To test, you can create a gRPC client and make a `GetCurrentWeather` request to `localhost:50051`.

## Extending the Service

To add more features, such as forecasts:

1. Update the `weather.proto` file with new service definitions.
2. Regenerate the gRPC code using the Protocol Buffers compiler.
3. Implement the new service in the server code.

## Troubleshooting
- **API Limitations**: The service relies on OpenWeatherMap, which might have rate limits based on your subscription.

## License

This project is licensed under the MIT License. See the `LICENSE.md` file for the full text.

