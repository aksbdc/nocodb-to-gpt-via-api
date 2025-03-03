from ollama import chat
from ollama import ChatResponse

import requests
import torch


URL = "https://app.nocodb.com/api"
PARAMETERS = {
    "accept: application/json",
    "user-agent: aksbdc/nocodb-to-gpt-via-api/0.0.3",
}


def fetch_data():
    """
    Retrieve data from the instance.
    """
    response = requests.get(URL, headers=PARAMETERS)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")

    return response.json()


def system_diagnostics():
    """
    TODO: GPU support verification.
    """
    sample = torch.rand(42, 907)
    print(sample)


def main():
    print(">> Hello from nocodb-to-gpt-via-api!")
    print(">> This is a simple script that fetches data from an instance via the API.")
    print(">> The data is then used to train a GPT model.")

    # system_diagnostics()


if __name__ == "__main__":
    main()
