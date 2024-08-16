# Dam Analytics Project

## Overview

This project is a Django application designed to provide insightful data analytics based on dam statistics. The application uses PostgreSQL as the database backend and is deployable using Docker.

## Table of Contents

1. [Setup Instructions](#setup-instructions)
2. [Database Population](#database-population)
3. [API Endpoints](#api-endpoints)
4. [Assumptions, Limitations, and Future Improvements](#assumptions-limitations-and-future-improvements)
5. [Docker Deployment](#docker-deployment)

---

## Setup Instructions

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- PostgreSQL
- Docker and Docker Compose
- Git

### Cloning the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/dam_analytics_project.git
cd dam_analytics_project
```

### Setting Up the Django Application

1. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

2. **Install the Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

3. **Update Database Settings**

   Ensure your Django application is configured to use PostgreSQL. Update the `DATABASES` section in `dam_analytics/settings.py` to match your PostgreSQL configuration.

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

4. **Run Migrations**

   Apply database migrations to set up the schema:

   ```bash
   python manage.py migrate
   ```

### PostgreSQL Database

1. **Create a PostgreSQL Database**

   You need a PostgreSQL database to store your data. Create a new database and user for the Django application.

   ```sql
   CREATE DATABASE dam_analytics_db;
   CREATE USER dam_user WITH ENCRYPTED PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE dam_analytics_db TO dam_user;
   ```

2. **Update Database Credentials**

   Update the `DATABASES` configuration in `settings.py` with the credentials you used to create the database.

## Database Population

### Gathering Data

1. **Data Source**

   Data is gathered from the [KSEB Dams Data](https://dams.kseb.in/?p=4703) for the date range August 4 to August 14, 2024.

2. **Data Ingestion**

   Populate the database using Django management commands, custom scripts, or data migration tools. You can create a custom Django management command to automate this.

   Example command to run a custom script:

   ```bash
   python manage.py populate_dam_data
   ```

## API Endpoints

### Overview

The API provides various endpoints to query dam statistics. The following endpoints are available:

1. **Get Highest Rainfall in a 10-Day Period**

   - **Endpoint**: `/api/rainfall/highest/`
   - **Method**: GET
   - **Response**:

     ```json
     {
       "dam_name": "Dam Name",
       "highest_rainfall": 150,
       "date": "2024-08-10"
     }
     ```

2. **Get Date of Highest Rainfall for a Specific Dam**

   - **Endpoint**: `/api/rainfall/highest/<dam_name>/`
   - **Method**: GET
   - **Response**:

     ```json
     {
       "dam_name": "Dam Name",
       "date": "2024-08-10",
       "rainfall": 150
     }
     ```

3. **List All Dams Within a Specific District**

   - **Endpoint**: `/api/dams/district/<district_name>/`
   - **Method**: GET
   - **Response**:

     ```json
     [
       {
         "dam_name": "Dam Name 1",
         "district": "District Name"
       },
       {
         "dam_name": "Dam Name 2",
         "district": "District Name"
       }
     ]
     ```

## Assumptions, Limitations, and Future Improvements

### Assumptions

- The data source from KSEB provides accurate and complete information.
- The PostgreSQL database is properly configured and accessible.

### Limitations

- The application currently supports only a fixed date range for data ingestion.
- Limited error handling and validation for API responses.

### Future Improvements

- Implement automated data ingestion to periodically update the database.
- Add advanced analytics features and visualizations.
- Enhance API with authentication and authorization features.

## Docker Deployment

### Prerequisites

Ensure Docker and Docker Compose are installed on your machine.

### Docker Setup

1. **Build and Run Containers**

   To build and run the Docker containers, use:

   ```bash
   docker-compose up --build
   ```

2. **Stopping the Containers**

   To stop and remove the containers, use:

   ```bash
   docker-compose down
   ```

### Docker Configuration

- **Dockerfile**: Contains instructions for building the Django application image.
- **docker-compose.yml**: Defines services for the Django application and PostgreSQL database.

Ensure the `docker-compose.yml` file correctly specifies the PostgreSQL database service and Django application configuration.

## Contributing

Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

### Steps to Update Your `README.md`

1. **Edit Your Local README.md**

   Open the `README.md` file in your project directory with a text editor and paste the above content.

2. **Commit and Push Changes**

   If you’ve made changes to the `README.md` file, commit and push them to your repository:

   ```bash
   git add README.md
   git commit -m "Update README with setup instructions, API endpoints, and Docker deployment"
   git push origin master
   ```

3. **Verify on GitHub**

   Visit your repository on GitHub to ensure the updated `README.md` file reflects the changes.

This updated `README.md` provides comprehensive information on setting up the project, populating the database, using the API, and deploying the application with Docker.
