Agricultural Drone Sprinkler Management System



Project Overview:


This project is a Python-based console application designed to manage and monitor liquid dispersal missions for agricultural drones. Built using a Three-Layered Monolithic Architecture, the software allows operators to log spraying sessions, track liquid efficiency, and maintain a historical record of crop treatments. This application is a direct adaptation of a proven Blood Pressure Tracking architecture, repurposed for the precision agriculture industry.


Key Features:


1.Mission Logging (CRUD): Create, Read, and Delete records of drone missions.

2.Automated Efficiency Classification: Calculates spraying performance based on liquid-to-area ratios.

3.Persistence: Data is stored in a flat-file database (drone_logs.txt) for lightweight, reliable storage without external dependencies.

4.Summary Analytics: Provides real-time totals for area covered and resources consumed.


System Architecture:


1.The software follows a structured monolithic design:

2.Presentation Layer: Handles user interaction via a CLI (Command Line Interface).

3.Business Logic Layer: contains the algorithms for classifying mission status (e.g., Optimal vs. Refill Required).

4.Data Access Layer: Manages file I/O operations with the local file system


Data Schema:


1.Each mission record (LOG) consists of the following attributes:

2.Mission ID: Unique identifier for the flight.

3.Crop Type: The specific crop being treated (e.g., Wheat, Corn, Soy).

4.Liquid Used: Volume of pesticide/fertilizer dispersed in Liters.

5.Area Covered: Total land treated in Acres.

6.Efficiency Status: Auto-generated classification based on dispersal rates.


How to Run:


1.Ensure you have Python 3.x installed.

2.Download the [drone_sprinkler.py] script.

3.Run the application via terminal:

      [python drone_sprinkler.py]

4.Data will automatically be saved to drone_logs.txt in the same directory.a


Future Enhancements:


1.Battery Telemetry: Integration of battery percentage tracking per mission.

2.CSV Export: Functionality to export logs for analysis in Excel or GIS software.

3.GPS Coordination: Adding latitude/longitude start/end points for each log.
