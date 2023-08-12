
<div align="center">
  <h1> Paw Rescue - Connecting Animals with Loving Homes</h1>
</div>

<img src="https://raw.githubusercontent.com/vanesakuleva/PawRescue/master/screenshots/Screenshot%202023-08-12%20at%201.06.09.png" alt="Project image" style="width: 850px"/>

Welcome to Paw Rescue! Our mission is to connect animals in need with caring families. Paw Rescue is a Django Web App designed to facilitate the adoption and fostering of animals, providing a platform where users can discover adorable pets awaiting their forever homes.

Paw Rescue offers a range of features to provide a comprehensive platform for animal adoption and fostering, as well as pet-related events:


- **User-friendly Adoption and Fostering Platform** 

- **Submit Adoption and Fostering Applications Online** 

- **Interactive Admin Panel** 

- **Events Page** 

- **Responsive Design for Optimal User Experience**  



## Installation

Follow these steps to set up and run the Paw Rescue Django web app on your local machine:

1. **Clone the Repository:** Start by cloning this repository to your local machine using Git:
   ```bash
   git clone https://github.com/vanesakuleva/PawRescue.git
   
2. Navigate to the Project Directory: Change your working directory to the project folder:
   ```bash
   cd PawRescue
   
3. Create and Activate Virtual Environment:
   ```bash
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate   # On macOS and Linux
    venv\Scripts\activate      # On Windows

4. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   
5. Apply necessary database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6. Create a superuser account for admin access:
Create a Superuser (Optional but Recommended): Create a superuser account for admin access:
   ```bash
    python manage.py createsuperuser

7. Start the Django development server:
   ```bash
    python manage.py runserver
    
8. Open a web browser and go to http://127.0.0.1:8000/ to see the Paw Rescue web app.



## Technologies

- Django
- HTML, CSS
- PostgreSQL
- Bootstrap


[//]: # (## Demo)

[//]: # ()
[//]: # (For a live demonstration of the Paw Rescue platform, visit our live demo at [http://pawrescue-demo.com/]&#40;http://pawrescue-demo.com/&#41;.)

## License

This project is licensed under the MIT License.

## Screenshots

<img src="https://raw.githubusercontent.com/vanesakuleva/PawRescue/master/screenshots/Screenshot%202023-08-12%20at%201.06.09.png" alt="Project image" style="width: 850px"/>