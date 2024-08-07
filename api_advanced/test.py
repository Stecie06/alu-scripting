import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Print status code and response text for debugging
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 0

# Example usage
subreddit = "python"
subscribers = number_of_subscribers(subreddit)
print(f"Subscribers: {subscribers}")
