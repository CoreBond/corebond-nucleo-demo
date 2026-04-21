from verify import compare_signals, load_signal

print("=== CoreBond Demo ===\n")

a1 = load_signal("deviceA_run1.txt")
a2 = load_signal("deviceA_run2.txt")
b1 = load_signal("deviceB_run1.txt")

print("Device A vs A:", compare_signals(a1, a2))
print("Device A vs B:", compare_signals(a1, b1))