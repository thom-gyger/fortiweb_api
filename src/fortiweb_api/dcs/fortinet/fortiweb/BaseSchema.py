from marshmallow import ValidationError, Schema, EXCLUDE, pre_dump
from marshmallow import pre_load, post_dump, validates_schema, ValidationError
import re


class Baseschema(Schema):
    '''
    Base schema for all schemas in the module
    This Base Schema includes the replacement of hyphens with underscores in keys during load and also transforms it back during dump.
    Due to the Fact that the devices API may contain underscores in keys,
    it's not possible to make a simple replacement of hyphens with underscores and vice versa.
    all keys that are transformed during load have to be tracked and recorded in the context of the Meta class.
    This information is then used during dump to revert the transformation.

    This BaseSchema class is passed as a parameter to the dataclass decorator in the schema classes.
    '''

    class Meta:
        unknown = EXCLUDE
        context = {"transformed_keys": {}, "firmware_version": None}
        exclude = ()

    @pre_load
    def replace_hyphens_with_underscores(self, data, **kwargs):

        """Replace hyphens with underscores in keys and store transformations in context. Includes other workarounds like tacacs+"""

        if not isinstance(data, dict):
            return data

        transformed_data = {}
        self.Meta.context['transformed_keys'][type(self)] = {}

        for key, value in data.items():
            new_key = key.replace('-', '_')
            new_key = new_key.replace('tacacs+', 'tacacsplus')
            transformed_data[new_key] = value
            if new_key != key:  # Track only transformed keys
                self.Meta.context['transformed_keys'][type(self)][new_key] = key
        return transformed_data

    @pre_load
    def check_firmware(self, data, **kwargs):
        """in any Dataclass, use the metadata key "firmware" to specify the firmware version at which the field should be used. example: some_crap : str = field(metadata={"firmware":">6.6"})"""

        from dataclasses import field

        firmware = None
        if isinstance(data, dict):
            firmware = data.get("firmware", None)

        if firmware:
            self.fields["firmware"] = field()

        if self.fields.get("firmware"):
            for field, value in self.fields.items():
                if value.metadata.get("firmware"):
                    field_version = float(value.metadata.get("firmware")[1:])
                    if value.metadata.get("firmware").startswith(">"):
                        if firmware < field_version:
                            value.allow_none = True
                            data[field] = None

                    elif value.metadata.get("firmware").startswith("<"):
                        if firmware >= field_version:
                            value.allow_none = True
                            data[field] = None

        return data


    @post_dump
    def replace_underscores_with_hyphens(self, data, **kwargs):
        """Replace underscores with hyphens for keys based on pre_load transformations. Includes other workarounds like tacacs+"""
        transformed_data = {}
        for key, value in data.items():
            # Check if this key was transformed and revert it
            original_key = self.Meta.context.get('transformed_keys', {}).get(type(self), {}).get(key, key)
            transformed_data[original_key] = value
        return transformed_data


