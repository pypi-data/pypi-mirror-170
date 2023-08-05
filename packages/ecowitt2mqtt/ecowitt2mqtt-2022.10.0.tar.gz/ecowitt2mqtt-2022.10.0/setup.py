# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ecowitt2mqtt',
 'ecowitt2mqtt.backports',
 'ecowitt2mqtt.helpers',
 'ecowitt2mqtt.helpers.calculator',
 'ecowitt2mqtt.helpers.publisher',
 'ecowitt2mqtt.util']

package_data = \
{'': ['*']}

install_requires = \
['asyncio-mqtt>=0.12.1',
 'colorlog>=6.6.0,<7.0.0',
 'fastapi>=0.85.0,<0.86.0',
 'meteocalc>=1.1.0,<2.0.0',
 'python-multipart>=0.0.5,<0.0.6',
 'rapidfuzz>=2.10.3,<3.0.0',
 'ruamel.yaml>=0.17.21,<0.18.0',
 'uvicorn>=0.18.0,<0.19.0',
 'uvloop>=0.17.0,<0.18.0',
 'voluptuous>=0.13.1,<0.14.0']

entry_points = \
{'console_scripts': ['ecowitt2mqtt = ecowitt2mqtt.__main__:main']}

setup_kwargs = {
    'name': 'ecowitt2mqtt',
    'version': '2022.10.0',
    'description': 'A small web server to send data from Ecowitt devices to an MQTT Broker',
    'long_description': '![ecowitt2mqtt](resources/logo-full.png)\n\n[![CI](https://github.com/bachya/ecowitt2mqtt/workflows/CI/badge.svg)](https://github.com/bachya/ecowitt2mqtt/actions)\n[![PyPi](https://img.shields.io/pypi/v/ecowitt2mqtt.svg)](https://pypi.python.org/pypi/ecowitt2mqtt)\n[![Docker Hub](https://img.shields.io/docker/pulls/bachya/ecowitt2mqtt)](https://hub.docker.com/r/bachya/ecowitt2mqtt)\n[![Version](https://img.shields.io/pypi/pyversions/ecowitt2mqtt.svg)](https://pypi.python.org/pypi/ecowitt2mqtt)\n[![License](https://img.shields.io/pypi/l/ecowitt2mqtt.svg)](https://github.com/bachya/ecowitt2mqtt/blob/main/LICENSE)\n[![Code Coverage](https://codecov.io/gh/bachya/ecowitt2mqtt/branch/dev/graph/badge.svg)](https://codecov.io/gh/bachya/ecowitt2mqtt)\n[![Maintainability](https://api.codeclimate.com/v1/badges/a03c9e96f19a3dc37f98/maintainability)](https://codeclimate.com/github/bachya/ecowitt2mqtt/maintainability)\n[![Say Thanks](https://img.shields.io/badge/SayThanks-!-1EAEDB.svg)](https://saythanks.io/to/bachya)\n\n<a href="https://www.buymeacoffee.com/bachya1208P" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>\n\n`ecowitt2mqtt` is a small CLI/web server that allows [Ecowitt](http://www.ecowitt.com)\ndevice data to be sent to an MQTT broker.\n\n- [Installation](#installation)\n- [Python Versions](#python-versions)\n- [Disclaimer](#disclaimer)\n- [Quick Start](#quick-start)\n- [Configuration](#configuration)\n  * [Command Line Options](#command-line-options)\n  * [Environment Variables](#environment-variables)\n  * [Configuration File](#configuration-file)\n  * [Merging Configuration Options](#merging-configuration-options)\n- [Advanced Usage](#advanced-usage)\n  * [Calculated Sensors](#calculated-sensors)\n  * [Battery Configurations](#battery-configurations)\n  * [Unit Systems](#unit-systems)\n  * [Raw Data](#raw-data)\n  * [Home Assistant](#home-assistant)\n  * [Running in the Background](#running-in-the-background)\n  * [Docker](#docker)\n- [Diagnostics](#diagnostics)\n- [Contributing](#contributing)\n\n# Installation\n\n```python\npip install ecowitt2mqtt\n```\n\n# Python Versions\n\n`ecowitt2mqtt` is currently supported on:\n\n* Python 3.8\n* Python 3.9\n* Python 3.10\n\n# Disclaimer\n\nThe datapoints within this library and documentation constitute estimates and are\nintended to help informed decision making. They should not replace analysis, advice, or\ndiagnosis from trained professionals. Use this data at your own discretion.\n\n# Quick Start\n\nNote that this README assumes that:\n\n* you have access to an MQTT broker.\n* you have already paired your Ecowitt device with the WS View Android/iOS app from\n  Ecowitt.\n\nFirst, install `ecowitt2mqtt` via `pip`:\n\n```bash\n$ pip install ecowitt2mqtt\n```\n\nThen, shift over to the WS View app on your Android/iOS device. While viewing your\ndevice in the app, select `Weather Services`:\n\n![Select Weather Services](https://raw.githubusercontent.com/bachya/ecowitt2mqtt/dev/assets/1-weather-services.jpeg?raw=true)\n\nPress `Next` until you reach the `Customized` screen:\n\n![The Customized screen in the WS View app](https://raw.githubusercontent.com/bachya/ecowitt2mqtt/dev/assets/2-customized.jpeg?raw=true)\n\nFill out the form with these values and tap `Save`:\n\n* `Protocol Type Same As`: `Ecowitt`\n* `Server IP / Hostname`: the IP address/hostname of the device running `ecowitt2mqtt`\n* `Path`: `/data/report/`\n* `Port`: `8080` (the default port on which `ecowitt2mqtt` is served)\n* `Upload Interval`: `60` (change this to alter the frequency with which data is published)\n\nThen, on the machine where you installed `ecowitt2mqtt`, run it:\n\n```bash\n$ ecowitt2mqtt \\\n    --mqtt-broker=192.168.1.101 \\\n    --mqtt-username=user \\\n    --mqtt-password=password \\\n    --mqtt-topic=ecowitt2mqtt/device_1\n```\n\nWithin the `Upload Interval`, data should begin to appear in the MQTT broker.\n\n# Configuration\n\n`ecowitt2mqtt` can be configured via command line options, environment variables, or a\n(YAML or JSON) config file.\n\n## Command Line Options\n\n```\nusage: ecowitt2mqtt [-h] [--version] [--battery-override BATTERY_OVERRIDE] [-c config]\n                    [--default-battery-strategy default_battery_strategy] [--diagnostics]\n                    [--disable-calculated-data] [-e endpoint] [--hass-discovery]\n                    [--hass-discovery-prefix hass_discovery_prefix]\n                    [--hass-entity-id-prefix hass_entity_id_prefix]\n                    [--input-unit-system input_unit_system] [-b mqtt_broker]\n                    [-p mqtt_password] [--mqtt-port mqtt_port] [--mqtt-retain] [--mqtt-tls]\n                    [-t mqtt_topic] [-u mqtt_username]\n                    [--output-unit-system output_unit_system] [--port port] [--raw-data] [-v]\n\nSend data from an Ecowitt gateway to an MQTT broker\n\noptions:\n  -h, --help            show this help message and exit\n  --version             show program\'s version number and exit\n  --battery-override BATTERY_OVERRIDE\n                        A battery configuration override (format: key,value)\n  -c config, --config config\n                        A path to a YAML or JSON config file\n  --default-battery-strategy default_battery_strategy\n                        The default battery config strategy to use (default: boolean)\n  --diagnostics         Output diagnostics\n  --disable-calculated-data\n                        Disable the output of calculated sensors\n  -e endpoint, --endpoint endpoint\n                        The relative endpoint/path to serve ecowitt2mqtt on (default:\n                        /data/report)\n  --hass-discovery      Publish data in the Home Assistant MQTT Discovery format\n  --hass-discovery-prefix hass_discovery_prefix\n                        The Home Assistant MQTT Discovery topic prefix to use (default:\n                        homeassistant)\n  --hass-entity-id-prefix hass_entity_id_prefix\n                        The prefix to use for Home Assistant entity IDs\n  --input-unit-system input_unit_system\n                        The input unit system used by the gateway (default: imperial)\n  -b mqtt_broker, --mqtt-broker mqtt_broker\n                        The hostname or IP address of an MQTT broker\n  -p mqtt_password, --mqtt-password mqtt_password\n                        A valid password for the MQTT broker\n  --mqtt-port mqtt_port\n                        The listenting port of the MQTT broker (default: 1883)\n  --mqtt-retain         Instruct the MQTT broker to retain messages\n  --mqtt-tls            Enable MQTT over TLS\n  -t mqtt_topic, --mqtt-topic mqtt_topic\n                        The MQTT topic to publish device data to\n  -u mqtt_username, --mqtt-username mqtt_username\n                        A valid username for the MQTT broker\n  --output-unit-system output_unit_system\n                        The output unit system used by the gateway (default: imperial)\n  --port port           The port to serve ecowitt2mqtt on (default: 8080)\n  --raw-data            Return raw data (don\'t attempt to translate any values)\n  -v, --verbose         Increase verbosity of logged output\n```\n\n## Environment Variables\n\n* `ECOWITT2MQTT_BATTERY_OVERRIDE`: a semicolon-delimited list of key=value battery overrides (default: `numeric`)\n* `ECOWITT2MQTT_CONFIG`: a path to a YAML or JSON config file (default: `None`)\n* `ECOWITT2MQTT_DEFAULT_BATTERY_STRATEGY`: the default battery config strategy to use (default: `boolean`)\n* `ECOWITT2MQTT_DIAGNOSTICS`: whether to output diagnostics (default: `false`)\n* `ECOWITT2MQTT_DISABLE_CALCULATED_DATA`: whether to disable the output of calculated sensors (default: `false`)\n* `ECOWITT2MQTT_ENDPOINT`: the relative endpoint/path to serve ecowitt2mqtt on (default: `/data/report`)\n* `ECOWITT2MQTT_HASS_DISCOVERY_PREFIX`: the Home Assistant discovery prefix to use (default: `homeassistant`)\n* `ECOWITT2MQTT_HASS_DISCOVERY`: publish data in the Home Assistant MQTT Discovery format Idefault: `false`)\n* `ECOWITT2MQTT_HASS_ENTITY_ID_PREFIX`: the prefix to use for Home Assistant entity IDs (default: `""`)\n* `ECOWITT2MQTT_INPUT_UNIT_SYSTEM`: the input unit system used by the device (default: `imperial`)\n* `ECOWITT2MQTT_MQTT_BROKER`: the hostname or IP address of an MQTT broker\n* `ECOWITT2MQTT_MQTT_PASSWORD`: a valid password for the MQTT broker\n* `ECOWITT2MQTT_MQTT_PORT`: the listenting port of the MQTT broker (default: `1883`)\n* `ECOWITT2MQTT_MQTT_RETAIN`: whether to instruct the MQTT broker to retain messages (default: `false`)\n* `ECOWITT2MQTT_MQTT_TLS`: publish data via MQTT over TLS (default: `false`)\n* `ECOWITT2MQTT_MQTT_TOPIC`: the MQTT topic to publish device data to\n* `ECOWITT2MQTT_MQTT_USERNAME`: a valid username for the MQTT broker\n* `ECOWITT2MQTT_OUTPUT_UNIT_SYSTEM`: the unit system to use in output (default: `imperial`)\n* `ECOWITT2MQTT_PORT`: the port to serve ecowitt2mqtt on (default: `8080`)\n* `ECOWITT2MQTT_RAW_DATA`: return raw data (don\'t attempt to translate any values) (default: `false`)\n* `ECOWITT2MQTT_VERBOSE`: increase verbosity of logged output (default: `false`)\n\n## Configuration File\n\nThe configuration file can be formatted as either YAML:\n\n```yaml\n---\nbattery_override:\n  battery_key1: boolean\ndefault_battery_strategy: numeric\ndiagnostics: false\ndisable_calculated_data: false\nendpoint: /data/report\nhass_discovery: false\nhass_discovery_prefix: homeassistant\nhass_entity_id_prefix: test_prefix\ninput_unit_system: imperial\nmqtt_broker: 127.0.0.1\nmqtt_password: password\nmqtt_port: 1883\nmqtt_retain: false\nmqtt_tls: false\nmqtt_topic: Test\nmqtt_username: user\noutput_unit_system: imperial\nport: 8080\nraw_data: false\nverbose: false\n```\n\n...or JSON\n\n\n```json\n{\n  "battery_override": {\n    "battery_key1": "boolean"\n  },\n  "default_battery_strategy": "numeric",\n  "diagnostics": false,\n  "disable_calculated_data": false,\n  "endpoint": "/data/report",\n  "hass_discovery": false,\n  "hass_discovery_prefix": "homeassistant",\n  "hass_entity_id_prefix": "test_prefix"\n  "input_unit_system": "imperial",\n  "mqtt_broker": "127.0.0.1",\n  "mqtt_password": "password",\n  "mqtt_port": 1883,\n  "mqtt_retain": true,\n  "mqtt_tls": false,\n  "mqtt_topic": "Test",\n  "mqtt_username": "user",\n  "output_unit_system": "imperial",\n  "port": 8080,\n  "raw_data": false,\n  "verbose": false\n}\n```\n\n### Multiple Gateways\n\nWhen using the configuration file, it is possible to define specific configuration\nparameters for multiple Ecowitt gateways. This is useful if different gateways should\npublish to different MQTT brokers, in different formats, etc.\n\nFirst, you must determine the unique ID for each gateway. This can be observed in the\nlogs when `verbose` is enabled – look for the `PASSKEY` value that the gateway has:\n\n```\nReceived data from the Ecowitt device: {\'PASSKEY\': \'abcde12345\', ...}\n```\n\nThen, in the configuration file, simply add a `gateways` key that contains a mapping of any\nof the existing configuration options. Options that remain at the root level of the file\nare treated as defaults.\n\nFor example, this YAML configuration file:\n\n```yaml\n---\nmqtt_broker: 127.0.0.1\nmqtt_password: password\nmqtt_topic: Test\nmqtt_username: user\n\ngateways:\n  abcde12345:\n    hass_discovery: true\n```\n\n...defines two gateway definitions:\n\n* One that publishes to the `Test` topic on an MQTT broker at `127.0.0.1`\n* One (with a `PASSKEY` of `abcde12345`) that publishes to the same broker, but in Home\n  Assistant MQTT Discovery format.\n\nIn another example, this JSON configuration file:\n\n```json\n{\n  "mqtt_broker": "127.0.0.1",\n  "mqtt_password": "password",\n  "mqtt_port": 1883,\n  "mqtt_topic": "Test",\n  "mqtt_username": "user",\n  "gateways": {\n    "abcde12345": {\n      "mqtt_broker": "192.168.1.100",\n      "mqtt_retain": true,\n      "output_unit_system": "metric"\n    }\n  }\n}\n```\n\n...defines two gateway definitions:\n\n* One that publishes to the `Test` topic on an MQTT broker at `127.0.0.1`\n* One (with a `PASSKEY` of `abcde12345`) that publishes to a different broker\n  (`192.168.1.100`), outputs the data in metric, and retains the data on the broker\n\n## Merging Configuration Options\n\nWhen parsing configuration options, `ecowitt2mqtt` looks at the configuration sources in\nthe following order:\n\n1. Configuration File (Specific Gateway)\n2. Configuration File (Defaults)\n3. Environment Variables\n4. CLI Options\n\nThis allows you to mix and match sources – for instance, you might have "defaults" in\nthe configuration file and override them via environment variables.\n\n\n# Advanced Usage\n\n## Calculated Sensors\n\nIn addition to the data coming from a gateway, `ecowitt2mqtt` will automatically deduce\nand published several additional, calculated data points if the requisite underlying\ndata exists:\n\n* **[Absolute Humidity](https://en.wikipedia.org/wiki/Humidity#Absolute_humidity):** the actual volume of water vapor in the air\n* **[Beaufort Scale](https://en.wikipedia.org/wiki/Beaufort_scale):** the empirical measure that relates wind speed to observed conditions at sea or on land\n* **[Dew Point](https://en.wikipedia.org/wiki/Dew_point):** the temperature to which air must be cooled to become saturated with water vapor, assuming constant air pressure and water content\n* **[Feels Like](https://en.wikipedia.org/wiki/Heat_index):** how hot or how cold the air feels to the human body when factoring in variables such as relative humidity, wind speeds, the amount of sunshine, etc.\n* **[Frost Point](https://en.wikipedia.org/wiki/Dew_point#Frost_point):** the temperature below 32°F (0°C) at which moisture in the air will condense as a layer of frost on exposed surfaces that are also at a temperature below the frost point\n* **[Frost Risk](https://en.wikipedia.org/wiki/Dew_point#Frost_point):** how likely the formation of frost is (based on the `frostpoint`)\n* **[Heat Index](https://en.wikipedia.org/wiki/Heat_index):** how hot the air feels to the human body when factoring in relative humidity (applicable when the apparent temperature is higher than the air temperature)\n* **[Safe Exposure Times](https://www.openuv.io/kb/skin-types-safe-exposure-time-calculation/):** how long different skin types can be in the sun (unprotected) before burning begins according to the [Fitzpatrick Scale](https://en.wikipedia.org/wiki/Fitzpatrick_scale)\n* **Solar Radiation (lux):** the detected solar radiation illuminance calculated in lux\n* **Solar Radiation (%):** the percentage of detected solar radiation illuminance as perceived by the human eye\n* **[Simmer Index](http://summersimmer.com/ssi_page2.htm):** an alternative to heat index that describes how how the air feels to the human body in relatively dry environments\n* **Simmer Zone:** a human-friendly interpretation of the Simmer Index\n* **Thermal Perception:** a human-friendly interpretation of the Dew Point\n* **[Wind Chill](https://en.wikipedia.org/wiki/Wind_chill):** how cold the air feels to the human body when factoring in relative humidity, wind speed, etc. (applicable when the apparent temperature is lower than the air temperature)\n\nIf you would prefer to not have these sensors calculated and published, you can utilize\nthe `--disable-calculated-data` configuration option.\n\n## Battery Configurations\n\nEcowitt devices report battery levels in three different formats:\n\n* `boolean`: `0` represents `OFF` (i.e., the battery is in normal condition) and `1`\n   represents `ON` (i.e., the battery is low).\n* `numeric`: the raw numeric value is interpreted as the number of volts remaining in\n   the battery.\n* `percentage`: the raw numeric value is interpreted as the percentage of voltage\n   remaining the battery.\n\n`ecowitt2mqtt` provides three mechanisms to handle this complexity:\n\n1. A built-in mapping of all currently known battery types to their assumed strategy\n2. A default battery strategy for unknown battery types\n3. User-defined battery strategy overrides\n\n### Built-in Mapping\n\n`ecowitt2mqtt` contains an internal mapping that should automatically transform all\nknown battery types into their correct format.\n\n### Default Battery Strategy\n\nBy using the `--default-battery-strategy` configuration parameter, users can specify how\nunknown battery types should be treated by default.\n\n### Battery Overrides\n\nIndividual batteries can be overridden and given a new strategy. How this is\naccomplished differs slightly based on the configuration method used:\n\n* Command Line Options: provide one or more `--battery-override "batt1=boolean"` options\n* Environment Variables: provide a `ECOWITT2MQTT_BATTERY_OVERRIDE` variable that is a\n  semicolon-delimited pair of "key=value" strings (e.g.,\n  `ECOWITT2MQTT_BATTERY_OVERRIDE="batt1=boolean;batt2=numeric"`)\n* Config File: include a dictionary of key/value pairs in either YAML or JSON format\n\nThese overrides work on both known and unknown battery types; that said, if you should\nfind the need to override a known battery type because `ecowitt2mqtt` has an incorrect\ninternal interpretation, submit an issue to get it corrected!\n\n### Example\n\nIn this example, a user mostly has batteries that should be treated as `boolean`, but\nalso has one – `wh60_batt1` – that should be treated as numeric.\n\n#### Command Line Options\n\n```\n$ ecowitt2mqtt --default-battery-strategy boolean --battery-override="wh60_batt1=numeric"\n```\n\n#### Environment Variables\n\n```\n$ ECOWITT2MQTT_DEFAULT_BATTERY_STRATEGY=boolean \\\n  ECOWITT2MQTT_BATTERY_OVERRIDE="wh60_batt1=numeric" \\\n  ecowitt2mqtt\n```\n\n#### Config File\n\nIn YAML:\n\n```yaml\n---\ndefault_battery_strategy: boolean\nbattery_override:\n  wh60_batt1: numeric\n```\n\n...or JSON\n\n```json\n{\n  "default_battery_strategy": "boolean",\n  "battery_override": {\n    "wh60_batt1": "numeric"\n  }\n}\n```\n\n## Unit Systems\n\n`ecowitt2mqtt` allows you to specify both the input and output unit systems for a device.\nThis is fairly self-explanatory, but take care to use an `--input-unit-system` that is\nconsistent with what your device provides (otherwise, your data will be very "off").\n\n## Raw Data\n\nIn some cases, it may be preferable to prevent `ecowitt2mqtt` from doing any data\ntranslation (converting values to a new unit system, changing binary values – such as\nmight be used by a battery – into "friendly" values, etc.). Passing the `--raw-data` flag\nwill accomplish this: data will flow directly from the Ecowitt device to the MQTT broker\nas-is.\n\nNote that the `--raw-data` flag supersedes any that might cause data translation (such as\n`--input-unit-system` or `--output-unit-system`).\n\n## Home Assistant\n\n### MQTT Discovery\n\n[Home Assistant](https://home-assistant.io) users can quickly add entities from an\nEcowitt device by using\n[MQTT Discovery](https://www.home-assistant.io/docs/mqtt/discovery/).\n\nOnce Home Assistant is configured to accept MQTT Discovery, `ecowitt2mqtt` simply needs\nthe `--hass-discovery` flag:\n\n```bash\n$ ecowitt2mqtt \\\n    --mqtt-broker=192.168.1.101 \\\n    --mqtt-username=user \\\n    --mqtt-password=password \\\n    --hass-discovery\n```\n\nNote that if both `--hass-discovery` and `--mqtt-topic` are provided, `--hass-discovery` will\nwin out.\n\n### Custom Entity ID Prefix\n\nYou can provide a custom prefix for all Home Assistant entities via the\n`--hass-entity-id-prefix` config parameter.\n\n### Home Assistant OS Add-on\n\nHome Assistant OS users can install the official `ecowitt2mqtt` add-on by clicking the\nlink below:\n\n[![Open this add-on in your Home Assistant instance.][addon-badge]][addon]\n\n## Running in the Background\n\n`ecowitt2mqtt` doesn\'t, itself, provide any sort of daemonization mechanism. The suggested\nroute is to use a different application.\n\n### `supervisord`\n\nAn example `supervisord` configuration file might look like this:\n\n```\n[supervisord]\nnodaemon=true\nloglevel=info\nuser=root\n\n[program:ecowitt2mqtt]\ncommand=ecowitt2mqtt --mqtt-broker=192.168.1.101 --mqtt-username=user --mqtt-password=password\nstdout_logfile=/dev/stdout\nstdout_logfile_maxbytes=0\nredirect_stderr=true\n```\n\n### `systemd`\n\nAn example `systemd` service file in `/etc/systemd/system` might look like this:\n\n```\n[Unit]\nDescription=ECOWITT2MQTT daemon\nAfter=network.target\n\n[Service]\nType=simple\nExecStart=ecowitt2mqtt --mqtt-broker=192.168.1.101 --mqtt-username=user --mqtt-password=password\nExecReload=kill -HUP $MAINPID\nKillMode=process\nRestart=on-failure\nRestartSec=5s\n\n[Install]\nWantedBy=multi-user.target\n```\n\nTo enable the service:\n\n```bash\n$ systemctl enable ecowitt2mqtt\n```\n\n## Docker\n\nThe library is available via a Docker image\n([`bachya/ecowitt2mqtt`](https://hub.docker.com/r/bachya/ecowitt2mqtt)). It is configured\nby using the same environment variables listed [above](#environment-variables).\n\nRunning the image is straightforward:\n\n```\ndocker run -it \\\n    -e ECOWITT2MQTT_MQTT_BROKER=192.168.1.101 \\\n    -e ECOWITT2MQTT_MQTT_USERNAME=user \\\n    -e ECOWITT2MQTT_MQTT_PASSWORD=password \\\n    -p 8080:8080 \\\n    bachya/ecowitt2mqtt:latest\n```\n\nNote the value of the `-p` flag: you must expose the port defined by the `PORT`\nenvironment variable. In the example above, the default port (`8080`) is used and is\nexposed via the same port on the host.\n\n[`docker-compose`](https://docs.docker.com/compose/) users can find an example\nconfiguration file at\n[`docker-compose.dev.yml`](https://github.com/bachya/ecowitt2mqtt/blob/dev/docker-compose.dev.yml).\nNote that this is intended to be a dev environment for quickly testing the repo itself;\nin production, you should refer to one of the\n[Docker Hub](https://hub.docker.com/r/bachya/ecowitt2mqtt) images.\n\n# Diagnostics\n\nYou may run `ecowitt2mqtt` in diagnostics mode by providing the `--diagnostics` flag. In\nthis mode, the app will wait until it receives and publishes a single payload, then\nexit. This allows users to collect a small-but-complete payload for use in testing,\ndebugging, and issue reporting.\n\n# Contributing\n\n1. [Check for open features/bugs](https://github.com/bachya/ecowitt2mqtt/issues)\n  or [initiate a discussion on one](https://github.com/bachya/ecowitt2mqtt/issues/new).\n2. [Fork the repository](https://github.com/bachya/ecowitt2mqtt/fork).\n3. (_optional, but highly recommended_) Create a virtual environment: `python3 -m venv .venv`\n4. (_optional, but highly recommended_) Enter the virtual environment: `source ./.venv/bin/activate`\n5. Install the dev environment: `script/setup`\n6. Code your new feature or bug fix.\n7. Write tests that cover your new functionality.\n8. Run tests and ensure 100% code coverage: `nox -rs coverage`\n9. Update `README.md` with any new documentation.\n10. Add yourself to `AUTHORS.md`.\n11. Submit a pull request!\n\n[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg\n[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=c35f0383_ecowitt2mqtt&repository_url=https%3A%2F%2Fgithub.com%2Fbachya%2Fhome-assistant-addons\n',
    'author': 'Aaron Bach',
    'author_email': 'bachya1208@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bachya/ecowitt2mqtt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
