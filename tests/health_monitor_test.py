import pytest

from src.health_monitor import (
    check_cpu,
    check_memory,
    check_disk,
    check_service,
    system_health,
    generate_alert
)


def test_check_cpu():
    assert check_cpu(50) == True


def test_check_memory():
    assert check_memory(60) == True


def test_check_disk():
    assert check_disk(70) == True


def test_check_service():
    assert check_service("running") == True


def test_system_health():
    assert system_health(50, 60, 70, "running") == True


def test_cpu_type_error():
    with pytest.raises(TypeError):
        check_cpu("high")


def test_memory_type_error():
    with pytest.raises(TypeError):
        check_memory("high")


def test_disk_type_error():
    with pytest.raises(TypeError):
        check_disk("high")


def test_service_type_error():
    with pytest.raises(TypeError):
        check_service(123)


def test_generate_alert():
    assert generate_alert(50, 60, 70, "running") == "System Healthy"


def test_generate_alert_failure():
    assert generate_alert(95, 60, 70, "running") == "Alert: System requires attention"