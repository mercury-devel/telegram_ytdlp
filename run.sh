#!/bin/bash

# Function to display the menu
show_menu() {
    echo "Select an action:"
    echo "1. Build"
    echo "2. Create and start container"
    echo "3. Stop container"
    echo "4. Restart container"
    echo "5. Remove container"
    echo "6. Show container logs"
    echo "7. Exit"
}

# Function to perform the build command
build_image() {
    echo "Building image..."
    docker build -t savefrom .
}

# Function to create and start the container
create_and_run_container() {
    echo "Creating and starting container..."
    docker run -d --name savefrom --env-file .env savefrom
}

# Function to stop the container
stop_container() {
    echo "Stopping container..."
    docker stop savefrom
}

# Function to restart the container
restart_container() {
    echo "Restarting container..."
    docker start savefrom
}

# Function to remove the container
remove_container() {
    echo "Removing container..."
    docker rm savefrom
}

# Function to show container logs
show_logs() {
    echo "Container logs..."
    docker logs savefrom
}

# Main program loop
while true; do
    show_menu
    read -p "Enter the number of the action: " choice
    case $choice in
        1) build_image ;;
        2) create_and_run_container ;;
        3) stop_container ;;
        4) restart_container ;;
        5) remove_container ;;
        6) show_logs ;;
        7) echo "Exiting..."; exit 0 ;;
        *) echo "Invalid choice. Please enter a number between 1 and 7." ;;
    esac
    echo ""
done
