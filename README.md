# manager_wareguard

WireGuard Manager (GTK GUI)  Japan Style
WireGuard Manager is a lightweight GTK-based graphical interface for managing WireGuard VPN connections on Linux. Designed for speed, clarity, and minimalism, it allows users to control VPN sessions, view status, and edit configuration files—all from a neon-themed GUI.
______
Features
  Start/Stop VPN: One-click control of wg-quick up/down

  IP Trace: Check public IP via curl with auto-close delay

  Status View: Display current WireGuard session info

  Config Editor: Launch nano to edit wg0.conf

  Autostart Toggle: Enable systemd autostart for wg-quick@wg0

<img width="429" height="488" alt="image" src="https://github.com/user-attachments/assets/286f90b4-054a-465f-b0eb-646bebf07e69" />

Requirements
Python 3

GTK 3 (python3-gi)

WireGuard installed (wg, wg-quick)

RUN
./manager_wireguard.py
