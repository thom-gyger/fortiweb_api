import json
from marshmallow.fields import Nested, List
class EndpointBase:
    post_required_fields = []
    post_mark = {"post": True}
    post_mark_optional = {"post_optional": True}
    put_mark = {"put": True}
    key_mark = {"key": True}

    @classmethod
    def get_post_json_template(cls)  -> str:
        json_friendly_annotations = {
            key: f"{{{{{key}}}}}" for key in cls.__annotations__.keys() if key in cls.post_required_fields
        }
        return json.dumps(json_friendly_annotations)

    def serialize(self, all_fields=False) -> dict:
        if all_fields:
            filtered_data = {
                key: getattr(self, key)
                for key, field in self.Schema().fields.items()
                if not isinstance(field, (self.Schema, Nested))  # Exclude Schema and Nested fields
            }
            return self.Schema().dump(filtered_data)
        else:
            filtered_data = {
                key: getattr(self, key)
                for key, field in self.Schema().fields.items()
                if field.metadata.get("post", False)
            }

            return self.Schema().dump(filtered_data)


    def post_fields(self):
        from dataclasses import fields
        fields = [field.name for field in fields(self) if field.metadata.get("post", False)]
        return fields

    def put_fields(self):
        from dataclasses import fields
        fields = [field.name for field in fields(self) if field.metadata.get("put", False)]
        return fields

    def key_field(self):
        from dataclasses import fields
        fields = next(field.name for field in fields(self) if field.metadata.get("key", False))
        return fields
