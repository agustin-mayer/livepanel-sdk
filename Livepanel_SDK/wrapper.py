import requests

class APIAccess:
    def __init__(self, auth):
        self.auth = auth
        
    def get_projects(self):
        url = f'https://tools.api.stg.livepanel.ai/api/v2/projects'
        headers = self.auth.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()

    def create_project(self, payload): 
        url = 'https://tools.api.stg.livepanel.ai/api/v2/projects'
        headers = self.auth.get_headers()
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
    

    def get_project(self, project_id):
        url = f'https://tools.api.stg.livepanel.ai/api/v2/projects/{project_id}'
        headers = self.auth.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()
    
    def enqueue_project_for_processing(self, project_id):
        url = f'https://tools.api.stg.livepanel.ai/api/v2/projects/{project_id}/enqueue'
        headers = self.auth.get_headers()
        response = requests.post(url, headers=headers)
        return response.json()

    def download_dataset(self, project_id, file_type):
        url = f'https://tools.api.stg.livepanel.ai/api/v2/projects/{project_id}/datasets/get_file?type={file_type}'
        headers = self.auth.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()