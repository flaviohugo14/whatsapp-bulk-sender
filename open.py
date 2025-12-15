import platform
import shlex
import subprocess

directory = "/tmp/chrome-whatsapp-bulk-sender"
port = 9222

os_name = platform.system()

if os_name == "Darwin":  # macOS
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = (
        f'"{chrome_path}" --user-data-dir="{directory}" --remote-debugging-port={port}'
    )

elif os_name == "Windows":
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    cmd = (
        f'"{chrome_path}" --user-data-dir="{directory}" --remote-debugging-port={port}'
    )

elif os_name == "Linux":
    chrome_path = "google-chrome"
    cmd = f'{chrome_path} --user-data-dir="{directory}" --remote-debugging-port={port}'

else:
    raise RuntimeError(f"Sistema operacional não suportado: {os_name}")

subprocess.Popen(shlex.split(cmd))
