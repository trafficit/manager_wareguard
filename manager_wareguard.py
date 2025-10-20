#!/usr/bin/env python3
import gi
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class WireGuardManager(Gtk.Window):
    def __init__(self):
        super().__init__(title="ワイヤーガード・マネージャー")
        self.set_border_width(20)
        self.set_default_size(420, 320)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0.05, 0.05, 0.1, 1))

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.add(vbox)

        header = Gtk.Label()
        header.set_markup("<span font='18' weight='bold' foreground='#00ffff'>🧬 ワイヤーガード制御ノード</span>")
        header.set_justify(Gtk.Justification.CENTER)
        vbox.pack_start(header, False, False, 10)

        self.actions = [
            ("⚡  接続開始 ( INIT LINK )", "sudo wg-quick up wg0"),
            ("⚔️  接続終了 ( TERMINATE )", "sudo wg-quick down wg0 || true"),
            ("🧾  設定編集 ( CONFIG )", "sudo nano /etc/wireguard/wg0.conf"),
            ("🛰️  IP確認 ( TRACE )", "curl -4 https://ipinfo.io; sleep 6"),
            ("🧿  自動起動 ( AUTOSTART )", "sudo systemctl enable wg-quick@wg0"),
            ("📶  状態確認 ( STATUS )", "sudo wg show; sleep 6")
        ]

        for label, cmd in self.actions:
            btn = Gtk.Button(label=label)
            btn.set_size_request(240, 42)
            btn.get_style_context().add_class("suggested-action")
            btn.connect("clicked", self.run_command, cmd)
            vbox.pack_start(btn, False, False, 0)

    def run_command(self, widget, command):
        wrapped_cmd = f"bash -c '{command}'"
        subprocess.Popen(["x-terminal-emulator", "-e", wrapped_cmd])

def main():
    Gtk.init()
    win = WireGuardManager()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
