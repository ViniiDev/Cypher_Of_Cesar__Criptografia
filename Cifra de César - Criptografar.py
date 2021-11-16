print ('CIFRA DE CÉSAR')

print ("Sua Mensagem será Criptografada e guardada em um arquivo (TXT) !")

CRIPTOGRAFADO = 1;
DECRIPTOGRAFADO = 0;

def cesar (textos, chave, modo):  #função para fazer a troca do texto criptografado para o texto puro
    alfabeto = 'abcdefghijklmnopqrstuvwxyzáàãâéêóôõìùçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÂÃÉÊÕÔÌÙÇ,. ';
    novo_texto = '';
      
    for i in textos:
        indice = alfabeto.find(i);
        if indice == -1:
            novo_texto += i;
        else:
            novo_indice = indice + chave if modo == CRIPTOGRAFADO else indice - chave;
            novo_indice = novo_indice % len (alfabeto);
            novo_texto += alfabeto [novo_indice:novo_indice+1];
    return novo_texto;




chave = 5;
original = str(input('digite a mensagem a ser criptografada: '));
while len (original) > 128:     #verificar o tamanho da mensagem
    print('\nSUA MENSAGEM PASSOU O LIMITE DE CARACTERE');
    print('\nDigite uma nova mensagem com até 128 caracteres para ser criptografada \n');
    original = input ('digite a mensagem: ');
cifrado = cesar (original, chave, CRIPTOGRAFADO);
print ('\nEncriptada: ', cifrado);


with open("senha.txt","w") as arquivo:
    arquivo.write (str(cifrado))    #gravar a mensagem criptografada em um arquivo TXT