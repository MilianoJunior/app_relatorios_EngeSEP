from datetime import datetime
# import datetime as dt
from pytz import timezone
# import locale
import pandas as pd

class Periodo:
    def __init__(self):
        self.unidade = 1000.0 # dividido por 1000 está em megawats
        self.nivel_unidade = 100.0 # está em metros
        self.resolucao = 2
    def soma_hora(self,selecao):
        dia = 0
        energia_a = 0
        energia_b = 0
        selecionado = pd.DataFrame(columns=['ano','mes','hora','data','energia_a','energia_b','nivel'])
        if len(selecao) < 1:
            return selecionado
        limite = len(selecao)
        dia = selecao['dias'].values[0]
        hora = int(selecao.criado_em.values[0][11:13])
        seta = selecao['energia_a'].values[0]
        setb = selecao['energia_b'].values[0]
        acumulado = 0
        for row in range(0,limite):
            if int(selecao.criado_em.values[row][11:13]) !=  hora or row == (limite-1):
                energia_a =  selecao['energia_a'].values[row] - seta
                energia_b =  selecao['energia_b'].values[row] - setb
                acumulado += energia_a
                selecionado = selecionado.append({'ano': int(selecao['ano'].values[row]),
                                                'mes': int(selecao['mes'].values[row]),
                                                'hora': int(hora),
                                                'data': int(dia),
                                                'energia_a':round(float(energia_a)/self.unidade,self.resolucao),
                                                'energia_b':round(float(energia_b)/self.unidade,self.resolucao),
                                                'nivel':round(float(selecao['nivel'].values[row])/self.nivel_unidade,self.resolucao)},ignore_index=True)
                hora = int(selecao.criado_em.values[row][11:13])
                seta = selecao['energia_a'].values[row]
                setb = selecao['energia_b'].values[row]
        selecionado = selecionado.astype({'ano':int,'mes':int,'hora':int,'data':int,'energia_a':float,'energia_b':float,'nivel':float})
        return selecionado

    def dia_metodo(self, dados, mes):
        mes = mes.strftime('%Y-%m-%d').split('-')
        tipos_types = {'id':int,'energia_a':float ,'energia_b':float,'id_a':str,'id_b':str,'nivel':float,
                       'cidade':str, 'usina':str,'ip_a':str,'ip_b':str,'registro_a':str,'registro_b':str,'registro_nivel':str, 'criado_em':str, 'ts':float}
        for s in tipos_types.keys():
            for t in dados.index:
                if not isinstance(dados[s][t],tipos_types[s]):
                    if tipos_types[s] == float:
                        try:
                            dados.loc[t,s] = float(dados[s][t])
                        except:
                            dados.loc[t,s] = 0.0
                    if tipos_types[s] == str:
                        try:
                            dados.loc[t,s] = str(dados[s][t])
                        except:
                            dados.loc[t,s] = ' '
                    if tipos_types[s] == int:
                        try:
                            dados.loc[t,s] = int(dados[s][t])
                        except:
                            dados.loc[t,s] = 0
        dados = dados.astype({'id':int,'energia_a':float ,'energia_b':float,'id_a':str,'id_b':str,'nivel':float, 'cidade':str, 'usina':str,
                                            'ip_a':str,'ip_b':str,'registro_a':str,'registro_b':str,'registro_nivel':str, 'criado_em':str, 'ts':float})
        dados['data'] = dados['criado_em'].apply(lambda x: str(x)[0:10])
        dados['dias'] = pd.DatetimeIndex(dados['data']).day
        dados['mes'] = pd.DatetimeIndex(dados['data']).month
        dados['ano'] = pd.DatetimeIndex(dados['data']).year
        par = mes[2]
        selecao = dados[dados['dias'] == int(par)]
        selecao = selecao[selecao['ano'] == dados['ano'].values[-1]]
        descricao = pd.DataFrame(columns=['turbina_a','turbina_b','producao_atual_a','producao_atual_b','nome_usina','local','selecao','nivel'])
        descricao = descricao.append({'turbina_a':str(dados['id_a'].values[-1]),
                                      'turbina_b':str(dados['id_b'].values[-1]),
                                      'producao_atual_a':round(float(dados['energia_a'].values[-1])/self.unidade,self.resolucao),
                                      'producao_atual_b':round(float(dados['energia_b'].values[-1])/self.unidade,self.resolucao),
                                      'nome_usina':str(dados['usina'].values[-1]),
                                      'local':str(dados['cidade'].values[-1]),
                                      'selecao':['dia',mes[2]],
                                      'nivel':round(float(dados['nivel'].values[-1])/self.nivel_unidade,self.resolucao)},ignore_index=True)
        return self.soma_hora(selecao), descricao

    def soma(self, selecao):
        dia = 0
        energia_a = 0
        energia_b = 0
        selecionado = pd.DataFrame(columns=['ano','mes','data','energia_a','energia_b','nivel'])
        if len(selecao) < 1:
            return selecionado
        limite = len(selecao)-1
        dia = selecao['dias'].values[0]
        seta = selecao['energia_a'].values[0]
        setb = selecao['energia_b'].values[0]
        for row in range(0,limite):
            if selecao['dias'].values[row] !=  dia or row == (limite-1):
                energia_a =  selecao['energia_a'].values[row] - seta
                energia_b =  selecao['energia_b'].values[row] - setb
                selecionado = selecionado.append({'ano': int(selecao['ano'].values[row]),
                                                'mes': int(selecao['mes'].values[row]),
                                                'data': int(dia),
                                                'energia_a':round(float(energia_a)/self.unidade,self.resolucao),
                                                'energia_b':round(float(energia_b)/self.unidade,self.resolucao),
                                                'nivel':round(float(selecao['nivel'].values[row])/self.nivel_unidade,self.resolucao)},ignore_index=True)
                dia = selecao['dias'].values[row]
                seta = selecao['energia_a'].values[row]
                setb = selecao['energia_b'].values[row]
        return selecionado

    def mes_metodo(self, dados, mes):
        tipos_types = {'id':int,'energia_a':float ,'energia_b':float,'id_a':str,'id_b':str,'nivel':float,
                       'cidade':str, 'usina':str,'ip_a':str,'ip_b':str,'registro_a':str,'registro_b':str,'registro_nivel':str, 'criado_em':str, 'ts':float}
        for s in tipos_types.keys():
            for t in dados.index:
                if not isinstance(dados[s][t],tipos_types[s]):
                    if tipos_types[s] == float:
                        try:
                            dados.loc[t,s] = float(dados[s][t])
                        except:
                            dados.loc[t,s] = 0.0
                    if tipos_types[s] == str:
                        try:
                            dados.loc[t,s] = str(dados[s][t])
                        except:
                            dados.loc[t,s] = ' '
                    if tipos_types[s] == int:
                        try:
                            dados.loc[t,s] = int(dados[s][t])
                        except:
                            dados.loc[t,s] = 0
        dados = dados.astype({'id':int,'energia_a':float ,'energia_b':float,'id_a':str,'id_b':str,'nivel':float, 'cidade':str, 'usina':str,
                                            'ip_a':str,'ip_b':str,'registro_a':str,'registro_b':str,'registro_nivel':str, 'criado_em':str, 'ts':float})
        dados['data'] = dados['criado_em'].apply(lambda x: str(x)[0:10])
        dados['dias'] = pd.DatetimeIndex(dados['data']).day
        dados['mes'] = pd.DatetimeIndex(dados['data']).month
        dados['ano'] = pd.DatetimeIndex(dados['data']).year
        par = mes[1]
        selecao = dados[dados['mes']== int(par)]
        selecao = selecao[selecao['ano']== dados['ano'].values[-1]]
        descricao = pd.DataFrame(columns=['turbina_a','turbina_b','producao_atual_a','producao_atual_b','nome_usina','local','selecao','nivel'])
        descricao = descricao.append({'turbina_a':str(dados['id_a'].values[-1]),
                                      'turbina_b':str(dados['id_b'].values[-1]),
                                      'producao_atual_a':round(float(dados['energia_a'].values[-1])/self.unidade,self.resolucao),
                                      'producao_atual_b':round(float(dados['energia_b'].values[-1])/self.unidade,self.resolucao),
                                      'nome_usina':str(dados['usina'].values[-1]),
                                      'local':str(dados['cidade'].values[-1]),
                                      'selecao':['mes', dados['mes'][0]],
                                      'nivel':round(float(dados['nivel'].values[-1])/self.nivel_unidade,self.resolucao)},ignore_index=True)
        return self.soma(selecao),descricao

