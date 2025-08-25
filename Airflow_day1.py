import requests
from datetime import datetime


def is_valid_date(date_text):
    """Check if a date string is in the correct format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_user_date_input():
    """Prompt user for a valid date range with proper validation."""
    while True:
        print("\n📅 Please enter the date range for weather data (format: YYYY-MM-DD)")
        start_date = input("Enter start date: ")
        end_date = input("Enter end date  : ")

        if not is_valid_date(start_date) or not is_valid_date(end_date):
            print("❌ Invalid date format. Please use YYYY-MM-DD.")
            continue

        if start_date > end_date:
            print("❌ Start date cannot be after end date.")
            continue

        print(f"✅ Selected date range: {start_date} to {end_date}")
        return start_date, end_date


def get_weather_data(start_date, end_date, latitude=17.3850, longitude=78.4867):
    """Fetch weather data from Open-Meteo API."""
    print("\n🌐 Fetching weather data from Open-Meteo API...")

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
        "start_date": start_date,
        "end_date": end_date
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        print("✅ Weather data fetched successfully.")
        return data["daily"]["time"], data["daily"]["temperature_2m_max"], data["daily"]["temperature_2m_min"]

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"❌ Network error occurred: {e}")
    except KeyError:
        raise RuntimeError("❌ API response format unexpected or data unavailable.")
    except Exception as e:
        raise RuntimeError(f"❌ Unexpected error: {e}")


def print_weather_report(dates, max_temps, min_temps):
    """Print daily weather report."""
    print("\n📊 === Daily Weather Report ===")
    for i in range(len(dates)):
        print(f"{dates[i]}  -->  Min: {min_temps[i]}°C , Max: {max_temps[i]}°C")


def find_extremes(dates, max_temps, min_temps):
    """Find and print the highest and lowest temperatures and their corresponding dates."""
    highest_temp = max(max_temps)
    lowest_temp = min(min_temps)
    highest_day = dates[max_temps.index(highest_temp)]
    lowest_day = dates[min_temps.index(lowest_temp)]

    print("\n📈 === Temperature Summary ===")
    print(f"🔺 Highest temperature: {highest_temp}°C on {highest_day}")
    print(f"🔻 Lowest temperature : {lowest_temp}°C on {lowest_day}")


def detect_anomalies(dates, max_temps, threshold=3.0):
    """Detect and print anomalies (sudden changes) in max temperature."""
    print("\n⚠️ === Anomalies Report (Δ > 3°C) ===")
    anomalies_found = False

    for i in range(1, len(max_temps)):
        diff = max_temps[i] - max_temps[i - 1]
        if abs(diff) > threshold:
            print(
                f"🚨 {dates[i]}: Max temp changed by {diff:+.1f}°C "
                f"(from {max_temps[i - 1]}°C to {max_temps[i]}°C)"
            )
            anomalies_found = True

    if not anomalies_found:
        print("✅ No temperature anomalies found during the selected period.")


def main():
    print("🌤️ === Hyderabad Weather Report Generator ===")

    # Step 1: Get valid date input from user
    start_date, end_date = get_user_date_input()

    try:
        # Step 2: Fetch weather data from Open-Meteo
        dates, max_temps, min_temps = get_weather_data(start_date, end_date)

        # Step 3: Display the data
        print_weather_report(dates, max_temps, min_temps)

        # Step 4: Show temperature extremes
        find_extremes(dates, max_temps, min_temps)

        # Step 5: Detect any anomalies
        detect_anomalies(dates, max_temps)

        print("\n✅ Report generation complete.\n")

    except RuntimeError as err:
        print(f"\n❌ ERROR: {err}")
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")


if __name__ == "__main__":
    main()
