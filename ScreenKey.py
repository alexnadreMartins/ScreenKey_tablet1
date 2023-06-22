#!/usr/bin/python
 
 
 
 
 
# ========== Configurações ====================
BUTTON_BACKGROUND 		= "black"
MAIN_FRAME_BACKGROUND 	= "black"
BUTTON_LOOK 			= "flat"  # flat, groove, raised, ridge, solid ou sunken
TOP_BAR_TITLE 			= "Atalhos de tela"
TOPBAR_BACKGROUND 		= "white"
TRANSPARENCY 			= 0.7
FONT_COLOR 				= "white"

# ==============================================

# Importar módulos
try:
    import Tkinter
except:
    import tkinter as Tkinter

import pyautogui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QDialog, QHBoxLayout, QLineEdit, QDialogButtonBox, QMessageBox
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
import keyboard

# Configuração das teclas é necessário fazer lista de teclas para que funcione
keys = [

    [
       
        [
            ("Hotkeys"),
            ({'side': 'top', 'expand': 'yes', 'fill': 'both'}),
            [
                             
                ("i","o"),
                ("space",),
                ("j","l"),
                ("b","delete",),
                ("backspace","l"),
                ("shift","ctrl"),
                ("j","l"),
                
                
            
            ]
        ],

    ],

]

# Criar evento da tecla
def create_keyboard_event( capslock, controler, key):
    return


## Classe do Frame
class Keyboard(Tkinter.Frame):
    def __init__(self, *args, **kwargs):
        Tkinter.Frame.__init__(self, *args, **kwargs)

        # Função para criar os botões
        self.create_frames_and_buttons()

    # Função para extrair os dados da tabela do teclado
    # e criar a interface gráfica do teclado
    def create_frames_and_buttons(self):
        # Pegar uma seção de cada vez
        for key_section in keys:
            # Criar um frame separado para cada seção
            store_section = Tkinter.Frame(self)
            store_section.pack(side='left', expand='yes', fill='both', padx=10, pady=10, ipadx=10, ipady=10)

            for layer_name, layer_properties, layer_keys in key_section:
                store_layer = Tkinter.LabelFrame(store_section)  # , text=layer_name)
                # store_layer.pack(side='top',expand='yes',fill='both')
                store_layer.pack(layer_properties)
                for key_bunch in layer_keys:
                    store_key_frame = Tkinter.Frame(store_layer)
                    store_key_frame.pack(side='top', expand='yes', fill='both')
                    for k in key_bunch:
                        k = k.capitalize()
                        if len(k) <= 3:
                            store_button = Tkinter.Button(store_key_frame, text=k, width=2, height=2)
                        else:
                            store_button = Tkinter.Button(store_key_frame, text=k.center(5, ' '), height=2)
                        if " " in k:
                            store_button['state'] = 'disable'

                        store_button['relief'] = BUTTON_LOOK
                        store_button['bg'] = BUTTON_BACKGROUND
                        store_button['fg'] = FONT_COLOR
                        
                        if k == "Configurar Botões":
                            store_button['command'] = self.configure_buttons
                        elif k == "Configurar Hotkeys":
                             store_button['command'] = self.configure_hotkeys

                        store_button['command'] = lambda q=k.lower(): self.button_command(q)
                        store_button.pack(side='left', fill='both', expand='yes')
        return

        # Botão de configurações
        settings_button = Tkinter.Button(self, text='Configurações', command=self.open_settings)
        settings_button.pack(side='top', pady=10)



    # Função para detectar a tecla pressionada
    def button_command(self, event):
       if event.lower() in ["shift", "ctrl"]:
        keyboard.press(event.lower())
       else:
           if keyboard.is_pressed("shift") or keyboard.is_pressed("ctrl"):
                keyboard.release("shift")
                keyboard.release("ctrl")
           pyautogui.press(event)
    def on_virtual_key_press(self, key):
        if hasattr(key, 'char'):
    # Enviar o comando para pressionar a tecla desejada
           pyautogui.press(key.char)

class top_moving_mechanism:
    def __init__(self, root, label):
        self.root = root
        self.label = label

    def motion_activate(self, kwargs):
        w, h = (self.root.winfo_reqwidth(), self.root.winfo_reqheight())
        (x, y) = (kwargs.x_root, kwargs.y_root)
        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        return

    # Abrir janela de configurações
    def open_settings(self):
        settings_window = tk.Toplevel(self)
        settings_window.title("Configurações")
        settings_window.geometry("400x300")

        # Adicionar widgets para edição da lista de teclas keys

        # Botão de confirmação
        confirm_button = tk.Button(settings_window, text="Confirmar", command=settings_window.destroy)
        confirm_button.pack(side='bottom', pady=10)


# Criar janela principal
def main():
    root = Tkinter.Tk(className=TOP_BAR_TITLE)
    k = Keyboard(root, bg=MAIN_FRAME_BACKGROUND)

    # Configuração
    root.overrideredirect(True)
    root.wait_visibility(root)
    root.wm_attributes('-alpha', TRANSPARENCY)
    # Custom
    f = Tkinter.Frame(root)
    t_bar = Tkinter.Label(f, text=TOP_BAR_TITLE, bg=TOPBAR_BACKGROUND)
    t_bar.pack(side='left', expand="yes", fill="both")
    mechanism = top_moving_mechanism(root, t_bar)
    t_bar.bind("<B1-Motion>", mechanism.motion_activate)
    Tkinter.Button(f, text="[X]", command=root.destroy).pack(side='right')
    f.pack(side='top', expand='yes', fill='both')
    k.pack(side='top')
    root.mainloop()
    return


# Função principal
if __name__ == '__main__':
    main()
