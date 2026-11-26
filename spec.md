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

### Principles
- Readability over size. Optimization is not a concern in the yaml.
- Be explicit everywhere

### SID (29 bits)
- `type: message_type` picks the message from `messages`.
- `type: metadata` is decoded with that message's own `metadata` spec.
- `metadata: null` means the byte is unused. Treated as a numeric in Parsley and whatever is sent is just ignored.
