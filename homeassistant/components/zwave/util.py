"""Zwave util methods."""
import logging

from . import const

_LOGGER = logging.getLogger(__name__)


def check_node_schema(node, schema):
    """Check if node matches the passed node schema."""
    if (const.DISC_NODE_ID in schema and
            node.node_id not in schema[const.DISC_NODE_ID]):
        _LOGGER.debug("node.node_id %s not in node_id %s",
                      node.node_id, schema[const.DISC_NODE_ID])
        return False
    if (const.DISC_GENERIC_DEVICE_CLASS in schema and
            node.generic not in schema[const.DISC_GENERIC_DEVICE_CLASS]):
        _LOGGER.debug("node.generic %s not in generic_device_class %s",
                      node.generic, schema[const.DISC_GENERIC_DEVICE_CLASS])
        return False
    if (const.DISC_SPECIFIC_DEVICE_CLASS in schema and
            node.specific not in schema[const.DISC_SPECIFIC_DEVICE_CLASS]):
        _LOGGER.debug("node.specific %s not in specific_device_class %s",
                      node.specific, schema[const.DISC_SPECIFIC_DEVICE_CLASS])
        return False
    return True


def check_value_schema(value, schema):
    """Check if the value matches the passed value schema."""
    if (const.DISC_COMMAND_CLASS in schema and
            value.command_class not in schema[const.DISC_COMMAND_CLASS]):
        _LOGGER.debug("value.command_class %s not in command_class %s",
                      value.command_class, schema[const.DISC_COMMAND_CLASS])
        return False
    if (const.DISC_TYPE in schema and
            value.type not in schema[const.DISC_TYPE]):
        _LOGGER.debug("value.type %s not in type %s",
                      value.type, schema[const.DISC_TYPE])
        return False
    if (const.DISC_GENRE in schema and
            value.genre not in schema[const.DISC_GENRE]):
        _LOGGER.debug("value.genre %s not in genre %s",
                      value.genre, schema[const.DISC_GENRE])
        return False
    if (const.DISC_INDEX in schema and
            value.index not in schema[const.DISC_INDEX]):
        _LOGGER.debug("value.index %s not in index %s",
                      value.index, schema[const.DISC_INDEX])
        return False
    if (const.DISC_INSTANCE in schema and
            value.instance not in schema[const.DISC_INSTANCE]):
        _LOGGER.debug("value.instance %s not in instance %s",
                      value.instance, schema[const.DISC_INSTANCE])
        return False
    if const.DISC_SCHEMAS in schema:
        found = False
        for schema_item in schema[const.DISC_SCHEMAS]:
            found = found or check_value_schema(value, schema_item)
        if not found:
            return False

    return True


def node_name(node):
    """Return the name of the node."""
    return node.name or '{} {}'.format(
        node.manufacturer_name, node.product_name)
