import math, time
g=9.81
L=1.0
theta0=math.radians(45)
print("Pendulum AI Tracker by Rudra - JEE 2028")
for t in range(10):
    theta=theta0*math.cos(math.sqrt(g/L)*t)
    print(f"Time {t}s -> Angle {math.degrees(theta):.2f}°")
    time.sleep(0.5)