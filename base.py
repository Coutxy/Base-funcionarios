import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import numpy as np
df = pd.read_excel(r'Base Projetos (1).xlsx')
st.set_page_config(page_title='Base projeto', layout='wide')
st.title('Base Projetos!')
st.sidebar.write('Analisando o Arquivo Base Projetos (1).xlsx')
stt = df.groupby('Setor')['Status'].value_counts()
responsavel = df.groupby('Setor')['Responsável'].value_counts().sort_values(ascending=False)
responsavel_cont = df.groupby('Responsável')['Valor Negociado'].sum()
df['Finalizados'] = np.where(df['Status'] == 'Finalizado', 'Sim', 'Não')
fina = df.groupby('Setor')['Finalizados'].value_counts()
aba1, aba2, aba3, aba4, aba5, aba6, aba7, aba8, aba9  = st.tabs(['Projetos','TI','Marketing','Comercial','Financeiro','Logística', 'Compras', 'Produção', 'RH'])
with aba1:
    setores = df['Setor'].value_counts().sort_index()
    seto = [{"value": int(v), "name": k} for k, v in setores.items()]
    options_pizza = {
    "color": ["#56B92F", "#31691A", "#FF9F1C", "#2EC4B6","#C42EBD", "#C42E2E", "#81B8E6", "#6F2EC4"],  # Cores personalizadas
    "title": {"text": "Status dos Projetos", "left": "center"},
    "tooltip": {"trigger": "item"},
    "legend": {"orient": "vertical", "left": "left"},
    "series": [{
        "type": "pie",
        "radius": "50%",
        "data": seto,
        "label": {"formatter": "{b}: {d}%"},
        "emphasis": {
            "itemStyle": {
                "shadowBlur": 10,
                "shadowOffsetX": 0,
                "shadowColor": "rgba(0, 0, 0, 0.5)"
                }
            }
        }]
    }
    st_echarts(options=options_pizza, key="grafico_pizza_geral")
    val_neg = df.groupby('Setor')['Valor Negociado'].sum()
    x = val_neg.index.tolist()
    y = val_neg.values.tolist()
    st.header('Valor Negociado por setor:')
    options = options = {
    "xAxis": {
        "type": "category",
        "data": x,
    },
    "yAxis": {"type": "value"},
    "series": [
        {"data": y,
         "type": "bar",
        "label": {
                "show": True,
                "position": "top"
                }
            }
        ],  
    }
    st_echarts(options=options, key="grafico_valor_negociado_setor")
    st.markdown(f"<h3 style='font-size: 30px;'>A media de Valores Negociados Totais foi de: {np.mean(y):,.0f}</h3>", unsafe_allow_html=True)
    status = df['Status'].value_counts().sort_index()
    stti = status.index.tolist()
    sttv = status.values.tolist()
    st.header('Status:')
    options1 = {
    "xAxis": {
        "type": "category",
        "data": stti,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": sttv,
            "type": "bar",
            "itemStyle": {
                "color": "#DDD55D"
            },
            "label": {
                "show": True,
                "position": "top"
                }
            }
        ]
    }
    st_echarts(options=options1, key="grafico_status_geral")
    st.divider()
    st.title('FInaceiro')
    orcamento = int(df['Valor Orçado'].sum())
    valor_neg = int(df['Valor Negociado'].sum())
    options2 = {
    "xAxis": {
        "type": "category",
        "data": ['Valor Orçado', 'Valor Negociado'],
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": [
                {"value" : orcamento, "itemStyle": {"color": "#56B92F"}},
                {"value": valor_neg, "itemStyle": {"color": "#2E9C02"}}
                ],
            "type": "bar",
            "label": {
                "show": True,
                "position": "top"
                }
            }
        ]
    }
    st_echarts(options=options2, key="grafico_orcado_vs_negociado")

    st.header('Descontos Concedidos:')
    desconto = df.groupby('Setor')['Desconto Concedido'].sum()
    desconto_res = df.groupby('Responsável')['Desconto Concedido'].sum().sort_values()
    p = desconto.values.tolist()
    options3 = {
    "xAxis": {
        "type": "category",
        "data": x,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": p,
            "type": "bar",
            "itemStyle": {
                "color": "#EE623F"
            },
            "label": {
                "show": True,
                "position": "top"
                }
            }
        ]
    }
    st_echarts(options=options3, key="grafico_descontos_concedidos")
    st.markdown(f"<h3 style='font-size: 30px;'>O responsavel que mais aplicou descontos foi o: {desconto_res.index[-1]}, e o setor que mais aplicou foi o: {desconto.index.sort_values().max()} </h3>", unsafe_allow_html=True)

