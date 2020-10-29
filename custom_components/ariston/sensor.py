"""Suppoort for Ariston sensors."""
import logging
from datetime import timedelta

from homeassistant.const import CONF_NAME, CONF_SENSORS
from homeassistant.helpers.entity import Entity

from .const import (
    DATA_ARISTON,
    DEVICES,
    PARAM_ACCOUNT_CH_GAS,
    PARAM_ACCOUNT_CH_ELECTRICITY,
    PARAM_ACCOUNT_DHW_GAS,
    PARAM_ACCOUNT_DHW_ELECTRICITY,
    PARAM_CH_ANTIFREEZE_TEMPERATURE,
    PARAM_CH_MODE,
    PARAM_CH_SET_TEMPERATURE,
    PARAM_CH_COMFORT_TEMPERATURE,
    PARAM_CH_ECONOMY_TEMPERATURE,
    PARAM_CH_DETECTED_TEMPERATURE,
    PARAM_CH_PROGRAM,
    PARAM_COOLING_LAST_24H,
    PARAM_COOLING_LAST_7D,
    PARAM_COOLING_LAST_30D,
    PARAM_COOLING_LAST_365D,
    PARAM_ERRORS,
    PARAM_ERRORS_COUNT,
    PARAM_DHW_COMFORT_FUNCTION,
    PARAM_DHW_MODE,
    PARAM_DHW_SET_TEMPERATURE,
    PARAM_DHW_STORAGE_TEMPERATURE,
    PARAM_DHW_COMFORT_TEMPERATURE,
    PARAM_DHW_ECONOMY_TEMPERATURE,
    PARAM_MODE,
    PARAM_OUTSIDE_TEMPERATURE,
    PARAM_HEATING_LAST_24H,
    PARAM_HEATING_LAST_7D,
    PARAM_HEATING_LAST_30D,
    PARAM_HEATING_LAST_365D,
    PARAM_SIGNAL_STRENGTH,
    PARAM_WATER_LAST_24H,
    PARAM_WATER_LAST_7D,
    PARAM_WATER_LAST_30D,
    PARAM_WATER_LAST_365D,
    PARAM_UNITS,
    PARAM_THERMAL_CLEANSE_CYCLE,
    PARAM_DHW_PROGRAM,
    PARAM_GAS_TYPE,
    PARAM_GAS_COST,
    PARAM_ELECTRICITY_COST,
    VALUE,
    UNITS,
)

SCAN_INTERVAL = timedelta(seconds=2)

STATE_AVAILABLE = "available"

SENSOR_ACCOUNT_CH_GAS = "Account CH Gas Use"
SENSOR_ACCOUNT_CH_ELECTRICITY = "Account CH Electricity Use"
SENSOR_ACCOUNT_DHW_GAS = "Account DHW Gas Use"
SENSOR_ACCOUNT_DHW_ELECTRICITY = "Account DHW Electricity Use"
SENSOR_CH_ANTIFREEZE_TEMPERATURE = "CH Antifreeze Temperature"
SENSOR_CH_DETECTED_TEMPERATURE = "CH Detected Temperature"
SENSOR_CH_MODE = "CH Mode"
SENSOR_CH_SET_TEMPERATURE = "CH Set Temperature"
SENSOR_CH_PROGRAM = "CH Time Program"
SENSOR_CH_COMFORT_TEMPERATURE = "CH Comfort Temperature"
SENSOR_CH_ECONOMY_TEMPERATURE = "CH Economy Temperature"
SENSOR_COOLING_LAST_24H = "Energy use for Cooling in last 24 hours"
SENSOR_COOLING_LAST_7D = "Energy use for Cooling in last 7 days"
SENSOR_COOLING_LAST_30D = "Energy use for Cooling in last 30 days"
SENSOR_COOLING_LAST_365D = "Energy use for Cooling in last 365 days"
SENSOR_DHW_COMFORT_FUNCTION = "DHW Comfort Function"
SENSOR_DHW_PROGRAM = "DHW Time Program"
SENSOR_DHW_SET_TEMPERATURE = "DHW Set Temperature"
SENSOR_DHW_STORAGE_TEMPERATURE = "DHW Storage Temperature"
SENSOR_DHW_COMFORT_TEMPERATURE = "DHW Comfort Temperature"
SENSOR_DHW_ECONOMY_TEMPERATURE = "DHW Economy Temperature"
SENSOR_DHW_MODE = "DHW Mode"
SENSOR_ERRORS = "Active Errors"
SENSOR_HEATING_LAST_24H = "Energy use for Heating in last 24 hours"
SENSOR_HEATING_LAST_7D = "Energy use for Heating in last 7 days"
SENSOR_HEATING_LAST_30D = "Energy use for Heating in last 30 days"
SENSOR_HEATING_LAST_365D = "Energy use for Heating in last 365 days"
SENSOR_MODE = "Mode"
SENSOR_OUTSIDE_TEMPERATURE = "Outside Temperature"
SENSOR_SIGNAL_STRENGTH = "Signal Strength"
SENSOR_WATER_LAST_24H = "Energy use for Water in last 24 hours"
SENSOR_WATER_LAST_7D = "Energy use for Water in last 7 days"
SENSOR_WATER_LAST_30D = "Energy use for Water in last 30 days"
SENSOR_WATER_LAST_365D = "Energy use for Water in last 365 days"
SENSOR_UNITS = "Units of Measurement"
SENSOR_THERMAL_CLEANSE_CYCLE = "Thermal Cleanse Cycle"
SENSOR_GAS_TYPE = "Gas Type"
SENSOR_GAS_COST = "Gas Cost"
SENSOR_ELECTRICITY_COST = "Electricity Cost"

