# CoreBond SDK (Developer Preview)

Hardware-rooted device identity without stored secrets.

CoreBond provides hardware-rooted device identity without stored secrets.

This developer preview demonstrates:
- Device-level entropy signals  
- Identity comparison  
- Replay-resistant verification  

---

## Run the Demo

Run from the repository root directory.

### Commands

pip install numpy  
python run_demo.py  

### Expected Output

=== CoreBond Demo ===

Device A vs A: AUTHENTIC  
Device A vs B: REJECT  

Run time: < 1 second. No setup beyond Python + NumPy.

---

## What This Shows

- Signals from the same device are consistent  
- Signals from different devices are distinguishable  
- Identity can be verified without stored keys  

This behavior has been observed across multiple physical devices with consistent separation between legitimate and non-matching signals under repeated cold boot conditions.

---

## Why This Matters

Traditional systems rely on stored secrets or transmitted keys.

CoreBond demonstrates a different model:
- No stored keys  
- No key exchange  
- Identity derived from physical device characteristics  

This model eliminates dependence on stored credentials entirely.

This removes entire classes of key extraction and replay attacks.

---

## Next Steps

For access to extended SDK capabilities and integration guidance:

Visit: https://corebond.io

---

## License

This repository is provided solely for evaluation and demonstration purposes.

No use, copying, modification, distribution, or commercial exploitation of this code is permitted without prior written permission from CoreBond Technologies LLC.

All rights reserved.