with aba2:
    st.markdown(f"<h3 style='font-size: 30px;'>O setor TI é presente em 20,17% dos projetos com {setores['TI']}! desses projetos, {fina['TI']['Sim']} deles foram Finalizados!</h3>", unsafe_allow_html=True)
    st.header('Status:')
    TI = stt['TI'].values.tolist()
    options4 = {
    "xAxis": {
        "type": "category",
        "data": stti,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": TI,
            "type": "bar",
            "itemStyle": {
                "color": "#DDD55D"
            },
            "label": {
                "show": True,
                "position": "top"
                }
            }
        ]
    }
    st_echarts(options=options4, key="grafico_TI_status")

    st.header('Responsaveis:')
    col1, col2 = st.columns([2,1])
    with col1:
        responsal_ti = responsavel['TI']
        pizza_datati = [{"value": int(v), "name": k} for k, v in responsal_ti.items()]
        optionsti = {
        "title": {
            "text": "Distribuição dos Status dos Projetos",
            "left": "center"
        },
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "orient": "vertical",
            "left": "left"
        },
        "series": [
            {
                "name": "Status",
                "type": "pie",
                "radius": "50%",
                "data": pizza_datati,
                "label": {
                    "formatter": "{b}: {d}%"
                },
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)"
                    }
                }
            }
        ]
    }
        st_echarts(options=optionsti, key="grafico_TI_responsaveis")
    with col2:
        st.write('')
        st.write('')
        st.markdown(f"<h3 style='font-size: 30px;'>O responsavel mais presente foi o(a) {responsal_ti.index[0]}, contribuiu a empresa com: R${responsavel_cont[responsal_ti.index[0]]:,.0f} em projetos negociados</h3>", unsafe_allow_html=True)

with aba3:
    st.markdown(f"<h3 style='font-size: 30px;'>O setor Marketing é presente em 19,18% dos projetos com {setores['Marketing']}! desses projetos, {fina['Marketing']['Sim']} deles foram Finalizados!</h3>", unsafe_allow_html=True)
    st.header('Status:')
    Marketing = stt['Marketing'].values.tolist()
    optionsm1 = {
    "xAxis": {
        "type": "category",
        "data": stti,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": Marketing,
            "type": "bar",
            "itemStyle": {
                "color": "#DDD55D"
            },
            "label": {
                "show": True,
                "position": "top"
                }
            }
        ]
    }
    
    st_echarts(options=optionsm1, key="grafico_Marketing_status")
    st.header('Responsaveis:')
    col3, col4 = st.columns([2,1])
    with col3:
        responsal_M = responsavel['Marketing']
        pizza_dataM = [{"value": int(v), "name": k} for k, v in responsal_M.items()]
        optionsM = {
        "title": {
            "text": "Distribuição dos Status dos Projetos",
            "left": "center"
        },
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "orient": "vertical",
            "left": "left"
        },
        "series": [
            {
                "name": "Status",
                "type": "pie",
                "radius": "50%",
                "data": pizza_dataM,
                "label": {
                    "formatter": "{b}: {d}%"
                },
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)"
                    }
                }
            }
        ]
    }
        st_echarts(options=optionsM, key="grafico_Markenting_responsaveis")
    with col4:
        st.write('')
        st.write('')
        st.markdown(f"<h3 style='font-size: 30px;'>O responsavel mais presente foi o(a) {responsal_M.index[0]}, contribuiu a empresa com: R${responsavel_cont[responsal_M.index[0]]:,.0f} em projetos negociados</h3>", unsafe_allow_html=True)

with aba4:
    st.markdown(f"<h3 style='font-size: 30px;'>O setor Comercial é presente em 17,16% dos projetos com {setores['Comercial']}! desses projetos, {fina['Comercial']['Sim']} deles foram Finalizados!</h3>", unsafe_allow_html=True)
    st.header('Status:')
    comercial = stt['Comercial'].values.tolist()
    optionsC1 = {
    "xAxis": {
        "type": "category",
        "data": stti,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": comercial,
            "type": "bar",
            "itemStyle": {
                "color": "#DDD55D"
            },
            "label": {
                "show": True,
                "position": "top"
                }
            }
        ]
    }
    st_echarts(options=optionsC1, key="grafico_Comercial_status")

    st.header('Responsaveis:')
    col5, col6 = st.columns([2,1])
    with col5:
        responsal_C = responsavel['Comercial']
        pizza_data4 = [{"value": int(v), "name": k} for k, v in responsal_C.items()]
        optionsC = {
        "title": {
            "text": "Distribuição dos Status dos Projetos",
            "left": "center"
        },
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "orient": "vertical",
            "left": "left"
        },
        "series": [
            {
                "name": "Status",
                "type": "pie",
                "radius": "50%",
                "data": pizza_data4,
                "label": {
                    "formatter": "{b}: {d}%"
                },
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)"
                    }
                }
            }
        ]
    }
        st_echarts(options=optionsC, key="grafico_Comercial_responsaveis")
    with col6:
        st.write('')
        st.write('')
        st.markdown(f"<h3 style='font-size: 30px;'>O responsavel mais presente foi o(a) {responsal_C.index[0]}, contribuiu a empresa com: R${responsavel_cont[responsal_C.index[0]]:,.0f} em projetos negociados</h3>", unsafe_allow_html=True)

