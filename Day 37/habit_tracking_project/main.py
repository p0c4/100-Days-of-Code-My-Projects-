import requests
import os
from datetime import datetime


"""First Step - Create a user"""
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": os.environ.get("PIXELA_TOKEN"),
    "username": os.environ.get("PIXELA_USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


"""Second Step - After user created, Create the graph"""
graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Speaking Graph",
    "unit": "minute",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": user_params["token"]
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


"""Third Step - After graph created, Adding pixel is next"""
add_pixel_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}"
add_pixel_params = {
    "date": datetime.now().strftime('%Y%m%d'),
    "quantity": input("How many minutes did you study speaking today? "),
}
response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
print(response.text)


"""Fourth Step - If we want to change any posted input"""  # This option is paid
# put posted input's date to update_endpoint
update_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{add_pixel_params['date']}"
new_pixel_params = {
    "quantity": "30"
}
# response = requests.put(url=update_endpoint, json=new_pixel_params, headers=headers)
# print(response.text)


""""Lastly - If we want to delete any posted input"""
delete_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{add_pixel_params['date']}"

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)