from mcstatus import MinecraftServer
from settings import SERVER_IP
from formatter import format_player_list

class Server:
    def __init__(self):
        self.server = MinecraftServer.lookup(SERVER_IP)
    
    def ping(self):
        try:
            return self.server.ping()
        except:
            return None

    def status(self):
        try:
            return self.server.status()
        except:
            return None

    

if __name__ == "__main__":
    server = Server()
    status = server.status().players
    print(format_player_list(status))
