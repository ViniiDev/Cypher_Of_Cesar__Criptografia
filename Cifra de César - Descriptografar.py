print ('CIFRA DE CÉSAR')

print ("O arquivo TXT criado, será decriptado ! ")

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

def msg():  #função para ler o arquivo TXT 
    with open ('senha.txt', 'r') as arquivo:
        for senha in arquivo:
            return senha

decriptografado = msg() #variavel recebe o valor da função MSG, no caso o texto criptografado

texto = cesar (decriptografado, chave, DECRIPTOGRAFADO);  #texto recebe o valor que está na função cesar
print ('\nMensagem Decripitada: ', texto);