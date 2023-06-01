#!/bin/bash

# Set the default command for the container
CMD="jupyter notebook"

# Add custom options to the command
CMD+=" --ip=0.0.0.0"
CMD+=" --no-browser"
CMD+=" --allow-root"
CMD+=" --NotebookApp.token=root"
CMD+=" --NotebookApp.password=root"

# Execute the command
exec $CMD "$@"
