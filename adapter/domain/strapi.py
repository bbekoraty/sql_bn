from fastapi import  HTTPException
import requests
import json
import uuid

from config import (STRAPI_URL,STRAPI_AUTHOR)

class Strapi:

    def __init__(self):
        self.login_url = f"{STRAPI_URL}api/auth/local"
        self.user_url = f"{STRAPI_URL}api/users/me?populate=%2A"
        self.project_url = f"{STRAPI_URL}api/projects"
        self.headers =  {'Content-Type': 'application/json'}

    def login(self,payload):
        response = requests.request("POST", self.login_url, headers=self.headers, data=json.dumps(payload))
        
        return json.loads(response.text)

    def getUserInfo(self,request):
        # headers = {'Authorization': request.headers.get('Authorization')}
        headers = {'Authorization': STRAPI_AUTHOR}

        response = requests.request("GET",self.user_url, headers=headers, data={})
    
        data = json.loads(response.text)
        
        if 'error' in data:
            raise HTTPException(status_code=data['error']['status'], detail=data['error']['message'])
        
        filtered_data = {
            "uuid": data["uuid"],
            "projects": [{"name": project["name"], "token": project["token"]} for project in data["projects"]]
        }
        
        return filtered_data
        # return data
        
    def getProject(self,request):
        # headers = {'Authorization': request.headers.get('Authorization')}
        headers = {'Authorization': STRAPI_AUTHOR}

        response = requests.request("GET",self.user_url, headers=headers, data={})
    
        data = json.loads(response.text)
        
        if 'error' in data:
            raise HTTPException(status_code=data['error']['status'], detail=data['error']['message'])
        
        filtered_data = {
            "projects": [{"name": project["name"], "token": project["token"]} for project in data["projects"]]
        }
        
        return filtered_data
        
        
    
    def findproject(self,request,uuid):
        
        headers = {'Authorization': request.headers.get('Authorization')}
        
        project_url = f"{self.project_url}?filters[token][$eq]={uuid}"

        response = requests.request("GET",project_url, headers=headers, data={})
        
        data = json.loads(response.text)
        
        if 'error' in data:
            raise HTTPException(status_code=data['error']['status'], detail=data['error']['message'])
        return data
    
    def createproject(self,request,payload):
        
        data = self.getuser(request)
        
        if 'error' in data:
            raise HTTPException(status_code=data['error']['status'], detail=data['error']['message'])
        
        headers = {'Authorization': request.headers.get('Authorization'),'Content-Type': 'application/json'}

        new_payload = {
            "data": {
                "name": payload.name,
                "capacity": payload.capacity,
                "inspection_date": payload.inspection_date,
                "inspector": payload.inspector,
                "tel":payload.tel,
                "total_component": payload.total_component,
                "users_permissions_users": data['id'],
                "token":str(uuid.uuid4()),
                "location": {
                    "latitude": payload.location['latitude'],
                    "longitude": payload.location['longitude']
                } 
            }
        }
        
        response = requests.request("POST", self.project_url, headers=headers, data=json.dumps(new_payload))
        
        response_text = json.loads(response.text)
        
        if 'error' in response_text:
            raise HTTPException(status_code=data['error']['status'], detail=data['error']['message'])
        
        return response_text
    
    def remove_project(self,request,id):
        
        headers = {'Authorization': request.headers.get('Authorization')}
        
        project_url = f"{self.project_url}/{id}"
        
        response = requests.request("DELETE",project_url, headers=headers, data={})
        
        data = json.loads(response.text)
        
        if 'error' in data:
            raise HTTPException(status_code=data['error']['status'], detail=data['error']['message'])
        
        return data
        
        
        
        

        

        
        



