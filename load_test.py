token = "..-ak8dp_ZQ73d-RwMAbHUhRs2focVR1pJaaqsDaEEY9eLY8_f7uC2ZmlmqedxsvrVIco1ZpnUcSzKGsI4s8aHdzbgKgckOfjsP3mmRDQUiVLYBciVRI0bu6wgZTzbD8Ied7kujxjK-K5IL6PC3-mMZLAAcENIIecF5_7IkixpezP6uvwSLLnVkiI8t4C7_qZirRjsr0sAdL8boXZjMfHmGyarM1JcFsdKWgsOpeyg"
from locust import HttpUser, task, between

class MyApiUser(HttpUser):
    wait_time = between(1, 3)  # Espera aleatoria entre peticiones (1 a 3 segundos)

    def on_start(self):
        # Token de autenticación
        self.token = token  # <-- reemplaza con tu token real

        # Headers con el token
        self.headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }

    @task
    def call_api(self):
        # Ejemplo: método GET
        self.client.get(
            "/predict",  # <-- ajusta a tu ruta real (puede ser '/' o 'predict', etc.)
            headers=self.headers
        )

        # Si es un POST, puedes hacerlo así:
        # self.client.post(
        #     "/ruta-api",
        #     json={"key": "value"},
        #     headers=self.headers
        # )
