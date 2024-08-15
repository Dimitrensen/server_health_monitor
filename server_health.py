import docker

def get_container_metrics(container_name):
    client = docker.from_env()
    container = client.containers.get(container_name)
    stats = container.stats(stream=False)

    cpu_usage = stats['cpu_stats']['cpu_usage']['total_usage']
    memory_usage = stats['memory_stats']['usage'] / (1024 * 1024)  # Convert to MB
    
    return cpu_usage, memory_usage

if __name__ == "__main__":
    container_name = "web-server"  # Assigned name of the Docker container
    cpu, mem = get_container_metrics(container_name)
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {mem} MB")