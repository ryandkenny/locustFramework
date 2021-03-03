from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.get("/")

    # TODO add back in login post when appropriate
    # def on_start(self):
    #     self.client.post("/login", json={"username":"foo", "password":"bar"})
