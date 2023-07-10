from typing import Union
from fastapi import WebSocket
from fastapi import FastAPI
import json
import websockets



app = FastAPI()





class SubscriptionManager:
    def allow_subscription(self, message):
        data = json.loads(message)


        if data in ["estudiante", "otro_tipo"]:
            # Realizar acciones para permitir la suscripción
            return True
        else:
            # Realizar acciones para denegar la suscripción
            return False






class WebSocketSubscriptionRequest:
    subscription_key: str

    def __init__ (self,app,pather):
        self.pather = pather
        self.subcription = []

        @app.websocket(self.pather)
        def accept_ws_request(websocket: websockets.WebSocketServerProtocol):
            websocket.accept()

            while True:
                try:
                    data = await websocket.receive_text()
                    subcripciones_cumplidas = []
                    for subcription in self.subcriptions:
                        # Verificar verificar los tipos q contiene el data para permitir la subcripcion
                        if subcription(data):
                            subcripciones_cumplidas.append(subcription)
                            return callback(subcripciones_cumplidas)

                except websockets.exceptions.ConnectionClosedOK:
                    break





myWsApp = WebSocketSubscriptionRequest(app,"ws")

@myWsApp.subscripe(
    lambda data: data.get("value")>0
)






def callback(self,):
    # segun el data sera el tipo de  mesanje
    # los cuae sseran dos para empezar
    self.send_message(

    )
    pass

# def subb_callback(suscripciones):
#     for suscripcion in suscripciones:
#         if isinstance(suscripcion, Estudiante):
#             # Realiza acciones para suscripciones de estudiantes
#             enviar_mensaje_estudiante(suscripcion)
#         elif isinstance(suscripcion, Mensaje):
#             # Realiza acciones para suscripciones de mensajes
#             enviar_mensaje(suscripcion)
#         else:
#             # Acciones para otros tipos de suscripciones
#             realizar_acciones(suscripcion)

# def sub_callback(suscripciones):
#     for key, value in suscripciones.items():
#         if key == "estudiante":
#             # Realiza acciones para suscripciones de estudiantes
#             enviar_mensaje_estudiante(value)
#         elif key == "mensaje":
#             # Realiza acciones para suscripciones de mensajes
#             enviar_mensaje(value)
#         else:
#             # Acciones para otros tipos de suscripciones
#             realizar_acciones(value)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
