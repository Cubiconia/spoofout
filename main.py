import os
from tempfile import NamedTemporaryFile

import cv2
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request

from person_identification import face_recognition_main as face

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/verify-video")
async def verify_video(req: Request, file: UploadFile = File(...)):
    temp = NamedTemporaryFile(delete=False, dir=os.getcwd())
    img = cv2.imread(os.path.join("person_identification", "photos", "sample_1.jpeg"))
    print("path_image", os.path.join("person_identification", "photos", "sample_1.jpeg"))
    try:
        try:
            contents = await file.read()
            with temp as f:
                f.write(contents)
        except Exception:
            raise HTTPException(status_code=500, detail='Error on uploading the file')
        finally:
            temp.close()
            file.file.close()
        path = temp.name.replace("\\","/")
        splitted = path.rsplit("/",maxsplit=1)
        result = face.recognize(splitted[1], img)
        # result = "face_match"
        print(result)
    except Exception:
        raise HTTPException(status_code=500, detail='Something went wrong')
    finally:
        temp.close()  # the `with` statement above takes care of closing the file
        os.remove(temp.name)  # Delete temp file
    return {"status": result}

# if __name__ == '__main__':

# sequence()
# face_identification()
