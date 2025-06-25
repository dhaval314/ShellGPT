import shlex
import subprocess

DANGEROUS_KEYWORDS = ["rm", "shutdown", "reboot", "mkfs", ":(){", "dd", "wget", "curl", "--no-preserve-root"]

def is_safe(command):
    for keyword in DANGEROUS_KEYWORDS:
        if keyword in command:
            return False
    return True

def run_command(command):
    if not is_safe(command):
        print("[!] Command flagged as potentially dangerous. Not executing.")
        return

    print("[i] Running command...\n")
    try:
        result = subprocess.run(shlex.split(command), capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print("[!] Error while executing:", e)
