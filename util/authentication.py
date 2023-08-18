import os
import secrets
from typing import Union

from fastapi import Depends, status, HTTPException, Header
from fastapi.security import HTTPBasicCredentials, HTTPBasic, OAuth2PasswordBearer
from typing_extensions import Annotated

basic = HTTPBasic()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def basic_auth_handler(credentials: Annotated[HTTPBasicCredentials, Depends(basic)]):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = bytes(os.environ["BASIC_AUTH_USERNAME"] or "GPM-DEVELOPMENT",encoding="utf-8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = bytes(os.environ["BASIC_AUTH_PASSWORD"] or "GPM-DEVELOPMENT",encoding="utf-8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect basic username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


def jwt_token_handler(x_access_token: Annotated[Union[str, None], Header()] = None):
    print(x_access_token)
