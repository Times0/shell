import subprocess


def execute_command(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error occurred: {stderr.decode()}")
    else:
        print(stdout.decode())


while True:
    command = input("> ")
    if command.lower() == "exit":
        break
    execute_command(command)
