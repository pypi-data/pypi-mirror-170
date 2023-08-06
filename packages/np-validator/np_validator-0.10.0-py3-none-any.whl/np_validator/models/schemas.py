from marshmallow import Schema, fields, post_load, validate

from .. import processors, validators
from .utils import list_functions


class ProcessorSchema(Schema):

    """Serialized builtin callable"""

    name = fields.String(validate=validate.OneOf(list_functions(processors)))
    args = fields.Dict(load_default={})


class ValidatorSchema(Schema):

    """Serialized builtin callable"""

    name = fields.String(validate=validate.OneOf(list_functions(validators)))
    args = fields.Dict(load_default={})


class ValidationStepSchema(Schema):

    """Serialized validation step"""

    path_suffix = fields.String()
    processor = fields.Nested(
        ProcessorSchema,
        many=False,
        allow_none=True,
    )
    validators = fields.Nested(ValidatorSchema, many=True)


class ValidatorResultSchema(Schema):

    value = fields.Raw()
    passed = fields.Boolean()
    validator = fields.Nested(ValidatorSchema, many=False)


class ValidationErrorSchema(Schema):

    message = fields.String()
    validator = fields.Nested(ValidatorSchema, many=False)
    processor = fields.Nested(
        ProcessorSchema,
        many=False,
    )


class ValidationResultSchema(Schema):

    """Serialized validation result"""

    filepath = fields.String()
    processor = fields.Nested(
        ProcessorSchema,
        many=False,
    )
    results = fields.Nested(
        ValidatorResultSchema,
        many=True,
    )
    errors = fields.Nested(
        ValidationErrorSchema,
        many=True,
    )