with aba5:
    st.markdown(f"<h3 style='font-size: 30px;'>O setor Financeiro é presente em 15,42% dos projetos com {setores['Financeiro']}! desses projetos, {fina['Financeiro']['Sim']} deles foram Finalizados!</h3>", unsafe_allow_html=True)
    st.header('Status:')
    Finceiro = stt['Financeiro'].values.tolist()
    optionsF1 = {
    "xAxis": {
        "type": "category",
        "data": stti,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": Finceiro,
            "type": "bar",
            "itemStyle": {
                "color": "#DDD55D"
            },
            "label": {
                "show": True,
                "position": "top"
                }
            }
        ]
    }
    st_echarts(options=optionsF1, key="grafico_Financeiro_status")

    st.header('Responsaveis:')
    col7, col8 = st.columns([2,1])
    with col7:
        responsal_F = responsavel['Financeiro']
        pizza_dataF = [{"value": int(v), "name": k} for k, v in responsal_F.items()]
        optionsF = {
        "title": {
            "text": "Distribuição dos Status dos Projetos",
            "left": "center"
        },
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "orient": "vertical",
            "left": "left"
        },
        "series": [
            {
                "name": "Status",
                "type": "pie",
                "radius": "50%",
                "data": pizza_dataF,
                "label": {
                    "formatter": "{b}: {d}%"
                },
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)"
                    }
                }
            }
        ]
    }
        st_echarts(options=optionsF, key="grafico_Finceiro_responsaveis")
    with col8:
        st.write('')
        st.write('')
        st.markdown(f"<h3 style='font-size: 30px;'>O responsavel mais presente foi o(a) {responsal_F.index[0]}, contribuiu a empresa com: R${responsavel_cont[responsal_F.index[0]]:,.0f} em projetos negociados</h3>", unsafe_allow_html=True)

with aba6:
    st.markdown(f"<h3 style='font-size: 30px;'>O setor Logística é presente em 12,08% dos projetos com {setores['Logística']}! desses projetos, {fina['Logística']['Sim']} deles foram Finalizados!</h3>", unsafe_allow_html=True)
    st.header('Status:')
    Logistica = stt['Logística'].values.tolist()
    optionsL1 = {
    "xAxis": {
        "type": "category",
        "data": stti,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": Logistica,
            "type": "bar",
            "itemStyle": {
                "color": "#DDD55D"
            },
            "label": {
                "show": True,
                "position": "top"
                }
            }
        ]
    }
    st_echarts(options=optionsL1, key="grafico_Logística_status")

    st.header('Responsaveis:')
    col9, col10 = st.columns([2,1])
    with col9:
        responsal_L = responsavel['Logística']
        pizza_dataL = [{"value": int(v), "name": k} for k, v in responsal_L.items()]
        optionsL = {
        "title": {
            "text": "Distribuição dos Status dos Projetos",
            "left": "center"
        },
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "orient": "vertical",
            "left": "left"
        },
        "series": [
            {
                "name": "Status",
                "type": "pie",
                "radius": "50%",
                "data": pizza_dataL,
                "label": {
                    "formatter": "{b}: {d}%"
                },
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)"
                    }
                }
            }
        ]
    }
        st_echarts(options=optionsL, key="grafico_Logística_responsaveis")
    with col10:
        st.write('')
        st.write('')
        st.markdown(f"<h3 style='font-size: 30px;'>O responsavel mais presente foi o(a) {responsal_L.index[0]}, contribuiu a empresa com: R${responsavel_cont[responsal_L.index[0]]:,.0f} em projetos negociados</h3>", unsafe_allow_html=True)
