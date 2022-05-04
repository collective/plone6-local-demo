from base64 import b64encode
from pathlib import Path
from time import sleep

import json
import requests
import magic
import typing as t


DATA_PATH = Path("./example-content").resolve()
IMAGE_PATH = DATA_PATH / "images"

base_url = "http://localhost:8080/Plone"
username = "admin"
password = "admin"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Wait for backend to be available
live: bool = False

while not live:
    try:
        response = requests.get(base_url)
    except requests.RequestException:
        sleep(1)
    else:
        live = response.status_code == 200


# Authenticate
response = requests.post(f"{base_url}/@login", headers=headers, json={"login": username, "password": password})

token = response.json()["token"]

headers["Authorization"] = f"Bearer {token}"


def add_to_plone(path: str, payload: dict):
    # Check if content exists
    url = f"{base_url}/{path}"
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        url = url[:-len(payload["id"])]
        response = requests.post(
            url,
            headers=headers,
            json=payload,
        )
        if response.status_code > 299:
            print(f"ERROR: {response.text}")
            return
        data = response.json()
        path = data["@id"]
        print(f"Created {path}")
        url = f"{path}/@workflow/publish"
        requests.post(url, headers=headers)
    elif response.status_code == 200:
        review_state = response.json().get("review_state")
        if review_state == "private":
            requests.post(f"{url}/@workflow/publish", headers=headers)
            print(f"Published {url}")
        response = requests.patch(
            url,
            headers=headers,
            json=payload,
        )
        if response.status_code > 299:
            breakpoint()
        print(f"Updated /{path}")
    else:
        print(f"ERROR: {url} {response.text}")


def add_image(info: dict) -> dict:
    has_image = info.get("set_local_image", {})
    if has_image:
        image_type = [i for i in has_image.keys()][0]
        image = has_image.get(image_type)
        local_filename = IMAGE_PATH / image
        if local_filename and local_filename.is_file():
            data = open(local_filename, "rb").read()
            info[image_type] = {
                "data": b64encode(data).decode("utf-8"),
                "encoding": "base64",
                "filename": image,
                "content-type": magic.from_buffer(data, mime=True)
            }
            del info["set_local_image"]
    return info


def get_content(path: Path) -> t.List[dict]:
    """Get all content"""
    content = []
    files = path.glob("*.json")
    for file in files:
        payload = add_image(json.load(open(file, "r")))
        name = file.name.replace(".json", "")
        if "id" not in payload:
            payload["id"] = name.split(".")[-1]
        internal_url = "/".join(name.split("."))
        if internal_url == "root":
            internal_url = ""
        content.append((internal_url, payload))
    return sorted(content)


content = get_content(DATA_PATH)
for path, payload in content:
    add_to_plone(path, payload)
