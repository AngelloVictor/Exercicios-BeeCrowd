a,b,c,d = map(float, input().split())

media_geral = (a*2 + b*3 + c*4 + d*1)/10

print("Media: {:.1f}".format(media_geral))

if media_geral >= 7.0:
    print("Aluno aprovado. \n")
    
elif media_geral < 5.0:
    print("Aluno reprovado.\n")
    
elif media_geral >= 5.0 and media_geral <= 6.9:
    print("Aluno em exame.\n")
    nota_exame = float(input())
    
    print("Nota do exame: {:.1f}\n".format(nota_exame))
    nova_media = (media_geral + nota_exame)/2
    
    if nova_media >= 5.0:
        print("Aluno aprovado.\n")
        print("Media final : {:.1f}\n".format(nova_media))
        
    else:
        print("Aluno reprovado.\n")
        print("Media final : {:.1f}\n".format(nova_media))
    
    
    