from ollama import chat
from ollama import ChatResponse
from dotenv import load_dotenv
import requests
import os

load_dotenv()

xc_token = os.getenv("API_KEY")
table_name = os.getenv("TABLE_NAME")
view_id = os.getenv("DEFAULT_VIEW")

LLM = "llama3.2"
QUERY = """
What are the main jurisdictional funding sources in Alaska?
"""

URL = f"https://app.nocodb.com/api/v2/tables/{table_name}/records"

HEADERS = {
    "accept": "application/json",
    "user-agent": "aksbdc/nocodb-to-gpt-via-api/0.0.4",
    "xc-token": xc_token,
}

PARAMETERS = {"offset": "0", "limit": "25", "where": "", "viewID": view_id}


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
    response: ChatResponse = chat(
        model=LLM,
        messages=[
            {"role": "user", "content": question},
        ],
    )

    output = response.message.content

    return output.json()


def fetch_data():
    """
    Retrieve data from the instance.
    """
    response = requests.request("GET", URL, headers=HEADERS, params=PARAMETERS)

    return response.json()


def main():
    project_description()


if __name__ == "__main__":
    main()
