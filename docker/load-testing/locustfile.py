

from locust import TaskSet, task, HttpUser

class UserBehaviour(TaskSet):
    # @task
    # def launch_url(self):
    #     # GET request
    #     self.client.get("/crud/Retrieve")
    #     print("Got a webpage response")
    
    @task
    def post_retrieve(self):
        # POST request on the RETRIEVE page
        response = self.client.get("/retrieve.php")
        self.client.post("/retrieve.php", {"USN": "1RV17EC666"})
        print("Posted a request")

class User(HttpUser):
    tasks = [UserBehaviour]
    min_wait = 1000
    max_wait = 2000
    host = "http://127.0.0.1:80"