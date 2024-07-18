import os
import subprocess
import threading
import argparse

# Function to execute the command and print its output
def run_cmd(llama_cpp_path: str, model_path: str, prompt_file_path: str):
    cmd = f"{llama_cpp_path}/llama-server -m {model_path} --host 0.0.0.0 --port 11436 --chat-template chatml -t 12 -ngl 0 -ctk f16 --system-prompt-file {prompt_file_path}"
    
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

# Parse command line arguments
parser = argparse.ArgumentParser(description="Run llama-server with specified paths")
parser.add_argument("--l", required=False, help="Path to the llama.cpp directory",defualt="/workspace/llama.cpp")
parser.add_argument("--m", required=False, help="Path to the model file",default="/workspace/llama.cpp/unsloth.Q4_K_M.gguf")
parser.add_argument("--p", required=False, help="Path to the prompt file",default="/workspace/llama.cpp/prompt_file.txt")

args = parser.parse_args()

# Create a thread that runs the command
cmd_thread = threading.Thread(target=run_cmd, args=(args.l, args.m, args.p))

# Start the thread
cmd_thread.start()

# Keep the script running
cmd_thread.join()
