# leader-ssh-standard
Direct SSH connection wirtten by leader

# Lightweight Python SSH Command Execution Client

A robust, lightweight Python script leveraging the **Paramiko** library to automate remote command execution over the Secure Shell (SSH) protocol. This tool demonstrates core concepts of network security automation, structured exception handling, and standard I/O stream manipulation.

---

## 🚀 Features

* **Automated Host Key Verification:** Seamlessly handles unknown SSH host keys using `AutoAddPolicy` to prevent execution deadlocks in non-interactive environments.
* **Structured Exception Handling:** Features a robust `try-except-finally` architecture ensuring safe execution and guaranteed socket closure, preventing memory and port leaks.
* **Granular Stream Separation:** Separates system output (`stdout`) from error logs (`stderr`) for precise post-execution analysis.

---

## 🧠 How the Logic Works (Under the Hood)

1. **Client Initialization:** The script instantiates an SSH client object using `paramiko.SSHClient()`.
2. **Policy Configuration:** It bypasses the manual interactive prompt for untrusted host keys by enforcing an automated caching policy.
3. **Encrypted Handshake:** It establishes a secure, encrypted TCP tunnel to the specified target IP using the provided credentials.
4. **Command Execution:** The command is pushed through the secure channel. The remote server executes it within its native shell and channels the results back into three distinct standard streams (`stdin`, `stdout`, `stderr`).
5. **Data Decoding:** The script captures the raw bytes from the streams and decodes them into readable UTF-8 strings.
6. **Graceful Cleanup:** The `finally` block guarantees that the network socket is closed immediately after execution, regardless of whether the command succeeded or triggered an exception.

---

## 🛠️ Prerequisites

Before running the script, ensure you have Python 3.x installed along with the Paramiko library.

```bash
pip install paramiko
