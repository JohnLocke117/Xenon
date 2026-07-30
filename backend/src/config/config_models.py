from pydantic import BaseModel

class AppConfig(BaseModel):
    name: str
    version: str

class ServerConfig(BaseModel):
    host: str
    port: int

# Final Config Class
class Config(BaseModel):
    app: AppConfig
    server: ServerConfig