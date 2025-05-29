#Ver se uma palavra é polidromo
def polidromo(text):
    text_clear = ''
    for char in text:
        if char.isalnum():
            text_clear += char.lower()
    return text_clear == text_clear [::-1]

def main():
    palavra = input("Digite uma palavra: ")
    if polidromo(palavra):
        print("Sim")
    else:
        print("Não")

main()