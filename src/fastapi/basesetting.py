from typing import List, Optional, Union
from datetime import datetime

from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings

class DBConfig(BaseSettings):
    host: str = Field(default='localhost', env='HOST')
    port: int = Field(default=8000, env='PORT')

    class Config:
        env_file = '.env'
    
    @field_validator("host", mode="before")
    def check_host(cls, v):
        if v == "localhost":
            return "127.0.0.1"
        return v
    
    @field_validator("port")
    def check_port(cls, v):
        if v < 1024:
            raise ValueError("Port must be greater than 1024")
        return v
    
class ProjectConfig(BaseModel):
    project_name: str = "soojin"
    db_info: DBConfig = DBConfig()


project_data = {
    "projet_name": "project A",
    "db_info": {
        "host": "localhost",
        "port": 8000
    }
}

project = ProjectConfig(**project_data)
print(project.model_dump())
print(project.db_info)
