# CoreBond Nucleo Demo (Developer Preview)

Hardware-rooted device identity without stored keys.

This demo shows that a device can consistently prove its own identity, while a different device is rejected under the same conditions.

No stored keys. No key exchange. Identity is derived at runtime from the device itself.

---

## Run the Demo

Run from the repository root directory:

pip install numpy  
python run_demo.py  

---

## What You'll See

=== CoreBond Demo ===

Device A vs A: AUTHENTIC  
Device A vs B: REJECT  

- Same device → authenticates  
- Different device → rejected  

---

## What This Demonstrates

- Signals from the same device are consistent  
- Signals from different devices are distinguishable  
- Identity can be verified without stored keys  

This behavior has been observed across repeated runs with clear separation between legitimate and non-matching signals.

---

## Why This Matters

Traditional systems rely on stored secrets or key exchange.

CoreBond removes both.

With no stored keys, there is nothing to extract from memory.  
With no key exchange, there is nothing to intercept or replay.  

Identity is generated at runtime from the device itself.

---

## Test Conditions

- Repeated cold boot measurements  
- Identity derived from intrinsic device signal behavior  
- No stored credentials or persistent identity artifacts  
- Evaluation performed under identical conditions across devices  

---

## Observed Behavior

- Same device → consistent identity reproduction (~83%)  
- Different device → failed authentication under the same constraints  
- Clear separation between legitimate and non-matching signals  

---

## Prototype Status

This is an early-stage prototype intended to demonstrate core identity behavior.

Ongoing work includes:
- Improving identity reproducibility  
- Environmental testing (temperature, voltage, aging)  
- Expanded multi-device validation  
- Adversarial resistance testing  

---

## Work With Us

Exploring hardware-rooted identity for real-world systems?

CoreBond is currently in active prototype validation across physical devices.

Contact: intro@corebond.io
