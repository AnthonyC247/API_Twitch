import requests
import twitchAPI
import os 
from datetime import datetime

CLIENT_ID = os.environ.get('TWITCH_CLIENT_ID')
CLIENT_SECRET = os.environ.get('TWITCH_CLIENT_SECRET')
  user_req = requests.get(BASE_URL + '/users?login=' + user_name, headers=headers)
  user_data = user_req.json()['data']
  if len(user_data) != 0:
    print('------------------')
    user_data = user_req.json()['data'][0]
    user_id = user_data['id']
    print("User found!")
    print("Name:", user_data['display_name'])
    print("Description:", user_data['description'])
    print("Broadcaster Type:", user_data['broadcaster_type'])
    print("Member since:", user_data['created_at'])
    print("Member since:", datetime.strptime(user_data['created_at'], "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y"))
    print("Most recent videos - ")
    video_req = requests.get(BASE_URL + '/videos?user_id=' + user_id, headers=headers)
    video_data = video_req.json()['data']
    i = 0
    while i < 5 and i < len(video_data):
      curr_vid = video_data[i]
      print("Title:", curr_vid['title'])
      print("Posted:", curr_vid['published_at'])
      print("Posted:", datetime.strptime(curr_vid['published_at'], "%Y-%m-%dT%H:%M:%SZ").strftime("%B %d, %Y"))
      print("Views:", curr_vid['view_count'])
      i+=1
    print('------------------')
  else:
    print("Viewer not seen :|")
print('Bye!')

#a test to be sure
