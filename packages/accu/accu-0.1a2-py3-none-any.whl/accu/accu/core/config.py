"""Helper functions for loading InvenTree configuration options."""

import os
import random
import shutil
import string
from pathlib import Path

import yaml

from .helpers.logging import LOGGER
from .utils import get_base_dir


def get_config_file(create=True) -> Path:
    """Returns the path of the InvenTree configuration file.

    Note: It will be created it if does not already exist!
    """
    base_dir = get_base_dir()

    cfg_filename = os.getenv("INVENTREE_CONFIG_FILE")

    if cfg_filename:
        cfg_filename = Path(cfg_filename.strip()).resolve()
    else:
        # Config file is *not* specified - use the default
        cfg_filename = base_dir.joinpath("config.yaml").resolve()

    if not cfg_filename.exists() and create:
        print(
            "InvenTree configuration file 'config.yaml' not found - creating default file"
        )

        cfg_template = base_dir.joinpath("config_template.yaml")
        shutil.copyfile(cfg_template, cfg_filename)
        print(f"Created config file {cfg_filename}")

    return cfg_filename


def load_config_data() -> map:
    """Load configuration data from the config file."""

    cfg_file = get_config_file()

    with open(cfg_file, "r") as cfg:
        data = yaml.safe_load(cfg)

    return data


def get_setting(env_var=None, config_key=None, default_value=None, typecast=None):
    """Helper function for retrieving a configuration setting value.

    - First preference is to look for the environment variable
    - Second preference is to look for the value of the settings file
    - Third preference is the default value

    Arguments:
        env_var: Name of the environment variable e.g. 'INVENTREE_STATIC_ROOT'
        config_key: Key to lookup in the configuration file
        default_value: Value to return if first two options are not provided
        typecast: Function to use for typecasting the value
    """

    def try_typecasting(value):
        """Attempt to typecast the value"""
        if typecast is not None:
            # Try to typecast the value
            try:
                return typecast(value)
            except Exception as error:
                LOGGER.error(
                    f"Failed to typecast '{env_var}' with value '{value}' to type '{typecast}' with error {error}"
                )
        return value

    # First, try to load from the environment variables
    if env_var is not None:
        val = os.getenv(env_var, None)

        if val is not None:
            return try_typecasting(val)

    # Next, try to load from configuration file
    if config_key is not None:
        cfg_data = load_config_data()

        result = None

        # Hack to allow 'path traversal' in configuration file
        for key in config_key.strip().split("."):

            if type(cfg_data) is not dict or key not in cfg_data:
                result = None
                break

            result = cfg_data[key]
            cfg_data = cfg_data[key]

        if result is not None:
            return try_typecasting(result)

    # Finally, return the default value
    return try_typecasting(default_value)


def get_settings_dir(reference: str, create=True):
    """Return the absolute path for a directory."""

    dir = get_setting(f"INVENTREE_{reference.upper()}", reference)

    if not dir:
        raise FileNotFoundError(f"{reference} not specified")

    dir_path = Path(dir).resolve()

    if create:
        dir_path.mkdir(parents=True, exist_ok=True)

    return dir_path


def get_plugin_file():
    """Returns the path of the InvenTree plugins specification file.

    Note: It will be created if it does not already exist!
    """

    # Check if the plugin.txt file (specifying required plugins) is specified
    plugin_file = get_setting("INVENTREE_PLUGIN_FILE", "plugin_file")

    if not plugin_file:
        # If not specified, look in the same directory as the configuration file
        config_dir = get_config_file().parent
        plugin_file = config_dir.joinpath("plugins.txt")
    else:
        # Make sure we are using a modern Path object
        plugin_file = Path(plugin_file)

    if not plugin_file.exists():
        LOGGER.warning(
            "Plugin configuration file does not exist - creating default file"
        )
        LOGGER.info(f"Creating plugin file at '{plugin_file}'")

        # If opening the file fails (no write permission, for example), then this will throw an error
        plugin_file.write_text(
            "# InvenTree Plugins (uses PIP framework to install)\n\n"
        )

    return plugin_file


def get_secret_key():
    """Return the secret key value which will be used by django.

    Following options are tested, in descending order of preference:

    A) Check for environment variable INVENTREE_SECRET_KEY => Use raw key data
    B) Check for environment variable INVENTREE_SECRET_KEY_FILE => Load key data from file
    C) Look for default key file "secret_key.txt"
    D) Create "secret_key.txt" if it does not exist
    """

    # Look for environment variable
    if secret_key := get_setting("INVENTREE_SECRET_KEY", "secret_key"):
        LOGGER.info("SECRET_KEY loaded by INVENTREE_SECRET_KEY")  # pragma: no cover
        return secret_key

    # Look for secret key file
    if secret_key_file := get_setting("INVENTREE_SECRET_KEY_FILE", "secret_key_file"):
        secret_key_file = Path(secret_key_file).resolve()
    else:
        # Default location for secret key file
        secret_key_file = get_base_dir().joinpath("secret_key.txt").resolve()

    if not secret_key_file.exists():
        LOGGER.info(f"Generating random key file at '{secret_key_file}'")

        # Create a random key file
        options = string.digits + string.ascii_letters + string.punctuation
        key = "".join([random.choice(options) for i in range(100)])
        secret_key_file.write_text(key)

    LOGGER.info(f"Loading SECRET_KEY from '{secret_key_file}'")

    key_data = secret_key_file.read_text().strip()

    return key_data


def get_custom_file(
    env_ref: str, conf_ref: str, log_ref: str, lookup_media: bool = False
):
    """Returns the checked path to a custom file.

    Set lookup_media to True to also search in the media folder.
    """
    from django.contrib.staticfiles.storage import StaticFilesStorage
    from django.core.files.storage import default_storage

    value = get_setting(env_ref, conf_ref, None)

    if not value:
        return None

    static_storage = StaticFilesStorage()

    if static_storage.exists(value):
        LOGGER.info(f"Loading {log_ref} from static directory: {value}")
    elif lookup_media and default_storage.exists(value):
        LOGGER.info(f"Loading {log_ref} from media directory: {value}")
    else:
        add_dir_str = " or media" if lookup_media else ""
        LOGGER.warning(
            f"The {log_ref} file '{value}' could not be found in the static{add_dir_str} directories"
        )
        value = False

    return value
