import requests

# Set the URL of the web page that you want to generate traffic for
url = "http://webapp-1983844521.ap-south-1.elb.amazonaws.com/"

# Set the number of requests to send
num_requests = 10000

# Send the requests and get output of the count with HTTP Status Code
for i in range(num_requests):
    response = requests.get(url)
    print(f"Request {i+1}: {response.status_code}")
