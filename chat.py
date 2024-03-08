# Titulo: HashZap
# Botão de iniciar chat 
    # clicou no botão;
    # popup / modal
        # Titulo: Bem vindo ao HashZap
        # Campo: Escreva seu nome
        # Botão: entrar no chat
# Chat
# Campo de digitar a mensagem
# Botão de enviar


import flet as ft

def main(pagina):
    texto = ft.Text("HashZap")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        print(mensagem)
        # Adicione a mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        # Limpe o campo mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua Mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    def entrar_chat(evento):
        print("Entrar no chat")
        # Fechar o popup
        popup.open = False
        # Tirar o botão iniciar chat
        pagina.remove(botao_iniciar)
        # Tirar o titulo HashZap
        pagina.remove(texto)
        # Criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all((f"{nome_usuario.value} entrou no chat"))
        # Colocar o botão de digitar mensagem
        pagina.add(linha_enviar)
        pagina.update()


    titulo_popup = ft.Text("Bem Vindo ao HashZap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target = main, view=ft.WEB_BROWSER)