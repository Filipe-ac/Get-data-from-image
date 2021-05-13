#!/home/filipe/anaconda3/bin/python

#fazer uma selecao para os pontos a serem procurados
#ti para a rgb a ser procurada
#parada correta na hora de plotar
#funcao para desenhar manualmente
#tentar automatizar

import pandas as pd
import numpy as np
import os
import sys

from time import time

def salva_dados(nome,*args):
    ''' Function to save data to a file'''

    os.chdir('/'.join(args[0].split('/')[:-1]))
    aux = nome; n = 1
    while nome in os.listdir():
        nome = aux + '_%s'%n; n+= 1
        
    arq = open(nome,'w')
    s = ''
    tamanho = len(args[0])
    for p in range(tamanho):
        
        for i in args:
            
            s += str(i[p]) + '\t'
        s += '\n'
    arq.write(s)
    arq.close()

def busca(l,valor):
    '''Function to search for the element with the closiest value in a list l''' 

    if len(l) == 0 or len(l) == 1:
        return 0
    
    else:
        return np.argsort(abs(l-valor))[0]




from kivyplt import *
#versao 2 - não acha as bordas do grafico automaticamente

class graf(modelo):
    def __init__(self,arquivo,**args):
        super().__init__()

        
        self.arquivo = arquivo
        self.im = Image.open(arquivo)
        self.matriz = np.array(self.im)
        self.method = 'mean'

        transposta = [[] for i in range(len(self.matriz[0]))]

        for j in range(len(transposta)):
            for linha in self.matriz:
                transposta[j].append(linha[j])
        self.transposta = transposta


        img_obj = self.ax.imshow(self.matriz)
        #img_obj.set_interpolation('bilinear')
        self.ax.axis('off')
        
        self.xlim = self.ax.get_xlim()
        self.ylim = self.ax.get_ylim()
        self.bbusca = Button(text = 'get_data',
                             on_release = self.get_data)

        self.bcancela = Button(text = 'erase',
                               on_release = self.cancela,
                               size_hint_x = None,
                               size = (50,0))
        self.bl_baixo.add_widget(self.bcancela)
            
        self.bl_baixo.add_widget(self.bbusca)

        self.bmove = Button(text = 'change point',on_release = self.move_ponto)
        #self.binsert = Button(text = 'add point',on_release = self.move_ponto)

        self.bl_lateral.lista.append(self.bmove)
        #self.bl_lateral.lista.append(self.binsert)

        #Buttons for set de convertion data
        
        self.b_convertionx = Button(text = 'ruler x',
                                size_hint_y = None,
                                size = (0,30),
                                    on_release = self.b_convertionx_func)
        self.ti_convertionx = TextInput(text = 'None',
                                size_hint_y = None,
                                size = (0,30),
                                multiline = False,
                                on_text_validate = self.set_convertion_x)

        self.b_convertiony = Button(text = 'ruler y',
                                size_hint_y = None,
                                size = (0,30),
                                    on_release = self.b_convertiony_func)
        self.ti_convertiony = TextInput(text = 'None',
                                size_hint_y = None,
                                size = (0,30),
                                multiline = False,
                                on_text_validate = self.set_convertion_y)

        self.bl_lateral.lista += [self.b_convertionx,
                                  self.ti_convertionx,
                                  self.b_convertiony,
                                  self.ti_convertiony]
                                  
                                    
        
        self.bsalvadados = Button(text = 'save',on_release = self.salva_dados)
        self.tinome = TextInput(text = 'arq name',
                                multiline = False,
                                on_text_validate = self.salva_dados)

        self.rgb_label = Button(text = 'RGB coords',
                               background_color = [0,0,0,1])
        self.rgb_ti = TextInput(text = '255,255,255',
                                size_hint_y = None,
                                size = (0,30))

        self.bl_lateral.lista.append(self.rgb_label)
        self.bl_lateral.lista.append(self.rgb_ti)


        self.tolerance = 0.1
        self.tolerance_ti = TextInput(text = '%.4f'%self.tolerance,
                                      multiline = False,
                    on_text_validate = self.ti_tolerance_func,
                                      size_hint_y = None,
                                      size = (0,30))

        self.bl_lateral.lista.append(Button(text = 'Tolerance',
                                            size_hint_y = None,
                                            size = (0,30)))
        self.bl_lateral.lista.append(self.tolerance_ti)
        
        self.bl_baixo.add_widget(self.tinome)
        self.bl_baixo.add_widget(self.bsalvadados)


        lmethod = Label(text = 'method',size_hint_y = None,
                        size = (0,20))
        self.bmethod1 = Button(text = 'mean',
                              on_release = self.func_method,
                              size_hint_y = None,
                              size = (0,30))
        self.bmethod1.background_color = [0,0,1,1]
        self.bmethod2 = Button(text = 'min',
                              on_release = self.func_method,
                              size_hint_y = None,
                              size = (0,30))
        self.bmethod3 = Button(text = 'max',
                              on_release = self.func_method,
                              size_hint_y = None,
                              size = (0,30))

        self.bl_lateral.lista.append(lmethod)
        self.bl_lateral.lista.append(self.bmethod1)
        self.bl_lateral.lista.append(self.bmethod2)
        self.bl_lateral.lista.append(self.bmethod3)
        
        self.start = False
        self.bstart = Button(text = 'start point',
                              on_release = self.bstart_func,
                                size_hint_y = None,
                                size = (0,30))
        self.ti_start = TextInput(text = 'False',
                                size_hint_y = None,
                                size = (0,30),
                                  multiline = False)

        
        
        self.bl_lateral.lista.append(self.bstart)
        self.bl_lateral.lista.append(self.ti_start)

        self.ll_lim_button = Button(text = 'left low lim',
                                    on_release = self.ll_lim_button_func,
                                size_hint_y = None,
                                size = (0,30))
        self.ll_lim_ti = TextInput(text = '0,0',
                                size_hint_y = None,
                                size = (0,30))

        self.ru_lim_ti = TextInput(text = '%i,%i'%(self.matriz.shape[0],
                                                   self.matriz.shape[1]),
                                size_hint_y = None,
                                size = (0,30))
                                   
        self.ru_lim_button = Button(text = 'right upper lim',
                                    on_release = self.ru_lim_button_func,
                                size_hint_y = None,
                                size = (0,30))

        self.button_blacklist = Button(text = 'add blacklist',
                                       on_release = self.blacklist_func,
                                size_hint_y = None,
                                size = (0,30))

        self.bl_lateral.lista.append(self.button_blacklist)
                                       
        
        self.bl_lateral.lista.append(self.ll_lim_button)
        self.bl_lateral.lista.append(self.ll_lim_ti)
        self.bl_lateral.lista.append(self.ru_lim_button)
        self.bl_lateral.lista.append(self.ru_lim_ti)        

        self.botao_injetora = Button(text = 'injective: True',
            on_release = self.botao_injetora_func,
                                     size_hint_y = None,
                                     size = (0,50))
        self.injective = True
                                     
        self.bl_lateral.lista.append(self.botao_injetora)



        
        self.rgb = [255,255,255]

        self.x = []; self.y = []
        self.color_mark = TextInput(text = 'black',multiline = False,
                                    on_text_validate = self.plt,
                                  size_hint_y = None, size = (0,30))
        self.size_mark =TextInput(text = '1.5',multiline = False,
                                    on_text_validate = self.plt,
                                  size_hint_y = None, size = (0,30))

        self.bl_lateral.lista += [Button(text = 'line color',
                                  size_hint_y = None, size = (0,30)),
                                  self.color_mark,
                                  Button(text = 'linewidth',
                                  size_hint_y = None, size = (0,30)),
                                  self.size_mark]

        self.bl_lateral.cria()

        self.ll_lim = [0,self.matriz.shape[0]]
        self.ru_lim = [self.matriz.shape[1],0]

        self.blacklist = [[0],[0]]

        x1,y2 = self.ll_lim
        x2,y1 = self.ru_lim
        self.ax.plot([x1,x2,x2,x1,x1],[y1,y1,y2,y2,y1],
                        '--', color = 'gray')
        


    def func_method(self,*args):
        if args[0].background_color == [0,0,1,1]:
            return
        else:
            for i in [self.bmethod1,self.bmethod2,self.bmethod3]:
                i.background_color = [1,1,1,1]
            args[0].background_color = [0,0,1,1]
            self.method = args[0].text
            
        
    def change_color_button(self,*args):

        if args[0].background_color == [0,0,1,1]:
            args[0].background_color = [1,1,1,1]
        else:
            args[0].background_color = [0,0,1,1]

    def b_convertionx_func(self,*args):
        if self.bsel.color == [0,0,1,1]:
            self.rx1 = self.ptx
            self.rx2 = self.ptx2
            self.rxy1 = self.pty
            self.rxy2 = self.pty2

            if self.ti_convertionx.text == 'None':
                self.ti_convertionx.text = '0,1'
            
            self.plt()
            
    def b_convertiony_func(self,*args):      
        if self.bsel.color == [0,0,1,1]:
            self.ry1 = self.pty
            self.ry2 = self.pty2
            self.ryx1 = self.ptx
            self.ryx2 = self.ptx2
            
            if self.ti_convertiony.text == 'None':
                self.ti_convertiony.text = '0,1'
            
            self.plt()
    def set_convertion_x(self,*args):
        return

    def set_convertion_y(self,*args):
        return
        

    def blacklist_func(self,*args):
        if self.bsel.color == [0,0,1,1]:
            self.bsel.color = [1,1,1,1]

            lx,ly = self.line_selecao.get_data()

            if len(lx) == 0:
                lx = [0]; ly = [0]
            self.blacklist = [lx,ly]
            self.plt()
        
    def ll_lim_button_func(self,*args):
        self.ll_lim = [int(self.ptx),int(self.pty)]
        self.ll_lim_ti.text = '%i,%i'%(int(self.ptx),int(self.pty))
        self.plt()

    def ru_lim_button_func(self,*args):
        self.ru_lim = [int(self.ptx),int(self.pty)]
        self.ru_lim_ti.text = '%i,%i'%(int(self.ptx),int(self.pty))
        self.plt()

    def bstart_func(self,*args):
        try:
            self.start = [int(self.ptx),int(self.pty)]
            self.ti_start.text = '%i,%i'%(int(self.ptx),int(self.pty))
        except Exception as ex:
            print('error bstart_func',ex)
            
    def ti_tolerance_func(self,*args):
        try:
            self.tolerance = float(args[0].text)
        except:
            pass

    def botao_injetora_func(self,*args):
        if args[0].text == 'injective: True':
            self.injective = False
            args[0].text = 'injective: False'
        else:
            args[0].text = 'injective: True'
            self.injective = True
            
            
    def move_ponto_func(self,*args):
        
        try:
            if self.bmove.color == [0,0,1,1]:
                px,py = args[0].pos
                pontox,pontoy = self.mouse2valor(px,py,self.ax.get_xlim(),
                                                 self.ax.get_ylim())

                # allwo one point per pixel in x points
                #to avoid too mutch useless data
                if args[0].button == 'left':
                    pos = busca(self.x,pontox)
                    
                    self.y[pos] = pontoy

                    self.line_pontos.set_data(self.x,self.y)
                    self.fig.canvas.draw()
                    
                    return
                else:
                    self.move(*args)
        except Exception as ex:
            print(ex)

    def insert_point_func(self,*args):
        return
        try:
            

            if self.binsert.color == [0,0,1,1]:
                px,py = args[0].pos
                pontox,pontoy = self.mouse2valor(px,py,self.ax.get_xlim(),
                                                 self.ax.get_ylim())

                if int(pontox) in self.x:
                    return
                if args[0].button == 'left':
                    self.x.append(int(pontox))
                    self.y.append(pontoy)


                          
                    self.plt()
                    return
                else:
                    self.move(*args)
        except Exception as ex:
            print(ex)

    def plt(self,*args):
        
        try:
            self.ax.lines  = []
            #self.cancela()
            if ',' in self.color_mark.text:
                if '(' in self.color_mark.text:
                    color = eval(self.color_mark.text)
                else:
                    color = eval('('+self.color_mark.text+')')
            else:
                color = self.color_mark.text
                
            l = self.ax.plot(self.x,np.array(self.y),
                               '--', color = color,
                             alpha = 1)[0]
            l.set_lw(eval(self.size_mark.text))
            #l.set_lw(1.5)
            #l.set_ms(eval(self.size_mark.text))
            
            
            self.ax.set_title('')

            x1,y2 = self.ll_lim
            x2,y1 = self.ru_lim
            self.ax.plot([x1,x2,x2,x1,x1],[y1,y1,y2,y2,y1],
                            '--', color = 'gray')

            self.ax.plot(self.blacklist[0],self.blacklist[1],
                           '--', color = 'red')

            if self.ti_convertionx.text != 'None':
                self.ax.plot([self.rx1,self.rx2],
                               [self.rxy1,self.rxy2],
                                '--', color = 'orange')

            if self.ti_convertiony.text != 'None':
                self.ax.plot([self.ryx1,self.ryx2],
                               [self.ry1,self.ry2],
                                '--', color = 'orange')

            if self.bsel.color == [0,0,1,1]:
                self.ax.lines.append(self.line_selecao)
                
            self.fig.canvas.draw()
            self.line_pontos = l
        except Exception as ex:
            print(ex,ex.__traceback__.tb_lineno)
        
        
    def on_touch_down(self,*args):
        texto_antigo = self.ti_ponto.text
        self.desce(*args)
        try:
            x,y = self.ptx,self.pty
            try:
                r,g,b,a = self.matriz[int(y)][int(x)]
            except:
                r,g,b = self.matriz[int(y)][int(x)]

            self.rgb = [r,g,b]
        
            self.ti_ponto.text = 'RGB: %s,%s,%s\n x,y: %i,%i'%(r,g,b,int(x),int(y))

            self.ti_ponto_text = '%s,%s,%s,%i,%i'%(r,g,b,int(x),int(y))

            self.rgb_label.background_color = [int(r)/255,int(g)/255,int(b)/255,1]
            #self.rgb_label.background_color = [62/255,168/255,62/255,1]
            self.rgb_ti.text = '%i,%i,%i'%(r,g,b)
            
        except Exception as ex:
            self.ti_ponto.text = texto_antigo
        self.move_ponto_func(*args)
        self.insert_point_func(*args)
        
    def on_touch_move(self,*args):


        if self.bmove.color == [0,0,1,1]:
            self.move_ponto_func(*args)
            return
