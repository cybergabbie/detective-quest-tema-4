print("=== DETECTIVE QUEST - TEMA 4 ===")

print("Você é o detetive responsável por identificar o principal suspeito.")
print("Responda às perguntas abaixo com 's' para sim ou 'n' para não.\n")

arma = input("O suspeito foi visto carregando uma arma? (s/n): ")
local = input("O suspeito estava perto do local do crime? (s/n): ")
motivo = input("O suspeito tinha motivo para cometer o crime? (s/n): ")

print("\n--- Resultado da Investigação ---")

if arma == "s" and local == "s" and motivo == "s":
    print("O suspeito é o MAIS provável autor do crime.")
elif local == "s" and motivo == "s":
    print("O suspeito é fortemente suspeito.")
elif arma == "s" and local == "s":
    print("Há fortes indícios contra o suspeito.")
elif motivo == "s":
    print("O suspeito tem motivo, mas faltam mais provas.")
else:
    print("O suspeito provavelmente é inocente.")

print("\nInvestigação concluída.")
