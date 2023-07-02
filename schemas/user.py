from pydantic import BaseModel, Field


# HEREDAR DE BASEMODEL PARA CREAR NUESTRA CLASE
class User(BaseModel):
    email: str = Field(min_length=5, max_length=100,
                       title="Email",
                       description="This is the email")
    password: str = Field(min_length=5, max_length=15,
                          title="Password",
                          description="This is the password")
