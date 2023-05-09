import customtkinter
from time import sleep


def clique():
    print('Fazendo login...')
    sleep(1)
    print('Login concluído')


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry('500x300')

texto = customtkinter.CTkLabel(janela, text='Fazer login')
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text='Digite seu email: ')
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text='Digite sua senha: ', show='*')
senha.pack(padx=10, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text='Salvar login')
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text='Login', command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()