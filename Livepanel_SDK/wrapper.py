import requests

class APIAccess:
    def __init__(self, auth):
        self.auth = auth

    def create_project(self, payload): 
        url = 'https://tools.api.livepanel.ai/v2/projects'
        headers = self.auth.get_headers()
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
    

    def get_project(self, project_id):
        url = f'https://tools.api.livepanel.ai/v2/projects/{project_id}'
        headers = self.auth.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()
    

    def download_dataset(self, project_id, file_type):
        url = f'https://tools.api.livepanel.ai/v2/api/projects/{project_id}/datasets/get_file?type={file_type}'
        headers = self.auth.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()