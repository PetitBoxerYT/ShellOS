# ShellOS

ShellOS is a modular application system designed to provide a premium multimedia interface running on top of Linux. It offers two main modes:

- **GameShell Mode**: console / retro / dev interface
- **CinemaShell Mode**: premium cinema interface with the MPV video player

ShellOS includes:
- a modular Core (services, APIs, session manager)
- an elegant BootShell for mode selection
- independent, clean, and extensible modes
- a simple installation system via `install.sh`

---

## 📦 Installation

ShellOS requires a Linux system (Debian/Ubuntu recommended).

```bash
sudo bash install.sh
```
Once installed:

```bash
shellos
```
To enable automatic startup:To enable automatic startup:

```bash
sudo systemctl enable shellos
```
