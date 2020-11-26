# Comparision-Of-IAAS-PAAS-SAAS
Steps to run the project
1. Install django
2. Navigate to the directory of the project
3. Open the terminal and run the command "python manage.py runserver"
4. Open pages "http://127.0.0.1:8000/crud/Create", "http://127.0.0.1:8000/crud/Retrieve", "http://127.0.0.1:8000/crud/Update" and "http://127.0.0.1:8000/crud/Delete" and verify the operations

For the Docker app:

1. Install Docker and then build the containers using the `docker compose up -d` command
2. After running all the 3 containers, open `localhost` to view the homepage of the CRUD Website
3. For load testing, run `pip install locust`, `cd` to the `load-testing` directory and run `locust` in the Terminal
4. Open `0.0.0.0:8089` to view the Locust Web UI and configure the load testing parameters
