#!/bin/bash

# Print current directory
echo "Current directory: $(pwd)"
echo "List of files in the current directory: $(ls)"

# Define the command
cmd="/llama-server -m /workspace/llama.cpp/unsloth.Q4_K_M.gguf --host 0.0.0.0 --port 11436 --chat-template chatml -t 12 -ngl 0 -ctk f16 "

# Start the process in the background
$cmd &

# Get the PID of the process
pid=$!
echo "The PID of the process is: $pid"

# Set CPU affinity (example: using CPUs 0-11)
taskset -cp 0-11 $pid

# Wait for the process to finish (not needed if running in background)
wait $pid
