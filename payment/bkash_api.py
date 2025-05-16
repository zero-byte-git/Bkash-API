import requests
from django.conf import settings
import json
import logging

logger = logging.getLogger(__name__)  # Get a logger instance


class BkashAPI:
    def __init__(self):
        self.app_key = settings.BKASH_APP_KEY
        self.app_secret = settings.BKASH_APP_SECRET
        self.username = settings.BKASH_USERNAME
        self.password = settings.BKASH_PASSWORD
        self.sandbox_mode = settings.BKASH_SANDBOX_MODE
        self.base_url = (
            settings.BKASH_BASE_URL_SANDBOX
            if self.sandbox_mode
            else settings.BKASH_BASE_URL_PRODUCTION
        )
        self.version = "v1.2.0"  # Define API Version

    def execute_request(self, method, url, headers=None, data=None):
        """
        Handles making HTTP requests and logging.
        """
        try:
            response = requests.request(method, url, headers=headers, data=data)
            response.raise_for_status()  # Raise exception for bad status
            logger.debug(
                f"Bkash API {method} request to {url} successful. Status Code: {response.status_code}"
            )
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Bkash API {method} request to {url} failed: {e}")
            if e.response:
                logger.error(f"Response content: {e.response.text}")
            return None

    def create_auth_token(self):
        url = f"{self.base_url}/api/checkout/{self.version}/token/grant"
        headers = {"Content-Type": "application/json", "X-APP-Key": self.app_key}
        payload = {"app_key": self.app_key, "app_secret": self.app_secret}
        return self.execute_request(
            "POST", url, headers=headers, data=json.dumps(payload)
        )

    def create_payment(self, amount, order_id):
        token_response = self.create_auth_token()
        if not token_response or "id_token" not in token_response:
            logger.error("Failed to obtain Bkash auth token")
            return None

        token = token_response["id_token"]

        url = f"{self.base_url}/api/checkout/{self.version}/payment/create"
        headers = {
            "Content-Type": "application/json",
            "Authorization": token,
            "X-APP-Key": self.app_key,
        }
        payload = {
            "amount": str(amount),
            "currency": "BDT",
            "merchantInvoiceNo": order_id,
            "callbackURL": settings.BKASH_CALLBACK_URL,
            "intent": "sale",
        }
        return self.execute_request(
            "POST", url, headers=headers, data=json.dumps(payload)
        )

    def execute_payment(self, payment_id):
        token_response = self.create_auth_token()
        if not token_response or "id_token" not in token_response:
            logger.error("Failed to obtain Bkash auth token")
            return None
        token = token_response["id_token"]

        url = (
            f"{self.base_url}/api/checkout/{self.version}/payment/execute/{payment_id}"
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": token,
            "X-APP-Key": self.app_key,
        }
        payload = {}
        return self.execute_request(
            "POST", url, headers=headers, data=json.dumps(payload)
        )

    def query_payment(self, payment_id):
        token_response = self.create_auth_token()
        if not token_response or "id_token" not in token_response:
            logger.error("Failed to obtain Bkash auth token")
            return None
        token = token_response["id_token"]
        url = f"{self.base_url}/api/checkout/{self.version}/payment/status/{payment_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": token,
            "X-APP-Key": self.app_key,
        }
        return self.execute_request("GET", url, headers=headers)
