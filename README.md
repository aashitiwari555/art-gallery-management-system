# Art Gallery Management System

A web-based **Art Gallery Management System** developed using **Flask** and **MySQL** to manage artists, artworks, exhibitions, buyers, and sales records in a structured and efficient manner.

This project demonstrates backend development, data handling using CSV files, and basic database integration with a clean web interface.

## Features
- Manage **artists, artworks, exhibitions, buyers, and sales**
- Add, view, search, and delete records
- CSV-based data handling for easy data import and testing
- Modular Flask application structure
- Clean separation of logic, templates, and static files
- Database connectivity using MySQL

## Tech Stack
**Backend:** Python, Flask  
**Frontend:** HTML, CSS  
**Database:** MySQL  
**Data Handling:** CSV files  
**Tools:** Git, GitHub
  
## Project Structure
```
art-gallery-management-system/
│
├── app.py                # Main Flask application
├── db.py                 # Database connection logic
│
├── templates/            # HTML templates
├── static/               # CSS and static assets
│
├── data/                 # Sample CSV data files
│   ├── artists.csv
│   ├── artworks.csv
│   ├── buyers.csv
│   ├── exhibitions.csv
│   ├── sales.csv
│   └── art_galleries.csv
│
├── docs/
│   └── Flowchart.png     # System flowchart
```

## System Flowchart
![System Flowchart](docs/Flowchart.png)

## How to Run the Project
1. Install Python and MySQL on your system  
2. Install required Python packages:
pip install flask mysql-connector-python
3. Configure MySQL database credentials in `db.py`
4. Ensure required CSV files are present in the `data/` folder
5. Run the application:
python app.py
6. Open the browser and navigate to:
http://localhost:5000

## Notes
CSV files provided are **sample data** for demonstration purposes

## Author
**Aashi Tiwari**  
Computer Science Engineering Student  
Interested in backend development, databases, and problem-solving
