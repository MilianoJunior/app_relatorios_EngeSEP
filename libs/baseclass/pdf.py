from fpdf import FPDF
import seaborn as sns
from unidecode import unidecode
from datetime import datetime,date
import webbrowser
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
import asynckivy as ak
import pandas as pd
from pytz import timezone
import locale
locale.setlocale(locale.LC_TIME, locale.normalize('pt_BR.utf8'))
# PACKAGE_PARENT = '..'
# SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
title = 'EngeSEP Engenharia Integrada LTDA'
endereco = 'Rua Nereu Ramos, Nº 3051E-Líder,Chapecó-SC'
CNPJ = 'CNPJ: 22.248.519/0001-26'
telefone = 'plantão: (49)-991075958'
email = 'engesep@engesep.com.br'
fonte = 'helvetica'
resolucao = int(2)
selecao = None
class PDF(FPDF):
    manager_open = False
    conteudo = ''
    path = None
    BASE_DIR = os.environ["ENGESEP_ASSETS"]
    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
    def select_path(self, path):
        self.path = path
        self.exit_manager()
        data_e_hora_atuais = datetime.now()
        data_e_hora = data_e_hora_atuais.strftime('%d-%m-%H-%M')
        name=f'ensegep-{unidecode(data_e_hora)}-.pdf'
        local_pdf = os.path.join(path, name)
        print(local_pdf)
        self.output(local_pdf)
        toast("Salvo com sucesso")
        webbrowser.open_new(local_pdf)
    def file_manager_open(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True,
        )
        home = os.path.expanduser('~')
        location = os.path.join(home, 'Downloads')
        self.file_manager.show(location)  # output manager to the screen
        self.manager_open = True
    def grafico_nivel(self,dados,selecao):
        if selecao[0] == 'mes':
            dados['datas'] = dados['data'].apply(lambda x: str(int(x)))
            sns.set_style("whitegrid")
            f, ax = plt.subplots(figsize=(10, 8))
            sns.set_color_codes("pastel")
            g = sns.relplot(x="datas", y="nivel", kind="line",ci="sd",markers=True, data=dados).set_titles("Nível do reservatório de águas")
            g.set_axis_labels("Dias do mês","Volume de águas em metros")
            save_b = os.path.join(self.BASE_DIR,"agua.png")
            plt.savefig(save_b,bbox_inches='tight')
            plt.close('all')
        else:
            dados['horas'] = dados['hora'].apply(lambda x: str(int(x)))
            sns.set_style("whitegrid")
            f, ax = plt.subplots(figsize=(10, 8))
            sns.set_color_codes("pastel")
            g = sns.relplot(x="horas", y="nivel", kind="line",ci="sd",markers=True, data=dados).set_titles("Nível do reservatório de águas")
            g.set_axis_labels("Horas do dia","Volume de águas em metros")
            save_b = os.path.join(self.BASE_DIR,"agua.png")
            plt.savefig(save_b,bbox_inches='tight')
            plt.close('all')
    def grafico(self,dados,name,turbina,selecao):
        if selecao[0] == 'mes':
            dados['datas'] = dados['data'].apply(lambda x: str(int(x)))
            # dados[name] = dados[name].apply(lambda x: int(x)/1000)
            sns.set_theme(style="whitegrid")
            f, ax = plt.subplots(figsize=(6, 13))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
            sns.set_color_codes("pastel")
            sns.barplot(x=name, y="datas", data=dados,
                        label="Energia em MW/h", color="b")
            ax.bar_label(ax.containers[0], label_type='center')
            ax.legend(ncol='', loc="lower right", frameon=True)
            ax.set(xlim=(0, max(dados[name].values)), ylabel="Dias do mês",
                   xlabel="Produção de Energia em MW/h",title= f'Produção de energia do mês {str(selecao[1])},{turbina}')
            sns.despine(left=True, bottom=True)
            arquivo = name+'.png'
            save_a = os.path.join(self.BASE_DIR,arquivo)
            plt.savefig(save_a,bbox_inches='tight')
            plt.close('all')
        else:
            dados['horas'] = dados['hora'].apply(lambda x: str(int(x)))
            # dados[name] = dados[name].apply(lambda x: int(x)/1000)
            sns.set_theme(style="whitegrid")
            f, ax = plt.subplots(figsize=(6, 13))
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
            sns.set_color_codes("pastel")
            sns.barplot(x=name, y="horas", data=dados,
                        label="Energia em MW/h", color="b")
            ax.bar_label(ax.containers[0], label_type='center')
            ax.legend(ncol='', loc="lower right", frameon=True)
            ax.set(xlim=(0, max(dados[name].values)), ylabel="Horas",
                   xlabel="Produção de Energia em MW/h",title= f'Produção de energia do dia {str(selecao[1])},{turbina}')
            sns.despine(left=True, bottom=True)
            arquivo = name+'.png'
            save_a = os.path.join(self.BASE_DIR,arquivo)
            plt.savefig(save_a,bbox_inches='tight')
            plt.close('all')

    def header(self):
        self.set_margins(20,20,20)
        img_b = os.path.join(self.BASE_DIR, 'logo.png')
        self.image(img_b, 20, 20, 35)
        self.set_font(fonte, 'B', 10)
        self.cell(40)
        self.cell(10,4,title,0, 1, 'L')
        self.cell(40)
        self.cell(10,4,endereco, 0, 1, 'L')
        self.cell(40)
        self.cell(10,4, CNPJ, 0, 1, 'L')
        self.set_font(fonte, 'B', 8)
        self.cell(40)
        self.cell(10, 4,telefone + '  ' + email, 0, 1, 'L')
        self.ln(3)
    def footer(self):
        data_atual = datetime.now()
        data_e_hora = data_atual.strftime('%d/%m/%Y %H:%M')
        self.set_fill_color(243, 245, 247)
        self.set_y(-15)
        self.set_font(fonte, 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'relatório gerado em '+str(data_e_hora)+ ' Página ' + str(self.page_no()), 0, 0, 'C')
    def chapter_title(self,label):
        self.set_font(fonte, 'B', 12)
        self.set_fill_color(18, 27, 44)
        self.set_text_color(255,246,247)
        self.cell(0,8,'%s'%(label), 0, 1, 'L', 1)
        self.ln(1)
    def sub_title(self,label):
        self.set_font(fonte, '', 10)
        self.set_fill_color(18, 27, 44)
        self.set_text_color(255, 246, 247)
        self.cell(0, 5,label, 0, 1, 'L', 1)
        self.ln(1)
    def descricao(self):
        self.set_text_color(18, 27, 44)
    def simple_table(self,spacing=1):
        data_atual = datetime.now()
        data_e_hora = data_atual.strftime('%d/%m/%Y %H:%M').split(' ')
        data = data_e_hora[0]
        hora = data_e_hora[1]
        self.set_text_color(18, 27, 44)
        data = [['Usina ', self.nome_usina],
                ['Cidade ',self.local],
                ['Período ', self.tipo.strip().upper()],
                ['Turbina ', self.turbina]
                ]
        self.set_font(fonte, size=10)
        line_height = self.font_size * 1.5
        col_width = self.epw / 3  # distribute content evenly
        for row in data:
            for datum in row:
                self.multi_cell(col_width, line_height, datum, border=0, ln=3, max_line_height=self.font_size)
            self.ln(line_height)
        self.ln(1)
    def chapter_body(self,info):
        # print(info)
        info = info[0]
        img_a = os.path.join(self.BASE_DIR,info['nome']+'.png')
        self.image(img_a, 100, 88, 87)
        self.set_font(fonte, '', 8)
        self.set_text_color(244, 244, 244)
        self.set_fill_color(10, 10, 10)
        self.cell(80, 5,'Relatório de energia', 0, 0, 'L', True)
        self.ln()
        self.set_fill_color(243, 245, 247)
        self.set_text_color(18, 27, 44)
        self.cell(80, 5, 'Média: '+str(round(info['mean'],resolucao))+' MW/h', 0, 0, 'L', True)
        self.ln()
        self.cell(80, 5, 'Máxima: '+str(round(info['max'],resolucao))+' MW/h', 0, 0, 'L', True)
        self.ln()
        self.cell(80, 5, 'Mínima: '+str(round(info['min'],resolucao))+' MW/h', 0, 0, 'L', True)
        self.ln()
        self.cell(8, 5, 'Variação: '+str(round(info['var'],resolucao))+' MW/h', 0, 0, 'L', True)
        self.ln()
        self.cell(8, 5, 'Desvio padrão: '+str(round(info['std'],resolucao))+' MW/h', 0, 0, 'L', True)
        self.ln()
        self.cell(8, 5, 'Acumulado: '+str(round(info['autal_p'],resolucao))+' MW/h', 0, 0, 'L', True)
        self.ln()
        if self.selecao[0] == 'mes':
            self.cell(8, 5, 'Acumulado do mês: '+str(round(info['mes_p'],resolucao))+' MW/h', 0, 0, 'L', True)
        else:
            self.cell(8, 5, 'Acumulado do dia: '+str(round(info['mes_p'],resolucao))+' MW/h', 0, 0, 'L', True)
        self.ln(5)
        # array_info = [mediaa, max1, min1, variacao1, std1,geracao_total,geracao_mes,nivel_media,nivel_max,nivel_min,nivel_variacao,nivel_std,nivel_atual,corr_nivel_turbina_a]
        self.set_text_color(244, 244, 244)
        self.set_fill_color(10, 10, 10)
        self.cell(80, 5,'Relatório de nível de águas', 0, 0, 'L', True)
        self.ln()
        self.set_fill_color(243, 245, 247)
        self.set_text_color(18, 27, 44)
        self.cell(80, 5, 'Média: '+str(round(info['nivel_mean'],resolucao))+' m', 0, 0, 'L', True)
        self.ln()
        self.cell(80, 5, 'Máxima: '+str(round(info['nivel_max'],resolucao))+' m', 0, 0, 'L', True)
        self.ln()
        self.cell(80, 5, 'Mínima: '+str(round(info['nivel_min'],resolucao))+' m', 0, 0, 'L', True)
        self.ln()
        self.cell(8, 5, 'Variação: '+str(round(info['nivel_var'],resolucao))+' m', 0, 0, 'L', True)
        self.ln()
        self.cell(8, 5, 'Desvio padrão: '+str(round(info['nivel_std'],resolucao))+' m', 0, 0, 'L', True)
        self.ln()
        self.cell(8, 5, 'Medição atual: '+str(round(info['nivel_atual'],resolucao))+' m', 0, 0, 'L', True)
        self.set_fill_color(10, 10, 10)
        self.set_text_color(244, 244, 244)
        self.ln(5)
        self.cell(80, 5, 'Correlação entre o nível de águas e energia', 0, 0, 'L', True)
        self.ln()
        self.set_fill_color(243, 245, 247)
        self.set_text_color(18, 27, 44)
        self.cell(80, 5, 'Correlação '+str(round(info['corr'],resolucao)), 0, 0, 'L', True)
        self.ln(10)
        ly = self.get_y()
        titulo = "agua.png"
        img_c = os.path.join(self.BASE_DIR, titulo)
        self.image(img_c,20,round(ly), 80)

    def print_chapter(self, title,info):
        self.add_page()
        self.chapter_title(title)
        self.sub_title('Informações Gerais')
        self.simple_table()
        self.sub_title('Informações quantitativas')
        self.chapter_body(info)
    def gerar(self,data,descricao):
        # print(data)
        # print(descricao)
        ifb = data.describe()
        ifc = data.corr()
        # print(ifb.head())
        # print(ifc.head())
        self.nome_usina = descricao['nome_usina'][0]
        self.local = descricao['local'][0]
        self.selecao = descricao['selecao'][0]
        # self.mes = descricao['selecao'][0][0]
        self.grafico_nivel(data,self.selecao)
        if descricao['producao_atual_a'][0] != 'Null':
            name = 'energia_a'
            self.turbina = descricao['turbina_a'][0]
            infoa = [{'mean':ifb[name]['mean'],
                      'max':ifb[name]['max'],
                      'min':ifb[name]['min'],
                      'var':(ifb[name]['max']-ifb[name]['min']),
                      'std':ifb[name]['std'],
                      'autal_p':descricao['producao_atual_a'][0],
                      'mes_p':sum(data[name]),
                      'nivel_mean':ifb['nivel']['mean'],
                      'nivel_max':ifb['nivel']['max'],
                      'nivel_min':ifb['nivel']['min'],
                      'nivel_var':(ifb['nivel']['max']-ifb['nivel']['min']),
                      'nivel_std':ifb['nivel']['std'],
                      'nivel_atual':descricao['nivel'][0],
                      'corr':ifc[name]['nivel'],
                      'nome':name}]

            self.grafico(data,name,self.turbina,self.selecao)
            if self.selecao[0] == 'mes':
                self.tipo = 'Mês ' + str(self.selecao[1])
            else:
                self.tipo = 'Dia ' + str(self.selecao[1])
            self.print_chapter('Relatório EngeSEP - '+self.turbina+'  '+self.tipo, infoa)

        if descricao['producao_atual_b'][0] != 'Null':
            name = 'energia_b'
            self.turbina = descricao['turbina_b'][0]
            infob = [{'mean':ifb[name]['mean'],
                      'max':ifb[name]['max'],
                      'min':ifb[name]['min'],
                      'var':(ifb[name]['max']-ifb[name]['min']),
                      'std':ifb[name]['std'],
                      'autal_p':descricao['producao_atual_b'][0],
                      'mes_p':sum(data[name]),
                      'nivel_mean':ifb['nivel']['mean'],
                      'nivel_max':ifb['nivel']['max'],
                      'nivel_min':ifb['nivel']['min'],
                      'nivel_var':(ifb['nivel']['max']-ifb['nivel']['min']),
                      'nivel_std':ifb['nivel']['std'],
                      'nivel_atual':descricao['nivel'][0],
                      'corr':ifc[name]['nivel'],
                      'nome':name}]
            self.grafico(data,name,self.turbina,self.selecao)
            if self.selecao[0] == 'mes':
                self.tipo = 'Mês ' + str(self.selecao[1])
            else:
                self.tipo = 'Dia ' + str(self.selecao[1])
            self.print_chapter('Relatório EngeSEP - '+self.turbina+'  '+self.tipo, infob)
        #     self.grafico(data,name,self.turbina)
        #     self.print_chapter('Relatório EngeSEP -'+self.turbina+' Mês: '+self.mes, infob)
        self.file_manager_open()




