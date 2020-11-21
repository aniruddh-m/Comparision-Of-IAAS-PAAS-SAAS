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
        response = self.client.get("/Retrieve")
        csrftoken = response.cookies['csrftoken']
        self.client.post("/Retrieve", {"USN": "1RV17EC011"}, headers={"X-CSRFToken": csrftoken})
        print("Posted a request")

class User(HttpUser):
    tasks = [UserBehaviour]
    min_wait = 1000
    max_wait = 2000
    host = "http://127.0.0.1:8000"