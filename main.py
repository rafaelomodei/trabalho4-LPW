from dados import *

running : bool = True

def changeState(new_state : bool):
    running = new_state

while running == True:
    print("1 - Adicionar contato \n"
          "2 - Remover contato \n"
          "3 - Atualizar contato \n"
          "4 - Apresentar todos os contatos \n"
          "0 - Finalizar\n")

    operation = int(input('Vamos lá, qual operação deseja realizar ?\n'))

    if(operation == 1):
        insert_inputed_contact()
    elif(operation == 2):
        delete_inputed_contact()
    elif(operation == 3):
        update_inputed_contact()
    elif(operation == 4):
        show_all_contacts()
    else:
        break;



