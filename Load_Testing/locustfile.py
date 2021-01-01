from locust import TaskSet, task, HttpUser

class UserBehaviour(TaskSet):

    @task
    def post_Create(self):
        # POST request on the CREATE page
        response = self.client.get("/Create")
        csrftoken = response.cookies['csrftoken']
        self.client.post("/Create", {"USN": "1RV17EC011", "Branch": "CSE", "Name": "Jon Do"}, headers={"X-CSRFToken": csrftoken})
        print("Posted a request")

    @task
    def post_update(self):
        # POST request on the UPDATE page
        response = self.client.get("/Update")
        csrftoken = response.cookies['csrftoken']
        self.client.post("/Update", {"USN": "1RV17EC011", "Branch": "CSE"}, headers={"X-CSRFToken": csrftoken})
        print("Posted a request")

    @task
    def post_retrieve(self):
        # POST request on the RETRIEVE page
        response = self.client.get("/Retrieve")
        csrftoken = response.cookies['csrftoken']
        self.client.post("/Retrieve", {"USN": "1RV17EC011"}, headers={"X-CSRFToken": csrftoken})
        print("Posted a request")

    @task
    def post_delete(self):
        # POST request on the DELETE page
        response = self.client.get("/Delete")
        csrftoken = response.cookies['csrftoken']
        self.client.post("/Delete", {"USN": "1RV17EC011"}, headers={"X-CSRFToken": csrftoken})
        print("Posted a request")

class User(HttpUser):
    tasks = [UserBehaviour]
    min_wait = 1000
    max_wait = 2000
    host = "http://127.0.0.1:8000"
