import os

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials

from controller.parser_controller import extract_text
from controller.summarizer_controller import summarize_document
from controller.report_controller import generate_csv_report

import io

load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly"
]

DOWNLOAD_FOLDER = "downloads"


def get_drive_service():

    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=SCOPES
    )

    return build(
        "drive",
        "v3",
        credentials=creds
    )


def download_file(service, file_id, file_name):

    request = service.files().get_media(
        fileId=file_id
    )

    path = os.path.join(
        DOWNLOAD_FOLDER,
        file_name
    )

    fh = io.FileIO(path, "wb")

    downloader = MediaIoBaseDownload(
        fh,
        request
    )

    done = False

    while not done:
        status, done = downloader.next_chunk()

    return path


def process_drive_documents():

    os.makedirs(
        DOWNLOAD_FOLDER,
        exist_ok=True
    )

    service = get_drive_service()

    folder_id = os.getenv(
        "GOOGLE_DRIVE_FOLDER_ID"
    )

    response = service.files().list(
        q=f"'{folder_id}' in parents",
        fields="files(id,name,mimeType)"
    ).execute()

    files = response.get(
        "files",
        []
    )

    results = []

    for file in files:

        file_name = file["name"]

        if not (
            file_name.endswith(".pdf")
            or file_name.endswith(".docx")
            or file_name.endswith(".txt")
        ):
            continue

        file_path = download_file(
            service,
            file["id"],
            file_name
        )

        extracted_text = extract_text(
            file_path
        )

        summary = summarize_document(
            extracted_text
        )

        results.append(
            {
                "file_name": file_name,
                "summary": summary
            }
        )

    generate_csv_report(
        results
    )

    return results