## Face Authentication

Returns face authentication result *(True/False)* given a picture and a video of user's face.

## Installation
```
pip install face-authentication-lib
```

## Get Started

How to perform **face authentication** using this library:

- Within python script:

```bash
from face_authentication_lib import FaceAuth

# Instantiate a FaceAuth object using API key
face_auth = FaceAuth(api_key=API_KEY)

# Call 'authenticate' method to perform face authentication given an image and video of user's face
authentication_result = face_auth.authenticate(image_file, video_file)
```

- As Command Line Tool:

```bash
face_auth api_key image_file video_file
```

Complete documentation on: [readthedocs.io](https://face-authentication-library.readthedocs.io/en/latest/)
## Licence

This package in released under The **MIT** Licence
