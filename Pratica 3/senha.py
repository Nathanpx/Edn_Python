import re
import random

# Função para verificar se a senha é forte


def verificar_senha(senha):
    # Senha deve ter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula, um número e um caractere especial
    if (len(senha) >= 8 and
        re.search(r'[A-Z]', senha) and
        re.search(r'[a-z]', senha) and
        re.search(r'[0-9]', senha) and
            re.search(r'[\W_]', senha)):
        return True
    return False

# Função para gerar mensagem aleatória caso a pessoa não queira mais criar a senha


def gerar_mensagem_aleatoria():
    mensagens = [
        "Ah, entendi! Vou deixar a senha de lado por enquanto. 😅",
        "Ok, sem problema! Se mudar de ideia, estarei aqui! 😉",
        "Parece que você não está pronto para criar uma senha agora. 😌",
        "A senha pode esperar! Tome seu tempo. ⏳",
        "Nada como um descanso para a mente. A senha vai ficar para depois! 😎"
    ]
    return random.choice(mensagens)

# Função principal


def main():
    while True:
        senha = input("Digite uma nova senha (ou 'sair' para desistir): ")

        if senha.lower() == 'sair':
            print(gerar_mensagem_aleatoria())
            break

        if verificar_senha(senha):
            print("Senha forte! ✅")
        else:
            print("Senha fraca. Tente novamente com uma senha mais forte (min. 8 caracteres, maiúsculas, minúsculas, números e caracteres especiais).")


# Iniciar o programa
if __name__ == "__main__":
    main()
