from notificador import Notificador

class NotificadorApp(Notificador):

    def notificar(self, mensagem):
        print(f"Mensagem enviada no app: {mensagem}")
