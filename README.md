# ☔ Weather_SMS_Alert

A Python automation project that monitors weather forecasts using the OpenWeatherMap API and sends SMS notifications through Twilio when rain is expected.

This project helps users stay prepared by automatically alerting them to carry an umbrella before bad weather arrives.

---

## Features

✅ Retrieves weather forecast data from OpenWeatherMap

✅ Checks upcoming weather conditions

✅ Detects rain based on weather condition codes

✅ Sends SMS alerts using Twilio

✅ Runs automatically at scheduled intervals

✅ Simple and beginner friendly Python project

---

## Technologies Used

- Python
- Requests
- OpenWeatherMap API
- Twilio API

---

## Project Structure

```text
Weather_SMS_Alert/
│
├── main.py
└── README.md
```

---

## How It Works

1. Fetches weather forecast data from OpenWeatherMap.
2. Examines upcoming weather condition codes.
3. Determines whether rain is expected.
4. Sends an SMS alert using Twilio if rain is predicted.
5. Reminds the user to carry an umbrella.

---

## Example SMS

```text
It's going to rain, get an umbrella with you!
☔
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Weather_SMS_Alert.git
```

Install required packages:

```bash
pip install requests twilio
```

---

## Configuration

Create your own:

- OpenWeatherMap API Key
- Twilio Account SID
- Twilio Auth Token

Replace the credentials in the code with your own values or store them as environment variables.

---

## Learning Outcomes

This project helped practice:

- Working with APIs
- JSON data handling
- HTTP requests
- SMS automation
- Python automation projects
- External service integration

---

## Author

Satya Saurav

Built while learning Python automation and API integration.
