### RocketCAN Priorities
Highest: 
- Flight Critical commands: Any commands that safety critical
    -  ex: RA/RPC Commands
- Flight Critical Telem: Must be received to launch
    - ex: RA/RPC Telem

High:
- Mission Critical Commands: Any commands that will need to received to have success of critical systems
    - ex: Ox injector valve open, camera/payload turn on and off cmds
- Timing Critical Mission Critical Telem: Messages that will cause certain system failure without this data
    - ex: GPS/mag/baro can msgs from GPS board to controls

Medium:
- Mission Critical Telem: 
    - ex: board health and critical system stats

Low:
- Rest of the messages:
    - Sensor data, non-critical system states…