_LOGGER = logging.getLogger(__name__)

# Sensor types are defined like: Name, units, icon
SENSORS = {
    PARAM_ACCOUNT_CH_GAS: [SENSOR_ACCOUNT_CH_GAS, "mdi:cash"],
    PARAM_ACCOUNT_DHW_GAS: [SENSOR_ACCOUNT_DHW_GAS, "mdi:cash"],
    PARAM_ACCOUNT_CH_ELECTRICITY: [SENSOR_ACCOUNT_CH_ELECTRICITY, "mdi:cash"],
    PARAM_ACCOUNT_DHW_ELECTRICITY: [SENSOR_ACCOUNT_DHW_ELECTRICITY, "mdi:cash"],
    PARAM_CH_ANTIFREEZE_TEMPERATURE: [SENSOR_CH_ANTIFREEZE_TEMPERATURE, "mdi:radiator"],
    PARAM_CH_DETECTED_TEMPERATURE: [SENSOR_CH_DETECTED_TEMPERATURE, "mdi:thermometer"],
    PARAM_CH_MODE: [SENSOR_CH_MODE, "mdi:radiator"],
    PARAM_CH_SET_TEMPERATURE: [SENSOR_CH_SET_TEMPERATURE, "mdi:radiator"],
    PARAM_CH_PROGRAM: [SENSOR_CH_PROGRAM, "mdi:calendar-month"],
    PARAM_CH_COMFORT_TEMPERATURE: [SENSOR_CH_COMFORT_TEMPERATURE, "mdi:radiator"],
    PARAM_CH_ECONOMY_TEMPERATURE: [SENSOR_CH_ECONOMY_TEMPERATURE, "mdi:radiator"],
    PARAM_COOLING_LAST_24H: [SENSOR_COOLING_LAST_24H, "mdi:cash"],
    PARAM_COOLING_LAST_7D: [SENSOR_COOLING_LAST_7D, "mdi:cash"],
    PARAM_COOLING_LAST_30D: [SENSOR_COOLING_LAST_30D, "mdi:cash"],
    PARAM_COOLING_LAST_365D: [SENSOR_COOLING_LAST_365D, "mdi:cash"],
    PARAM_DHW_PROGRAM: [SENSOR_DHW_PROGRAM, "mdi:calendar-month"],
    PARAM_DHW_COMFORT_FUNCTION: [SENSOR_DHW_COMFORT_FUNCTION, "mdi:water-pump"],
    PARAM_DHW_SET_TEMPERATURE: [SENSOR_DHW_SET_TEMPERATURE, "mdi:water-pump"],
    PARAM_DHW_STORAGE_TEMPERATURE: [SENSOR_DHW_STORAGE_TEMPERATURE, "mdi:water-pump"],
    PARAM_DHW_COMFORT_TEMPERATURE: [SENSOR_DHW_COMFORT_TEMPERATURE, "mdi:water-pump"],
    PARAM_DHW_ECONOMY_TEMPERATURE: [SENSOR_DHW_ECONOMY_TEMPERATURE, "mdi:water-pump"],
    PARAM_DHW_MODE: [SENSOR_DHW_MODE, "mdi:water-pump"],
    PARAM_ERRORS_COUNT: [SENSOR_ERRORS, "mdi:alert-outline"],
    PARAM_HEATING_LAST_24H: [SENSOR_HEATING_LAST_24H, "mdi:cash"],
    PARAM_HEATING_LAST_7D: [SENSOR_HEATING_LAST_7D, "mdi:cash"],
    PARAM_HEATING_LAST_30D: [SENSOR_HEATING_LAST_30D, "mdi:cash"],
    PARAM_HEATING_LAST_365D: [SENSOR_HEATING_LAST_365D, "mdi:cash"],
    PARAM_MODE: [SENSOR_MODE, "mdi:water-boiler"],
    PARAM_OUTSIDE_TEMPERATURE: [SENSOR_OUTSIDE_TEMPERATURE, "mdi:thermometer"],
    PARAM_SIGNAL_STRENGTH: [SENSOR_SIGNAL_STRENGTH, "mdi:signal"],
    PARAM_WATER_LAST_24H: [SENSOR_WATER_LAST_24H, "mdi:cash"],
    PARAM_WATER_LAST_7D: [SENSOR_WATER_LAST_7D, "mdi:cash"],
    PARAM_WATER_LAST_30D: [SENSOR_WATER_LAST_30D, "mdi:cash"],
    PARAM_WATER_LAST_365D: [SENSOR_WATER_LAST_365D, "mdi:cash"],
    PARAM_UNITS: [SENSOR_UNITS, "mdi:scale-balance"],
    PARAM_THERMAL_CLEANSE_CYCLE: [SENSOR_THERMAL_CLEANSE_CYCLE, "mdi:update"],
    PARAM_GAS_TYPE: [SENSOR_GAS_TYPE, "mdi:gas-cylinder"],
    PARAM_GAS_COST: [SENSOR_GAS_COST, "mdi:cash"],
    PARAM_ELECTRICITY_COST: [SENSOR_ELECTRICITY_COST, "mdi:cash"],
}


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up a sensor for Ariston."""
    if discovery_info is None:
        return

    name = discovery_info[CONF_NAME]
    device = hass.data[DATA_ARISTON][DEVICES][name]
    add_entities(
        [
            AristonSensor(name, device, sensor_type)
            for sensor_type in discovery_info[CONF_SENSORS]
        ],
        True,
    )


class AristonSensor(Entity):
    """A sensor implementation for Ariston."""

    def __init__(self, name, device, sensor_type):
        """Initialize a sensor for Ariston."""
        self._name = "{} {}".format(name, SENSORS[sensor_type][0])
        self._signal_name = name
        self._api = device.api.ariston_api
        self._sensor_type = sensor_type
        self._state = None
        self._attrs = {}
        self._icon = SENSORS[sensor_type][1]

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self._attrs

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        if self._sensor_type == PARAM_ERRORS_COUNT:
            try:
                if self._api.sensor_values[PARAM_ERRORS_COUNT][VALUE] == 0:
                    return "mdi:shield"
            except KeyError:
                pass
        return self._icon

    @property
    def unit_of_measurement(self):
        """Return the units of measurement."""
        try:
            return self._api.sensor_values[self._sensor_type][UNITS]
        except KeyError:
            return None

    @property
    def available(self):
        """Return True if entity is available."""
        return (
            self._api.available
            and not self._api.sensor_values[self._sensor_type][VALUE] is None
        )

    def update(self):
        """Get the latest data and updates the state."""
        try:
            if not self._api.available:
                return
            if not self._api.sensor_values[self._sensor_type][VALUE] is None:
                if self._sensor_type in {PARAM_CH_PROGRAM, PARAM_DHW_PROGRAM}:
                    if self._api.sensor_values[self._sensor_type][VALUE] != {}:
                        self._state = STATE_AVAILABLE
                    else:
                        self._state = None
                else:
                    self._state = self._api.sensor_values[self._sensor_type][VALUE]
            else:
                self._state = None

            self._attrs = {}
            if self._sensor_type in {
                PARAM_CH_SET_TEMPERATURE,
                PARAM_DHW_SET_TEMPERATURE,
            }:
                try:
                    self._attrs["Min"] = self._api.supported_sensors_set_values[
                        self._sensor_type
                    ]["min"]
                    self._attrs["Max"] = self._api.supported_sensors_set_values[
                        self._sensor_type
                    ]["max"]
                except KeyError:
                    self._attrs["Min"] = None
                    self._attrs["Max"] = None

            elif self._sensor_type == PARAM_ERRORS_COUNT:
                if not self._api.sensor_values[PARAM_ERRORS][VALUE] is None:
                    for valid_error in self._api.sensor_values[PARAM_ERRORS][VALUE]:
                        self._attrs[valid_error] = ""

            elif self._sensor_type in {
                PARAM_HEATING_LAST_24H,
                PARAM_WATER_LAST_24H,
                PARAM_COOLING_LAST_24H,
                PARAM_HEATING_LAST_7D,
                PARAM_WATER_LAST_7D,
                PARAM_COOLING_LAST_7D,
                PARAM_HEATING_LAST_30D,
                PARAM_WATER_LAST_30D,
                PARAM_COOLING_LAST_30D,
                PARAM_HEATING_LAST_365D,
                PARAM_WATER_LAST_365D,
                PARAM_COOLING_LAST_365D,
            }:
                list_param = self._sensor_type + "_list"
                self._attrs = self._api.sensor_values[list_param][VALUE]

            elif self._sensor_type in {PARAM_CH_PROGRAM, PARAM_DHW_PROGRAM}:
                if not self._api.sensor_values[self._sensor_type][VALUE] is None:
                    self._attrs = self._api.sensor_values[self._sensor_type][VALUE]
        except KeyError:
            _LOGGER.warning("Problem updating sensors for Ariston")
