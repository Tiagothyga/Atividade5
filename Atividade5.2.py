#Faça um programa que leia 4 notas de um aluno, salve as em uma lista e calcule a média das notas.

print("Bem Vindo ☺️")
nome = input ("Digite o nome do aluno: ")
nota1 = float(input ("Digite a primeira nota: "))
nota2 = float(input ("Digite a segunda nota: "))
nota3 = float(input ("Digite a terceira nota: "))
nota4 = float(input ("Digite a quarta nota: "))

tabela = [nota1,nota2,nota3,nota4]
x = (nota1 + nota2 + nota3 + nota4) / 4
print ("O resoltado de:", nome.capitalize(), "é:")
print ("Primeira nota:", nota1, "pontos")
print ("Segunda nota: ", nota2, "pontos")
print ("Terceira nota:", nota3, "pontos")
print ("Quarta nota:  ", nota4, "pontos")
print ("A lista com as respctivas notas são:", (tabela[0:]))
print ("A nota média de" , nome.capitalize(), "é de", x, "pontos")