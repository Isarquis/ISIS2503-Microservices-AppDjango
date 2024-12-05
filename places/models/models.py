# Models for the places microservice

from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId

class Colegio(BaseModel):
    codigo: str=Field(...)
    nombre: str = Field(...)
    cuenta: int = Field(...)
    direccion: str=Field(...)
    correo: str=Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "codigo": "ML515",
                "nombre": "sdfa",
                "cuenta": 1234,
                "direccion":"Calle",
                "correo":"correo@"
            }
        },
    )
    
class ColegioOut(BaseModel):
    id: PyObjectId=Field(alias="_id", default=None, serialization_alias="id")
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "codigo": "ML515",
                "nombre": "sdfa",
                "cuenta": 1234,
                "direccion":"Calle",
                "correo":"correo@"
            }
        },
    )

class ColegioCollection(BaseModel):
    # A collection of places
    places: List[Colegio] = Field(...)
