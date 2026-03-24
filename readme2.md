# **Agricultural Drone Sprinkler Management System**







## **Project Overview:**





This project is a Python-based console application designed to manage and monitor liquid dispersal missions for agricultural drones. Built using a Three-Layered Monolithic Architecture, the software allows operators to log spraying sessions, track liquid efficiency, and maintain a historical record of crop treatments. This application is a direct adaptation of a proven Blood Pressure Tracking architecture, repurposed for the precision agriculture industry.





### Key Features:





* Mission Logging (CRUD): Create, Read, and Delete records of drone missions.



* Automated Efficiency Classification: Calculates spraying performance based on liquid-to-area ratios.



* Persistence: Data is stored in a flat-file database (drone\_logs.txt) for lightweight, reliable storage without external dependencies.



* Summary Analytics: Provides real-time totals for area covered and resources consumed.





### System Architecture:





* The software follows a structured monolithic design:



* Presentation Layer: Handles user interaction via a CLI (Command Line Interface).



* Business Logic Layer: contains the algorithms for classifying mission status (e.g., Optimal vs. Refill Required).



* Data Access Layer: Manages file I/O operations with the local file system





### **Data Schema:**





* Each mission record (LOG) consists of the following attributes:



* Mission ID: Unique identifier for the flight.



* Crop Type: The specific crop being treated (e.g., Wheat, Corn, Soy).



* Liquid Used: Volume of pesticide/fertilizer dispersed in Liters.



* Area Covered: Total land treated in Acres.



* Efficiency Status: Auto-generated classification based on dispersal rates.





### **How to Run:**





* Ensure you have Python 3.x installed.



* Download the \[**drone\_sprinkler.py]** script.



* Run the application via terminal:



&#x20;     **\[python drone\_sprinkler.py]**



* Data will automatically be saved to drone\_logs.txt in the same directory.





### **Future Enhancements:**





* Battery Telemetry: Integration of battery percentage tracking per mission.



* CSV Export: Functionality to export logs for analysis in Excel or GIS software.



* GPS Coordination: Adding latitude/longitude start/end points for each log.

