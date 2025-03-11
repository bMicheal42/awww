import subprocess

commands = [
    {
        "event": "RT-KBNA-101",
        "service": "Kibana",
        "text": "Ошибок сервиса Retention.Api уровня Fatal в 2 раза больше тренда",
        "severity": "critical"
    },
    {
        "event": "rt-ipt-mgarb-07",
        "service": "Mongo Arbiter",
        "text": "System time is out of sync (diff with Zabbix server > 3m)",
        "severity": "minor"
    },
    {
        "event": "rt-ipt-mgarb-07",
        "service": "Mongo Arbiter",
        "text": "System time is out of sync (diff with Zabbix server > 3m)",
        "severity": "minor"
    },
    {
        "event": "RETN rt-exosrmq-103",
        "service": "RabbitMQ",
        "text": "Сообщений в очереди retention:Exo.SMTP.Gateway.command.exo.smtp.message.send..marketing больше нормы",
        "severity": "minor"
    },
    {
        "event": "	rt-k8s-svc-117",
        "service": "Kubernetes",
        "text": "Load average is too high (per CPU load over 5 for 15m)",
        "severity": "minor"
    },
    {
        "event": "	rt-k8s-svc-118",
        "service": "Kubernetes",
        "text": "Load average is too high (per CPU load over 5 for 15m)",
        "severity": "minor"
    },
    {
        "event": "	rt-k8s-svc-119",
        "service": "Kubernetes",
        "text": "Load average is too high (per CPU load over 5 for 15m)",
        "severity": "minor"
    },
    {
        "event": "	rt-k8s-svc-120",
        "service": "Kubernetes",
        "text": "Load average is too high (per CPU load over 5 for 15m)",
        "severity": "minor"
    }
]

base_command = [
    "docker", "exec", "-t", "alerta-api-1", "alerta", "send", "-r", "RETN", "-v", "ERROR", "-E", "Production"
]

# Функция для выполнения команды с параметрами
def run_command(params):
    command = base_command + [
        "-e", params["event"],
        "-S", params["service"],
        "-t", params["text"],
        "-s", params["severity"]
    ]
    subprocess.run(command)

for params in commands:
    run_command(params)
