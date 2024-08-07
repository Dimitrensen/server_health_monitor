import subprocess

def get_cpu_usage():
    result = subprocess.run(['./cpu_monitor.sh'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').strip()

if __name__ == "__main__":
    cpu_usage = get_cpu_usage()
    print(cpu_usage)
