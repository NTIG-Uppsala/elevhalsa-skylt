from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_JSON_FILE = "./service_account_credentials.json"


def get_service_account_credentials():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_JSON_FILE, scope
    )
    return credentials

def get_access_token():
    credentials = get_service_account_credentials()
    # from https://stackoverflow.com/a/69776579
    access_token = (
        credentials.create_delegated(credentials._service_account_email)
        .get_access_token()
        .access_token
    )
    return access_token