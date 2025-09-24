# Ocean-Disturbance-Data
This repository contains ocean disturbance data from Qixing Bay in Shenzhen and Eastern Bay in Huizhou, China. The data was collected by sensors such as RTK GPS, IMU, and anemometers installed on unmanned surface vessels (USVs). It is suitable for reference or analysis of disturbances experienced by USVs in the marine environment.
Here is a data sample of RTK GPS:

$GPGGA,022718.80,2234.03506362,N,11431.92532083,E,4,19,0.9,3.4038,M,-1.3415,M,00,0000*7F

$GPRMC,022718.80,A,2234.03506362,N,11431.92532083,E,0.009,115.3,051224,3.4,W,D*2E

$GNVTG,85.060,T,88.490,M,0.05259,N,0.09739,K,D*31

$GNHDT,234.0260,T*1A

The data above show a frame data of a RTK GPS, from which we can get the location and the altitude, flag indicating whether it is a differential signal, and so on.


Meanwhile, we simulated different water surface disturbance conditions in an indoor environment. We set up a water tank within a motion capture system, placed a floating platform inside the tank, and installed a robotic arm on the platform. Using a wave-making device developed in-house, we were able to induce swaying movements in the floating platform and the robotic arm. Furthermore, we attached marker points to the platform, the end effector of the robotic arm, and the base of the robotic arm, and constructed rigid bodies. This allowed us to simulate water surface sway in the indoor environment while simultaneously acquiring sway data of the floating platform and the robotic arm.
We collected over 100 hours of real-world data, covering three disturbance levels: no disturbance, slight disturbance, and moderate disturbance.
