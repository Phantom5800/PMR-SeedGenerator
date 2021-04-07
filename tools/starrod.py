import shutil
import subprocess


# Run a shell command and yield lines of text as it prints anything out
def run(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline().decode("utf-8").strip().replace("> ", "")
        if output == "" and process.poll() is not None:
            break
        if output:
            yield output
    rc = process.poll()
    return rc

def sr_command(sr_path, command, console=True, display_error=True):
    print(command)
    for line in run(command):
        if console:
            print(line)
        elif display_error and line.startswith("ERROR"):
            print(line)
            console = True

def sr_dump(sr_path, console=True, display_error=True):
    command = f"{sr_path}StarRod.exe -DUMPASSETS"
    sr_command(sr_path, command, console, display_error)

def sr_copy(sr_path, console=True, display_error=True):
    command = f"{sr_path}StarRod.exe -COPYASSETS"
    sr_command(sr_path, command, console, display_error)

def sr_compile(sr_path, console=True, display_error=True):
    command = f"{sr_path}StarRod.exe -COMPILEMOD"
    sr_command(sr_path, command, console, display_error)