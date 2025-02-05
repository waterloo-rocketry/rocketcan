# Auto generated file, do not edit directly

msg_prio = {
    'HIGHEST': 0x0,
    'HIGH':    0x1,
    'MEDIUM':  0x2,
    'LOW':     0x3
}

msg_type = {
    'GENERAL_BOARD_STATUS': 0x001,
    'RESET_CMD':            0x002,
    'DEBUG_RAW':            0x003,
    'CONFIG_SET':           0x004,
    'CONFIG_STATUS':        0x005,
    'ACTUATOR_CMD':         0x006,
    'ACTUATOR_ANALOG_CMD':  0x007,
    'ACTUATOR_STATUS':      0x008,
    'ALT_ARM_CMD':          0x009,
    'ALT_ARM_STATUS':       0x00A,
    'SENSOR_TEMP':          0x00B,
    'SENSOR_ALTITUDE':      0x00C,
    'SENSOR_LINEAR_ACC':    0x00D,
    'SENSOR_ANGULAR_VELO':  0x00E,
    'SENSOR_MAG':           0x010,
    'SENSOR_ANALOG':        0x011,
    'GPS_TIMESTAMP':        0x012,
    'GPS_LATITUDE':         0x013,
    'GPS_LONGITUDE':        0x014,
    'GPS_ALTITUDE':         0x015,
    'GPS_INFO':             0x016,
    'STATE_EST_DATA':       0x017,
    'LEDS_ON':              0x018,
    'LEDS_OFF':             0x019,
}

board_type_id = {
    'ANY':                  0x00,
    'INJ_SENSOR':           0x01,
    'CANARD_MOTOR':         0x02,
    'CAMERA':               0x03,
    'POWER':                0x04,
    'LOGGER':               0x05,
    'PROCESSOR':            0x06,
    'TELEMETRY':            0x07,
    'GPS':                  0x08,
    'SRAD_GNSS':            0x09,
    'ALTIMETER':            0x0A,
    'ARMING':               0x0B,
    'PAY_SENSOR':           0x40,
    'PAY_MOTOR':            0x41,
    'RLCS_GLS':             0x80,
    'RLCS_RELAY':           0x81,
    'RLCS_HEATING':         0x82,
    'DAQ':                  0x83,
    'CHARGING':             0x84,
    'THERMOCOUPLE':         0x85,
    'USB':                  0x86,
    'FYDP25_TVCA':          0xC0,
}

board_inst_id = {
    'ANY':        0x00,
    'GENERIC':    0x01,
    'INJ_A':       0x02,
    'INJ_B':       0x03,
    'VENT_A':      0x04,
    'VENT_B':      0x05,
    'VENT_C':      0x06,
    'VENT_D':      0x07,
    'RECOVERY':    0x08,
    'ROCKET':      0x09,
    'PAYLOAD':     0x0A,
    '1':           0x0B,
    '2':           0x0C,
    '3':           0x0D,
    '4':           0x0E,
}

board_status = {
    'E_NOMINAL':                 0x00,
}

actuator_id = {
    'ACTUATOR_VENT_VALVE':       0x00,
    'ACTUATOR_INJECTOR_VALVE':   0x01,
    'ACTUATOR_CAMERA_1':         0x02,
    'ACTUATOR_CAMERA_2':         0x03,
    'ACTUATOR_CANBUS':           0x04,
    'ACTUATOR_CHARGE':           0x05,
    'ACTUATOR_RADIO':            0x06,
}

actuator_state = {
    'ACTUATOR_ON':               0x00,
    'ACTUATOR_OFF':              0x01,
    'ACTUATOR_UNK':              0x02,
    'ACTUATOR_ILLEGAL':          0x03,
}

altimeter_id = {
    'ALTIMETER_RAVEN':           0x00,
    'ALTIMETER_STRATOLOGGER':    0x01,
    'ALTIMETER_SRAD':            0x02,
}

arm_state = {
    'ARM_STATE_DISARMED':        0x00,
    'ARM_STATE_ARMED':           0x01,
}

sensor_id = {
    'SENSOR_5V_CURR':            0x00,
    'SENSOR_BATT_CURR':          0x01,
    'SENSOR_BATT_VOLT':          0x02,
    'SENSOR_CHARGE_CURR':        0x03,
    'SENSOR_13V_CURR':           0x04,
    'SENSOR_MOTOR_CURR':         0x05,
    'SENSOR_GROUND_VOLT':        0x06,
    'SENSOR_PRESSURE_OX':        0x07,
    'SENSOR_PRESSURE_CC':        0x08,
    'SENSOR_PRESSURE_PNEUMATICS':0x09,
    'SENSOR_BARO':               0x0A,
    'SENSOR_ARM_BATT_1':         0x0B,
    'SENSOR_ARM_BATT_2':         0x0C,
    'SENSOR_MAG_1':              0x0D,
    'SENSOR_MAG_2':              0x0E,
    'SENSOR_VELOCITY':           0x0F,
    'SENSOR_VENT_TEMP':          0x10,
    'SENSOR_RADIO_CURR':         0x11,
    'SENSOR_PAYLOAD_TEMP_1':     0x12,
    'SENSOR_PAYLOAD_TEMP_2':     0x13,
}

state_est_id = {
    'STATE_POS_X':               0x00,
    'STATE_POS_Y':               0x01,
    'STATE_POS_Z':               0x02,
    'STATE_VEL_X':               0x03,
    'STATE_VEL_Y':               0x04,
    'STATE_VEL_Z':               0x05,
    'STATE_ACC_X':               0x06,
    'STATE_ACC_Y':               0x07,
    'STATE_ACC_Z':               0x08,
    'STATE_ANGLE_YAW':           0x09,
    'STATE_ANGLE_PITCH':         0x0A,
    'STATE_ANGLE_ROLL':          0x0B,
    'STATE_RATE_YAW':            0x0C,
    'STATE_RATE_PITCH':          0x0D,
    'STATE_RATE_ROLL':           0x0E,
}