##        if self.binsert.color == [0,0,1,1]:
##            self.insert_point_func(*args)
##            return
        
        else:
            self.move(*args)



    def salva_dados(self,*args):
        try:
            ly = self.matriz.shape[0] - np.array(self.y)
            lx = np.array(self.x)
            bm = ~np.isnan(ly)
            lx = lx[bm]; ly = ly[bm]
            
            if self.ti_convertiony.text != 'None':
                u1,u2 = eval(self.ti_convertiony.text)
                delta_P = np.sqrt((self.ry1-self.ry2)**2 + (self.ryx1-self.ryx2)**2)
                self.U = u2-u1
                cy = self.U/delta_P
                y0 = u1 - cy*(self.matriz.shape[0]-self.ry1)
                ly = ly*cy + y0
                
            if self.ti_convertionx.text != 'None':
                u1,u2 = eval(self.ti_convertionx.text)
                delta_P = np.sqrt((self.rx1-self.rx2)**2 + (self.rxy1-self.rxy2)**2)
                self.U = u2-u1
                cx = self.U/delta_P
                x0 = u1 - cx*self.rx1
                lx = lx*cx + x0
            
            
            salva_dados(self.tinome.text,lx,ly)

        except Exception as ex:
            print(ex,ex.__traceback__.tb_lineno)
            
    def cancela(self,*args):
        try:
           self.line_pontos.remove()
           self.fig.canvas.draw()
        except:
            pass

    def res_zoom(self,*args):
        self.ax.set_xlim(0,len(self.transposta))
        self.ax.set_ylim(len(self.matriz),0)
        


    def get_data(self,*args):
        try:
            injective = self.injective

            matriz2 = []
            pixel = np.array([self.rgb[0],self.rgb[1],self.rgb[2]])/255
            self.color_mark.text = '(%.2f,%.2f,%.2f)'%(abs(1-pixel[0]),
                                                      pixel[1],
                                                      abs(1-pixel[2]))
            tolerance = self.tolerance

            if self.start == False:
                start_x,start_y = 0,0
            else:
                start_x,start_y = self.start

            for i in self.matriz.transpose(1,0,2):
 
                if i.shape[1] == 4: #some files have the alpha information
                    lv1,lv2,lv3,lv4 = i.transpose()
                else:
                    lv1,lv2,lv3 = i.transpose()
                    
                lv1 = (lv1.astype(int)/255-pixel[0])**2
                lv2 = (lv2.astype(int)/255-pixel[1])**2
                lv3 = (lv3.astype(int)/255-pixel[2])**2
                matriz2.append(np.sqrt(lv1+lv2+lv3))

            matriz2 = np.array(matriz2)

            if self.start != False:
                n = start_x
                x = [start_x]
                y = [start_y]
                start_point = start_x + 1
            else:
                n = self.ll_lim[0]
                x = []
                y = []
                start_point = n

            end_point = self.ru_lim[0]

            
            for i in matriz2[start_point:end_point]:
                
                if i[self.ru_lim[1]:self.ll_lim[1]].min() <= tolerance:
                    
                    tolerance_list = np.where(i[self.ru_lim[1]:self.ll_lim[1]] <= tolerance)[0]
                    tolerance_list += self.ru_lim[1]

                    if n > min(self.blacklist[0]) and n < max(self.blacklist[0]):
                        bm = tolerance_list <= min(self.blacklist[1])
                        bm += tolerance_list >= max(self.blacklist[1])
                        tolerance_list = tolerance_list[bm]  
                    
                    #separate the tolerance_list in adjacent pixels (avoid legends, or
                    #get to y axis position at same x axis value)

                    #obs: seems not efficient. Could be better, but it works.

                    temp_matriz = []
                    index = 0; index_0 = 0
                    while index < len(tolerance_list)-1:
                        if tolerance_list[index] - tolerance_list[index+1] == -1:
                            pass
                        else:
                            temp_matriz.append(tolerance_list.copy()[index_0:index+1])
                            index_0 = index + 1
                        index += 1
                    temp_matriz.append(tolerance_list[index_0:])
                    
                    #if there are two or more possible points for the same x coordinates,
                    #and we are assuming a
                    #injective function, choose the closest point to the previous
                    if injective == True and len(temp_matriz) > 1:
                        temp_list = []
                        for j in temp_matriz:
                            
                            if len(y) == 0:
                                self.ax.set_title('Error - Try reduce the tolerance\n'\
                                                    + 'or set a start point')
                                self.fig.canvas.draw()
                                print('Error - Try reduce the tolerance')
                                return 'Error - Try reduce the tolerance'

                            if self.method == 'mean':
                                temp_list.append((abs(y[-1]-(j.mean())),
                                                  j.mean()))
                            if self.method == 'min':
                                temp_list.append((abs(y[-1]-(j.max())),
                                                  j.max()))
                            if self.method == 'max':
                                temp_list.append((abs(y[-1]-(j.min())),
                                                  j.min()))
                        
                        temp_list.sort()
                        #print(n,temp_matriz)
                        y.append(temp_list[0][1])
                        x.append(n+1)
                    else: #chose all points
                        for j in temp_matriz:
                            
                            if len(j) != 0:
                                x.append(n+1)
                                if self.method == 'mean':
                                    y.append(j.mean())
                                if self.method == 'min':
                                    y.append(j.max())
                                if self.method == 'max':
                                    y.append(j.min())                                    

                n += 1

            
            self.x = x; self.y = y

            self.ax.set_title('')
            
            self.plt()
    
            return True
        except Exception as ex:
            print(ex,ex.__traceback__.tb_lineno)


    def move_ponto(self,*args):
        if args[0].color == [1,1,1,1]:
            args[0].color = [0,0,1,1]
        else:
            args[0].color = [1,1,1,1]
    
        #self.bmove.color = [1,1,1,1]
        self.blupa.color = [1,1,1,1]

    def lupa(self,*args):
        if args[0].color == [1,1,1,1]:
            args[0].color = [0,0,1,1]
        else:
            args[0].color = [1,1,1,1]

        self.bmove.color = [1,1,1,1]


         

    def res_zoom(self,*args):
        self.ax.set_xlim(self.xlim)
        self.ax.set_ylim(self.ylim)
        self.fig.canvas.draw()
        
##try:
##    argv = sys.argv
##    #print(argv)   
##    nome = argv[1].split('/')[-1].strip('\n')
##    os.chdir('/'+argv[1].strip('\n').strip(nome).strip('/'))
##    
##    
##
##except Exception as ex:
##    print(ex)

try:
    graf(sys.argv[1]).run()

    

except Exception as ex:
    print(ex,ex.__traceback__.tb_lineno)
