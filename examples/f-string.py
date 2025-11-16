from datetime import datetime

number = 12345678
pi = 3.13
real = 86.25
full = 100
now = datetime.now()

print(f"Numbers: {number:020}")       # Numbers: 00000000000012345678
print(f"Numbers: {number:0^20}")      # Numbers: 00000012345678000000
print(f"Numbers: {number:0<20}")      # Numbers: 12345678000000000000
print(f"Numbers: {number:0>20}")      # Numbers: 00000000000012345678
print(f"Numbers: {number:=^20}")      # Numbers: 00000000000012345678
print(f"Pi: {pi:.4f}")                # Pi: 3.1300
print(f"Min: {min(number, pi)}")      # Min: 3.13
print(f"Res: {real/full:.0%}")        # Real: 86%
print(f"Date: {now:%Y-%m-%d %H:%M}")  # Date: 2024-11-16 14:35
