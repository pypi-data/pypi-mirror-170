from typing import Optional

import pydantic

from pynotionclient.schema.database.common_info_schema import IDSchema
from pynotionclient.schema.database.person_schema import PersonEmailSchema


class UserSchema(pydantic.BaseModel):
    id: Optional[str]
    name: Optional[str]
    object: Optional[str]
    avatar_url: Optional[str]
    person: Optional[PersonEmailSchema]


class DatabaseSchema(pydantic.BaseModel):
    database: Optional[IDSchema]


class PageSchema(pydantic.BaseModel):
    page: Optional[IDSchema]


# User, Page, database mention schema
class UPDMentionSchema(PageSchema, DatabaseSchema, UserSchema):
    pass
