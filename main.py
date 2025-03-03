from ollama import chat
from ollama import ChatResponse

import requests
import torch
import time

LLM = "llama3.2"
URL = "https://app.nocodb.com/api"
PARAMETERS = {
    "accept: application/json",
    "user-agent: aksbdc/nocodb-to-gpt-via-api/0.0.3",
}


def project_description():
    """
    Example entrypoint for command-line interface (CLI).
    """
    print(">> Hello from nocodb-to-gpt-via-api!")
    print(">> This is a simple script that fetches data from an instance via the API.")
    print(">> The data is then used to train a GPT model.")


def sample_usage(question):
    """
    Benchmark query analysis from research notes.
    """
    response: ChatResponse = chat(model=LLM, messages=[
        {
            'role': 'user',
            'content': question
        },
    ])
    output = response.message.content
    print(output)


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
    return sample


def main():
    system_diagnostics()
    project_description()
    length = 8
    print('-' * length)

    start = time.time()
    sample_usage("What are the main jurisdictional funding sources in Alaska?")
    end = time.time()
    elapsed = end - start

    print(f"\n>> ⏱️ Response Time: {elapsed}s")


if __name__ == "__main__":
    main()
