import os
from pathlib import Path
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import shutil

scopes = ["https://www.googleapis.com/auth/youtube.upload"]

def remove_content(filePath):
    parent_dir = filePath.parent
    try:
        shutil.rmtree(parent_dir)

        if not parent_dir.exists():
            print(f"Le dossier {parent_dir} a été supprimé.")
        else:
            print(f"Échec de la suppression du dossier {parent_dir}.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la tentative de suppression du dossier {parent_dir}: {e}")

def upload_video(filePath):
    filePath = Path(filePath)
    if not filePath.exists():
        print(f"Le fichier {filePath} n'existe pas.")
        return

    # Disable OAuthlib's HTTPS verification when running locally.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    try:
        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "categoryId": "22",
                    "description": "Automated Upload",
                    "title": filePath.stem
                },
                "status": {
                    "privacyStatus": "unlisted"
                }
            },
            media_body=googleapiclient.http.MediaFileUpload(filePath)
        )
        response = request.execute()

        if 'id' in response:
            print(f"Upload réussi. ID de la vidéo: {response['id']}")
            remove_content(filePath)
        else:
            print("Echec de l'upload, aucune ID de vidéo trouvée dans la réponse.")
    except googleapiclient.errors.HttpError as e:
        print(f"Une erreur HTTP est survenue: {e}")
    except googleapiclient.errors.Error as e:
        print(f"Une erreur de l'API est survenue: {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}")

def find_and_upload_videos(directory_path, ignore_path):
    path = Path(directory_path)
    ignore_path = Path(ignore_path)

    for file_path in path.rglob('*.mp4'):
        if ignore_path not in file_path.parents:
            upload_video(file_path)
        return  # Retirer pour traiter tous les fichiers

if __name__ == "__main__":
    start_directory = "C:\\Users\\tagem\\Videos\\Overwolf\\Outplayed\\Rocket League"
    ignore_directory = "C:\\Users\\tagem\\Videos\\Overwolf\\Outplayed\\temp-capture"
    find_and_upload_videos(start_directory, ignore_directory)
