## CoreBond Nucleo Demo (Developer Preview)

Hardware-rooted device identity without stored keys.

This demo shows a device recognizing itself and rejecting others under identical conditions.

No stored keys. No key exchange. Identity is derived at runtime from the device itself.

---

## Live Demo
[Download the demo video](https://github.com/CoreBond/corebond-nucleo-demo/raw/main/media/2026-04-20%2020-38-51.mp4)

---

## What This Demo Proves

- Same device produces consistent identity signals  
- Different devices produce distinguishable signals  
- Identity is derived at runtime, not stored  

## What This Demo Does Not Yet Prove

- Environmental stability (temperature, voltage variation)  
- Full challenge-response protocol  
- Replay resistance under adversarial conditions  
- Large-scale validation across many devices  

---

## Run the Demo

From the repository root:

pip install -r requirements.txt  
python run_demo.py  

---

## Expected Output

=== CoreBond Demo ===

Device A vs A: AUTHENTIC  
Device A vs B: REJECT  

Same device → authenticates  
Different device → rejected  

---

## Why This Matters

Traditional systems rely on stored secrets or key exchange.

CoreBond eliminates both.

- Nothing stored → nothing to extract  
- Nothing exchanged → nothing to intercept  

Identity becomes a property of the device, not something it holds.

---

## Test Conditions

- Repeated cold boot measurements  
- Identity derived from intrinsic device behavior  
- No stored credentials or persistent identity artifacts  
- Evaluation under identical conditions across devices  

---

## Observed Behavior

- Same device → consistent identity reproduction  
- Different device → failed authentication  
- Clear separation between legitimate and non-matching signals  

---

## Prototype Status

This is an early-stage prototype demonstrating core identity behavior.

Current work:
- Improving reproducibility  
- Environmental testing (temperature, voltage, aging)  
- Expanded multi-device validation  
- Adversarial resistance testing  

---

## Work With Us

Exploring hardware-rooted identity for real-world systems?

CoreBond is in active prototype validation across physical devices.

Contact: intro@corebond.io
