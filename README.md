# MILITECH TRIANGULATION RX8  
*(Two-Point Not Precise Triangulation Script)*

**[MILITECH TRIANGULATION RX8]** is a lightweight Python script for quick target location tracking using two reference points.  
This script was used in old MILITECH R1-TURRETS VER.1 to locate targets within 58 meter range.

/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


**Read before use:**

[/] Must be used with **[MILITECH GRID-10 BEACONS]** or any precise **[RTK GPS Devices]**  
[/] Must be configured within provided application software of your device

> "Script is very old and chunky due to it can locate only using two points and it can lead to ghost targets appearing in the wrong place, sometimes right behind you. haha, don’t let it happen in real life choom."

<br>


**Key Features:**

[/] Rapid two point triangulation for target estimation  
[/] Lightweight and no-dependency platform compatibility  
[/] Integratable with MILITECH GRID sensor network and RTK GPS inputs


<br>



**Recommended Hardware:**

[/] MILITECH GRID-10 Beacons  
[/] RTK GPS Modules  
[/] Custom-built modules with at least 500cm range accuracy


<br>



**Usage and Installation:**

1. Clone the repository to your local machine  
2. Configure your calibrated MILITECH GRID-10 Beacons  
3. Run `usage.py` and input coordinates and distances for two locations (refer CLI MILITECH messages)  
4. Use the output for approximation of your target location (best used with **77-DRONE**)


⚠️ **Disclaimer:** This script provides fast estimations only. For critical targeting always use certified MILITECH hardware.

---

@SKANDHJERTE [SRX-EOF]
