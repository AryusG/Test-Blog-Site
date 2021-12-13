import requests

class Post:
    def __init__(self, endpoint):
        self.end = endpoint
        self.json = self.get_json()

    def get_json(self):
        url = self.end
        r = requests.get(url)
        json = r.json()
        
        return json


# p = Post("https://api.npoint.io/c790b4d5cab58020d391")

# print(p.json[0])
# # print(p.get_title())