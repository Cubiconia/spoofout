import os
from tempfile import NamedTemporaryFile
from typing_extensions import Annotated

from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from person_identification import face_recognition_main as face
from util.authentication import basic_auth_handler, jwt_token_handler

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
async def verify_video(_: Annotated[str, Depends(basic_auth_handler)],
                       # jwt:Annotated[str, Depends(jwt_token_handler)],
                       video: UploadFile = File(),
                       image: UploadFile = File()):

    temp_video = NamedTemporaryFile(delete=False, dir=os.getcwd())
    temp_image = NamedTemporaryFile(delete=False, dir=os.getcwd())
    try:
        try:
            contents = await video.read()
            contents2 = await image.read()

            with temp_video as f:
                f.write(contents)
            with temp_image as f:
                f.write(contents2)

        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error on uploading the file')
        finally:
            temp_video.close()
            video.file.close()

            temp_image.close()
            image.file.close()

        path_video = temp_video.name.replace("\\", "/")
        path_video_split = path_video.rsplit("/", maxsplit=1)

        path_image = temp_image.name.replace("\\", "/")
        path_image_split = path_image.rsplit("/", maxsplit=1)

        result = face.recognize(path_video_split[1], path_image_split[1])
        print(result)
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Something went wrong')
    finally:
        temp_video.close()  # the `with` statement above takes care of closing the file
        temp_image.close()
        os.remove(temp_video.name)  # Delete temp file
        os.remove(temp_image.name)

    return JSONResponse(content={"message": result})
    # return {"status": result}

# sequence()
# face_identification()
