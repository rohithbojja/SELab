#!/bin/bash

# Print current directory
echo "Current directory: $(pwd)"
echo "List of files in the current directory: $(ls)"

# Default values
host="0.0.0.0"
port="11436"
model_path="/workspace/llama.cpp/unsloth.Q4_K_M.gguf"
threads="12"
cache_type_k="f16"
chat_template="chatml"

# Parse arguments
while [[ $# -gt 0 ]]; do
    key="$1"

    case $key in
        -h|--host)
        host="$2"
        shift
        shift
        ;;
        -p|--port)
        port="$2"
        shift
        shift
        ;;
        -m|--model)
        model_path="$2"
        shift
        shift
        ;;
        -t|--threads)
        threads="$2"
        shift
        shift
        ;;
        -ctk|--cache-type-k)
        cache_type_k="$2"
        shift
        shift
        ;;
        --chat-template)
        chat_template="$2"
        shift
        shift
        ;;
        *)
        # unknown option
        shift
        ;;
    esac
done

# Define the command
cmd="/llama-server -m \"$model_path\" --host \"$host\" --port \"$port\" --chat-template \"$chat_template\" -t \"$threads\" -ctk \"$cache_type_k\""

# Start the process in the background
$cmd &

# Get the PID of the process
pid=$!
echo "The PID of the process is: $pid"

# Set CPU affinity (example: using CPUs 0-11)
taskset -cp 0-11 $pid

# Wait for the process to finish (not needed if running in background)
wait $pid
