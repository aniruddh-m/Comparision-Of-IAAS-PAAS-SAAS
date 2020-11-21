from locust import TaskSet, task, HttpUser

class UserBehaviour(TaskSet):
    @task
    def launch_url(self):
        # GET request
        self.client.get("/crud/Retrieve")
        print("Got a webpage response")
    

class User(HttpUser):
    tasks = [UserBehaviour]
    min_wait = 1000
    max_wait = 2000
    host = "http://127.0.0.1:8000"