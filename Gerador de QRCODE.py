from tkinter import *
from PIL import Image, ImageTk
import qrcode

app = Tk()

class Functions():
	def exit(self):
		self.app.destroy()		
	
	def click_input_link(self, *args):
		self.link.delete(0, END)
		self.link['fg'] = 'white'
		
	def drop_input_link(self, *args):
		self.link.insert(0, 'link')
		self.link.delete(0, 4)
		self.link['fg'] = 'gray'
	
	def click_input_name(self, *args):
		self.name.delete(0, END)
		self.name['fg'] = 'white'
		
	def drop_input_name(self, *args):
		self.name.insert(0, 'Nome do QR')
		self.name.delete(0, 10)
		self.name['fg'] = 'gray'

	def gerar(self):
		self.info_link = self.link.get()
		self.info_name = self.name.get()
		
		if self.info_link == 'Link' and self.info_name == 'Nome do QR':
			self.errors['text'] = 'ERRO: TALVEZ ALGUM CAMPO ESTEJA VAZIO'
			self.errors['fg'] = 'red'
		else:
			qr = qrcode.QRCode(
				version=1,
				error_correction=qrcode.constants.ERROR_CORRECT_H,
				box_size=10,
				border=3
			)
			qr.add_data(self.link)
			qr.make()
			img = qr.make_image(fill_color='black', back_color='white')
			img.save(self.info_name + '.png')
			self.amostra = ImageTk.PhotoImage(Image.open(self.info_name + '.png'))
			self.img_qr['image'] = self.amostra
			
class Aplication(Functions):
	def __init__ (self):
		self.app = app
		self.app.config(background='#111d20')
		#self.app.overrideredirect(True)
		self.app.geometry('800x500')
		self.app.maxsize(width= 800, height= 2000)
		self.app.minsize(width= 800, height= 1200)
		
		# componentes.
		self.tela()
		self.frames()
		self.botoes()
		self.labels()
		self.inputs()
		
		app.mainloop()
		
	def tela(self):
		self.app.title('Gerador de QR CODE')
		self.app.geometry('700x500')
	
	def frames(self):
		
		# - frame da barra do topo.
		self.frame_bar_top = Frame(
					self.app,
					bg = '#111d20'
					)
		self.frame_bar_top.place(
					relx= 0,
					rely= 0,
					relwidth= 1,
					relheight= 0.08
					)	
		
		
		# - frame do conteudo.
		self.frame_content = Frame(
					self.app,
					bg = '#111d20'
					)
		self.frame_content.place(
					relx= 0,
					rely= 0.08,
					relwidth= 1,
					relheight= 0.5
					)
		
		
		#frame do QR.
		self.frame_QR = Frame(
					self.app,
					bg = '#111d20'
					)
		self.frame_QR.place(
					relx= 0,
					rely= 0.5,
					relwidth= 1,
					relheight= 0.5
					)

	def botoes(self):
		
		# botao para fechar o programa.
		self.exit = Button(
					self.frame_bar_top,
					text = 'sair',
					bg = '#111d20',
					fg = 'white',
					font = 'courier 7',
					relief = FLAT,
					highlightthickness = 0,
					command = self.exit
					)
		self.exit.place(
					relx= 0.9,
					rely= 0.22,
					relwidth= 0.09,
					relheight= 0.5
					)
		
		
		# botão e lista do menu.
		self.menu_icon = ImageTk.PhotoImage(Image.open('/storage/emulated/0/PROJECT/icons/fa_bar.png'))
		self.btn_menu = Menubutton(
					self.frame_bar_top,
					text = 'menu',
					image = self.menu_icon,
					bg = '#111d20'
					)
		self.btn_menu.place(
					relx= 0.02,
					rely= 0.13,
					relwidth= 0.10,
					relheight= 0.7,
					)
		self.menu = Menu(
					self.btn_menu,
					tearoff = 0,
					relief = FLAT,
					bd = 0,
					)
		self.btn_menu['menu'] = self.menu
		self.menu.add_command(
					label= 'Ajuda',
					)
		
		# botao de cor 1
		self.btn_color_1 = Button(
					self.frame_content,
					text= 'COR DO FUNDO',
					font= 'serif 4',
					highlightthickness = 0,
					relief= FLAT
					)	
		self.btn_color_1.place(
					relx= 0.05,
					rely= 0.35,
					relwidth= 0.18,
					relheight= 0.08
					)
		
		
		# botao de cor 2
		self.btn_color_2 = Button(
					self.frame_content,
					text= 'COR DO QR',
					font= 'serif 4',
					highlightthickness = 0,
					relief= FLAT
					)
		self.btn_color_2.place(
					relx= 0.77,
					rely= 0.35,
					relwidth= 0.18,
					relheight= 0.08
					)
					
		
		# botao confirm
		self.btn_confirm = Button(
					self.frame_content,
					text= 'GERAR',
					relief= FLAT,
					highlightthickness = 0,
					bg= '#009cb8',
					command= self.gerar
					)
		self.btn_confirm.place(
					relx= 0.36,
					rely= 0.6,
					relwidth= 0.30,
					relheight= 0.12
					)
					
	def labels(self):
			
		# label do titúlo do programa.
		self.title_ = Label(
				self.frame_bar_top,
				text= 'GERADOR DE QR CODE',
				font= 'Serif 9 bold',
				bg= '#111d20',
				fg= '#009cb8'
				)
		self.title_.place(
				relx= 0.22,
				rely= 0.25,
				relwidth= 0.60,
				relheight= 0.4
				)
		
		
		# label da imagem do QR CODE.
		self.img_qr = Label(
				self.frame_QR,
				bg= '#111d20',
				text= 'Seu QR será gerado aqui',
				fg= 'white',
				font= 'serif 7'
				)
		self.img_qr.place(
				relx= 0,
				rely= 0,
				relwidth= 1,
				relheight= 1
				)
		
		# mensagens de errio
		self.errors = Label(
				self.frame_content,
				bg= '#111d20',
				text= '',
				font= 'courier 6'
				)
		self.errors.place(
				relx= 0,
				rely= 0.73,
				relwidth= 1,
				relheight= 0.1
				)
		
	def inputs(self):
		
		# input do link.
		self.link = Entry(
				self.frame_content,
				bg= '#111d20',
				fg= 'gray',
				font= 'courier 6'
				)
		self.link.insert(0, 'Link')
		self.link.place(
				relx= 0.05,
				rely= 0.04,
				relwidth= 0.9,
				relheight= 0.11
				)
		self.link.bind('<Button-1>', self.click_input_link)
		self.link.bind('<Leave>', self.drop_input_link)
		
		
		# input do nome.
		self.name = Entry(
				self.frame_content, 
				bg= '#111d20',
				fg= 'gray',
				font= 'courier 6',
				relief= FLAT
				)
		self.name.insert(0, 'Nome do QR')
		self.name.place(
				relx= 0.05,
				rely= 0.18,
				relwidth= 0.9,
				relheight= 0.11
				)
		self.name.bind('<Button-1>', self.click_input_name)
		self.name.bind('<Leave>', self.drop_input_name)
				
Aplication()