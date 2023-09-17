from pydantic import BaseModel


class Config(BaseModel):
    client_output: str
