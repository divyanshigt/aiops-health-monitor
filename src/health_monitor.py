def check_cpu(cpu):
    if not isinstance(cpu, (int, float)):
        raise TypeError("cpu must be a number")
    return cpu < 80


def check_memory(memory):
    if not isinstance(memory, (int, float)):
        raise TypeError("memory must be a number")
    return memory < 80


def check_disk(disk):
    if not isinstance(disk, (int, float)):
        raise TypeError("disk must be a number")
    return disk < 90


def check_service(status):
    if not isinstance(status, str):
        raise TypeError("status must be a string")
    return status.lower() == "running"


def system_health(cpu, memory, disk, service):
    return (
        check_cpu(cpu)
        and check_memory(memory)
        and check_disk(disk)
        and check_service(service)
    )


def generate_alert(cpu, memory, disk, service):
    if system_health(cpu, memory, disk, service):
        return "System Healthy"
    return "Alert: System requires attention"