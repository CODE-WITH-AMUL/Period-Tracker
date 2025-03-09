# Period Tracking System

## Overview
The **Period Tracking System** is a Django-based application designed to help users track their menstrual cycles efficiently. It provides insights into cycle patterns, predicts upcoming periods, and offers lifestyle improvement suggestions.

## Features
- **Track Previous Records**: Stores and displays past menstrual cycle data.
- **Cycle Analysis**: Shows gaps between cycles and visualizes patterns.
- **Prediction System**: Estimates the next period cycle and end date.
- **Health Insights**: Provides suggestions for lifestyle improvements.
- **Modern UI**: Professional and visually appealing color scheme.

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/period-tracking-system.git
cd period-tracking-system
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Collect Static Files
```bash
python manage.py collectstatic
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

## Usage
1. Register/Login to your account.
2. Input your period start and end dates.
3. View cycle history and upcoming predictions.
4. Access health insights and recommendations.

## Documentation
Detailed documentation is available at [Documentation Link].

## Credits
This project is built using:
- **Django** - Backend framework
- **Bootstrap/Tailwind** - Frontend styling
- **Chart.js/D3.js** - Data visualization

## Screenshots
### Dashboard View:
_Image of the dashboard_

### Cycle Analysis:
_Image showing cycle tracking_

## License
This project is licensed under the [MIT License](LICENSE).

---
For contributions, issues, or feature requests, feel free to open a pull request or contact [your email].
