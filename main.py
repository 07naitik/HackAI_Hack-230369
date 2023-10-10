import requests
from uagents import Agent, Context

temp_agent = Agent(name="temp_agent", seed="temp fetch")

min_threshold = 0.0 
max_threshold = 0.0


# API Key and location information
API_KEY = 'f52caee3c7396e7d90fb8c595b251b93'  # Replace with your OpenWeatherMap API key
LOCATION = ''  # Replace with your preferred location (city, country code)

# def take_info():
#     min_threshold = float(input("Enter the min temp: "))
#     max_threshold = float(input("Enter the max temp: "))

# Create a TemperatureAlertAgent
    # Define a task to fetch and check the temperature
@temp_agent.on_interval(period=5)  # Fetch data every 10 minutes (adjust as needed)
async def check_temperature(ctx: Context):
    try:
        # Fetch real-time temperature data from the OpenWeatherMap API
        url = f'http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units=metric'
        response = requests.get(url)
        data = response.json()
        current_temperature = data['main']['temp']
        print(current_temperature)

        # min_threshold = 10.0  # Minimum acceptable temperature in °C
        # max_threshold = 30.0  # Maximum acceptable temperature in °C

        ctx.logger.info(f'Current temperature in {LOCATION}: {current_temperature}°C')
            # Check if the temperature is outside the user-defined range
        if current_temperature < min_threshold:
            ctx.logger.warning(f'Temperature is below the minimum threshold ({min_threshold}°C)!')
        elif current_temperature > max_threshold:
            ctx.logger.warning(f'Temperature is above the maximum threshold ({max_threshold}°C)!')

        else:
            ctx.logger.info('Its in the range baby.')

    except Exception as e:
        ctx.logger.error(f'Error fetching temperature data: {str(e)}')

if __name__ == "__main__":
    city = input("Enter the city: ")
    country = input("Enter the country code: ")
    LOCATION = f'{city},{country}'
    min_threshold = float(input("Enter the min temp: "))
    max_threshold = float(input("Enter the max temp: "))

    # Run the agent
    temp_agent.run()
