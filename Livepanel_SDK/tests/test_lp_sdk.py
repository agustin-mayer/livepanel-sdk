from Livepanel_SDK import LivepanelAuth, APIAccess
from dotenv import load_dotenv
import os

load_dotenv()

def get_api_access():
    api_key = os.getenv('LIVEPANEL_API_KEY')
    auth = LivepanelAuth(api_key)
    api_access = APIAccess(auth)
    return api_access

def test_get_projects():
    api_access = get_api_access()

    response = api_access.get_projects()
    print('Get Project Response:', response)

def test_create_project():
    api_access = get_api_access()

    payload = {
        'name': 'Proyecto de Prueba',
        'description': 'Descripción del proyecto de prueba',
    }

    response = api_access.create_project(payload)
    print('Create Project Response:', response)

def test_get_project():
    api_access = get_api_access()

    project_id = '194'
    response = api_access.get_project(project_id)
    print('Get Project Response:', response)

def test_download_dataset():
    api_access = get_api_access()

    project_id = '194'
    file_type = 'Train'
    response = api_access.download_dataset(project_id, file_type)
    print('Download Dataset Response:', response)


if __name__ == '__main__':
    # test_get_projects()
    # test_create_project()
    test_get_project()
    # test_download_dataset()
