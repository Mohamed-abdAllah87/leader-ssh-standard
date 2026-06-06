import paramiko

def ssh_command(ip, user, passwd, command):

    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:

        print(f"[*] connecting to {ip} >>>")

        client.connect(ip, username=user, password=passwd, timeout=10)

        stdin, stdout, stderr = client.exec_command(command)

        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print("[*] command output: ")
            print(f"[*] Command Output:\n{output}")
    
        if error:
            print("[-] command error: ")
            print(error)

    except Exception as e:
        print(f"[-] connection failed: {e}")
    finally:

        client.close()
