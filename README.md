# CoreBond SDK (Developer Preview)

Device identity without stored secrets.

CoreBond demonstrates that device identity can be verified without storing or transmitting any secret material.

This prototype shows consistent identity behavior and clear separation between physical devices using intrinsic entropy signals.

---

## Run the Demo

Run from the repository root directory.

### Commands
pip install numpy  
python run_demo.py  

---

## Observed Behavior

=== CoreBond Demo ===

Device A vs A: AUTHENTIC  
Device A vs B: REJECT  

Run time: < 1 second. No setup beyond Python + NumPy.

---

## What This Demonstrates

- Signals from the same device are consistent  
- Signals from different devices are distinguishable  
- Identity can be verified without stored secrets  

This behavior has been observed across multiple physical devices with consistent separation between legitimate and non-matching signals under repeated cold boot conditions.

Environmental variation and long-term drift are active areas of ongoing validation.

---

## What This Is Not

- Not encryption  
- Not a key storage mechanism  
- Not a PUF library or wrapper  
- Not secure key exchange  

CoreBond does not protect secrets. It removes the need for them.

---

## Why This Matters

Most security systems assume secrets can be protected.

CoreBond assumes they will eventually be extracted.

Instead of defending stored credentials, CoreBond eliminates them:

- No secrets to steal  
- No secrets to rotate  
- No secrets to leak at scale  

Identity is derived from the physical device itself, not from stored or transmitted data.

This removes entire classes of key extraction and replay attacks.

---

## Work With Us

Exploring hardware-rooted identity for real-world systems?

CoreBond is currently in active prototype validation across physical devices.

If you're working on device security, IoT, or embedded systems, reach out:

intro@corebond.io

---

## License

This repository is provided solely for evaluation and demonstration purposes.

No use, copying, modification, distribution, or commercial exploitation of this code is permitted without prior written permission from CoreBond Technologies LLC.

All rights reserved.
