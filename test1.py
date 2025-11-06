import subprocess

def list_files_vulnerable(user_input_path):
    """
    Vulnerable: builds a shell command by concatenating untrusted input
    and runs it with shell=True.
    """
    # Unsafe: user_input_path can inject extra shell commands
    cmd = "ls -la " + user_input_path
    print("DEBUG vulnerable CMD:", cmd)
    # shell=True executes the entire string in a shell
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    # benign usage
    list_files_vulnerable("/tmp")

    # example of malicious-looking input (harmless echo used here to demonstrate)
    malicious = "/tmp; echo INJECTED_BY_ATTACKER"
    list_files_vulnerable(malicious)
