from src.pynotionclient.schema.database import IdNameSchema, IdTypeSchema


class InternalSelectSchema(IdNameSchema):
    color: str


class SelectSchema(IdTypeSchema):
    select: InternalSelectSchema
