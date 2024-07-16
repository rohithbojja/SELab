import os
import subprocess
import threading

# Function to execute the command and print its output
def run_cmd(cmd: str):
    # Start the process
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # Print the PID of the process
    print(f"The PID of the process is: {process.pid}")
    print(os.sched_getaffinity(process.pid))  # Print initial affinity
    os.sched_setaffinity(process.pid, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11})  # Set affinity
    print(os.sched_getaffinity(process.pid))  # Print new affinity

    # Read the output line by line and print it
    for line in process.stdout:
        print(line.strip())

cmd = "/opt/llama.cpp/llama-server -m /opt/llama.cpp/unsloth.Q4_K_M.gguf --host 0.0.0.0 --port 11436 --chat-template chatml -t 12 -ngl 0 -ctk f16 --system-prompt-file /opt/llama.cpp/prompt_file.txt"

# Create a thread that runs the command
cmd_thread = threading.Thread(target=run_cmd, args=(cmd,))

# Start the thread
cmd_thread.start()

# Keep the script running
cmd_thread.join()