with aba7:
    st.markdown(f"<h3 style='font-size: 30px;'>O setor Compras é presente em 7,75% dos projetos com {setores['Compras']}! desses projetos, {fina['Compras']['Sim']} deles foram Finalizados!</h3>", unsafe_allow_html=True)
    st.header('Status:')
    Compras = stt['Compras'].values.tolist()
    optionsCo1 = {
    "xAxis": {
        "type": "category",
        "data": stti,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": Compras,
            "type": "bar",
            "itemStyle": {
                "color": "#DDD55D"
            },
            "label": {
                "show": True,
                "position": "top"
                }
            }
        ]
    }
    st_echarts(options=optionsCo1, key="grafico_Compras_status")

    st.header('Responsaveis:')
    col11, col12 = st.columns([2,1])
    with col11:
        responsal_Co = responsavel['Compras']
        pizza_dataCo = [{"value": int(v), "name": k} for k, v in responsal_Co.items()]
        optionsCo = {
        "title": {
            "text": "Distribuição dos Status dos Projetos",
            "left": "center"
        },
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "orient": "vertical",
            "left": "left"
        },
        "series": [
            {
                "name": "Status",
                "type": "pie",
                "radius": "50%",
                "data": pizza_dataCo,
                "label": {
                    "formatter": "{b}: {d}%"
                },
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)"
                    }
                }
            }
        ]
    }
        st_echarts(options=optionsCo, key="grafico_Compras_responsaveis")
    with col12:
        st.write('')
        st.write('')
        st.markdown(f"<h3 style='font-size: 30px;'>O responsavel mais presente foi o(a) {responsal_Co.index[0]}, contribuiu a empresa com: R${responsavel_cont[responsal_Co.index[0]]:,.0f} em projetos negociados</h3>", unsafe_allow_html=True)


with aba8:
    st.markdown(f"<h3 style='font-size: 30px;'>O setor Produção é presente em 5,32% dos projetos com {setores['Produção']}! desses projetos, {fina['Produção']['Sim']} deles foram Finalizados!</h3>", unsafe_allow_html=True)
    st.header('Status:')
    Produção = stt['Produção'].values.tolist()
    optionsP1 = {
    "xAxis": {
        "type": "category",
        "data": stti,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": Produção,
            "type": "bar",
            "itemStyle": {
                "color": "#DDD55D"
            },
            "label": {
                "show": True,
                "position": "top"
                }
            }
        ]
    }
    st_echarts(options=optionsP1, key="grafico_Produção_status")

    st.header('Responsaveis:')
    col13, col14 = st.columns([2,1])
    with col13:
        responsal_P = responsavel['Produção']
        pizza_dataP = [{"value": int(v), "name": k} for k, v in responsal_P.items()]
        optionsP = {
        "title": {
            "text": "Distribuição dos Status dos Projetos",
            "left": "center"
        },
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "orient": "vertical",
            "left": "left"
        },
        "series": [
            {
                "name": "Status",
                "type": "pie",
                "radius": "50%",
                "data": pizza_dataP,
                "label": {
                    "formatter": "{b}: {d}%"
                },
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)"
                    }
                }
            }
        ]
    }
        st_echarts(options=optionsP, key="grafico_Produção_responsaveis")
    with col14:
        st.write('')
        st.write('')
        st.markdown(f"<h3 style='font-size: 30px;'>O responsavel mais presente foi o(a) {responsal_P.index[0]}, contribuiu a empresa com: R${responsavel_cont[responsal_P.index[0]]:,.0f} em projetos negociados</h3>", unsafe_allow_html=True)


with aba9:
    st.markdown(f"<h3 style='font-size: 30px;'>O setor RH é presente em 2,92% dos projetos com {setores['RH']}! desses projetos, {fina['RH']['Sim']} deles foram Finalizados!</h3>", unsafe_allow_html=True)
    st.header('Status:')
    RH = stt['RH'].values.tolist()
    optionsR1 = {
    "xAxis": {
        "type": "category",
        "data": stti,
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": RH,
            "type": "bar",
            "itemStyle": {
                "color": "#DDD55D"
            },
            "label": {
                "show": True,
                "position": "top"
                }
            }
        ]
    }
    st_echarts(options=optionsR1, key="grafico_RH_status")

    st.header('Responsaveis:')
    col15, col16 = st.columns([2,1])
    with col15:
        responsal_R = responsavel['RH']
        pizza_dataR = [{"value": int(v), "name": k} for k, v in responsal_R.items()]
        optionsR = {
        "title": {
            "text": "Distribuição dos Status dos Projetos",
            "left": "center"
        },
        "tooltip": {
            "trigger": "item"
        },
        "legend": {
            "orient": "vertical",
            "left": "left"
        },
        "series": [
            {
                "name": "Status",
                "type": "pie",
                "radius": "50%",
                "data": pizza_dataR,
                "label": {
                    "formatter": "{b}: {d}%"
                },
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)"
                    }
                }
            }
        ]
    }
        st_echarts(options=optionsR, key="grafico_RH_responsaveis")
    with col16:
        st.write('')
        st.write('')
        st.markdown(f"<h3 style='font-size: 30px;'>O responsavel mais presente foi o(a) {responsal_R.index[0]}, contribuiu a empresa com: R${responsavel_cont[responsal_R.index[0]]:,.0f} em projetos negociados</h3>", unsafe_allow_html=True)
