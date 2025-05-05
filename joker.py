import requests

def fetch_random_joke():
    api_url = "https://official-joke-api.appspot.com/random_joke"
    try:
        joke_response = requests.get(api_url)
        joke_response.raise_for_status()
        return joke_response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error fetching joke: {error}")
        return None

def display_joke(joke):
    print("\nHere is a random joke for you:")
    print(f"Q: {joke.get('setup')}")
    print(f"A: {joke.get('punchline')}")

def start():
    joke_data = fetch_random_joke()
    if joke_data:
        display_joke(joke_data)
    else:
        print("Failed to retrieve a joke. Please try again later.")

if __name__ == "__main__":
    start()
