import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd

from globals import *

# ========= Layout ========= #
layout = dbc.Card([
                html.H1("MyBudget", className="text-primary"),
                html.P("By Vicentin", className="text-info"),
                html.Hr(),
                        

        # === Seção PERFIL === #
                dbc.Button(id='botao_avatar',
                    children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')], style={'background-color': 'transparent', 'border-color': 'transparent'}),
                                                                                                        

        # === Seção NOVO === #
                dbc.Row([
                    dbc.Col([
                        dbc.Button(color="success", id="open-novo-receita", 
                                children=["+ Receita"]),
                    ], width=6),

                    dbc.Col([
                        dbc.Button(color="danger", id="open-novo-despesa",
                                children=["+ Despesa"]),
                    ], width=6)
                ]),


                # Modal Receita
                html.Div([
                    dbc.Modal([
                        dbc.ModalHeader(dbc.ModalTitle("Adicionar receita")),
                        dbc.ModalBody([
                            dbc.Row([
                                dbc.Col([
                                        dbc.Label("Descrição: "),
                                        dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-receita"),
                                ], width=6), 
                                dbc.Col([
                                        dbc.Label("Valor: "),
                                        dbc.Input(placeholder="$100.00", id="valor_receita", value="")
                                ], width=6)
                            ]),

                            dbc.Row([
                                dbc.Col([
                                    dbc.Label("Data: "),
                                    dcc.DatePickerSingle(id='date-receitas',
                                        min_date_allowed=date(2023, 1, 1),
                                        max_date_allowed=date(2030, 12, 31),
                                        date=datetime.today(),
                                        style={"width": "100%"}
                                    ),
                                ], width=4),

                                dbc.Col([
                                    dbc.Label("Extras"),
                                    dbc.Checklist(
                                        options=[],
                                        value=[],
                                        id="switches-input-receita",
                                        switch=True),
                                ], width=4),

                                dbc.Col([
                                    html.Label("Categoria da receita"),
                                    dbc.Select(id="select_receita", 
                                        options=[{'label': i, 'value': i} for i in cat_receita], 
                                        value=cat_receita[0])
                                ], width=4)
                            ], style={"margin-top": "25px"}),
                            
                            dbc.Row([
                                dbc.Accordion([
                                    dbc.AccordionItem(children=[
                                        dbc.Row([
                                            dbc.Col([
                                                html.Legend("Adicionar categoria", style={'color': 'green'}),
                                                dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-receita", value=""),
                                                html.Br(),
                                                dbc.Button("Adicionar", className="btn btn-success", id="add-category-receita", style={"margin-top": "20px"}),
                                                html.Br(),
                                                html.Div(id="category-div-add-receita", style={}),
                                            ], width=6),

                                            dbc.Col([
                                                html.Legend("Excluir categorias", style={'color': 'red'}),
                                                dbc.Checklist(
                                                    id="checklist-selected-style-receita",
                                                    options=[],
                                                    value=[],
                                                    label_checked_style={"color": "red"},
                                                    input_checked_style={"backgroundColor": "#fa7268",
                                                        "borderColor": "#ea6258"},
                                                ),                                                            
                                                dbc.Button("Remover", color="warning", id="remove-category-receita", style={"margin-top": "20px"}),
                                            ], width=6)
                                        ]),
                                    ], title="Adicionar/Remover Categorias"),
                                ], flush=True, start_collapsed=True, id='accordion-receita'),
                                        
                                    html.Div(id="id_teste_receita", style={"padding-top": "20px"}),
                                
                                    dbc.ModalFooter([
                                        dbc.Button("Adicionar Receita", id="salvar_receita", color="success"),
                                        dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left", trigger="click"),
                                        ])
                                ], style={"margin-top": "25px"}),
                            ])
                    ],
                    style={"background-color": "rgba(17, 140, 79, 0.05)"},
                    id="modal-novo-receita",
                    size="lg",
                    is_open=False,
                    centered=True,
                    backdrop=True)
                ]),


                # Modal DESPESA
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('Adicionar despesa')),
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Descrição: "),
                                dbc.Input(placeholder="Ex.: Gasolina, Merccado...", id="txt-despesa"),
                            ], wwidth=6),
                        ]),

                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Data: "),
                                dcc.DatePickerSingle(id='date-despesas',
                                    min_date_allowed=date(2023, 1, 1),
                                    max_date_allowed=date(2030, 12, 31),
                                    date=datetime.today(),
                                    style={"width": "100%"}
                                ),
                            ], width=4),

                            dbc.Col([
                                dbc.Label("Opções Extras"),
                                dbc.Checklist(
                                    options=[{"label": "Foi recebida", "value": 1}, 
                                        {"label": "Receita Recorrente", "value": 2}],
                                    value=[1],
                                    id='switches-input-despesa',
                                    switch=True
                                ),
                            ], width=4),

                            dbc.Col([
                                html.Label("Categoria da despesa"),
                                dbc.Select(id="select_despesa", 
                                    options=[{'label': i, 'value': i} for i in cat_despesa], 
                                    value=cat_despesa[0])
                            ], width=4),
                        ], style={"margin-top": "25px"}),

                        dbc.Row([
                            dbc.Accordion([
                                dbc.AccordionItem(children=[
                                    dbc.Row([
                                        dbc.Col([
                                            html.Legend("Adicionar categoria", style={'color': 'green'}),
                                            dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-despesa", value=""),
                                            html.Br(),
                                            dbc.Button("Adicionar", className="btn btn-success", id="add-category-despesa", style={"margin-top": "20px"}),
                                            html.Br(),
                                            html.Div(id="category-div-add-despesa", style={}),
                                        ], width=6),

                                        dbc.Col([
                                            html.Legend("Excluir categoria", style={'color': 'red'}),
                                            dbc.Checklist(
                                                    id="checklist-selected-style-despesa",
                                                    options=[],
                                                    value=[],
                                                    label_checked_style={"color": "red"},
                                                    input_checked_style={"backgroundColor": "#fa7268",
                                                        "borderColor": "#ea6258"},
                                            ),
                                            dbc.Buutton("Remover", color="warning", id="remove-category-despesa", style={"margin-top": "20px"}), 
                                        ], width=6),
                                    ]),
                                ], title="Adicioanr/Remover Categorias"),
                            ], flush=True, start_collapsed=True, id="accordion-despea"),

                            dbc.ModalFooter([
                                dbc.Button("Adiocionar despesa", color="error", id="salvar_despesa", value="despesa"),
                                dbc.Popover(dbc.PopoverBody("Despesa Salva"), target="salvar_despesa", placement="left", trigger="click"),
                            ]),
                        ], style={"margin-top": "25px"}),
                    ]),
                ], 
                style={"background-color": "rgba(17, 140, 79, 0.05)"},
                id="modal-novo-despesa",
                size="lg",
                is_open=False,
                centered=True,
                backdrop=True),


# === Seção NAV === #
                html.Hr(),
                dbc.Nav([
                    dbc.NavLink("Dashboard", href="/dashboars", active="exact"),
                    dbc.NavLink("Extratos", href="/extratos", active="exact"),
                ], vertical=True, pills=True, id='nav-buttons', style={"margin-butttom": "50px"}),
        ], id='sidebar_completa')



# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-receita', 'n_clicks'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    

# Pop-up despesa
@app.callback(
    Output('modal-novo-despesa', 'is_open'),
    Input('open-novo-despesa', 'n_clicks'),
    State('modal-novo-despesa', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open


# Enviar Form receita
@app.callback(
    Output('store-receitas', 'data'),
    Input('salvar_receita', 'n_clicks'),
    [
        State('txt-receita', 'value'),
        State('valor_receita', 'value'),
        State('date-receitas', 'date'),
        State('switches-input-receita', 'value'),
        State('select_receita', 'value'),
        State('store-receitas', 'data')
    ]
)
def salve_form_receita(n, descricao, valor, date, switches, categoria, dict_receitas):
    # import pdb
    # pdb.set_trace()

    df_receitas = pd.DataFrame(dict_receitas)
    
    if n and not(valor == "" or valor == None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria

        recebido = 1 if 1 in switches else 0
        fixo = 1 if 2 in switches else 0

        df_receitas.loc[df_receitas.shape[0]] = [valor, recebido, fixo, date, categoria, descricao]
        df_receitas.to_csv("df_receitas.csv")

    data_return = df_receitas.to_dict()
    return data_return


# Enviar Form despesa
@app.callback(
    Output('store-despesas', 'data'),
    Input("salvar_despesa", "n_clicks"),
    [
        State("valor_despesa", "value"),
        State("switches-input-despesa", "value"),
        State("select_despesa", "value"),
        State("date-despesas", "date"),
        State("txt-despesa", "value"),
        State('store-despesas', 'data')
    ])
def salve_form_despesa(n, valor, switches, descricao, date, txt, dict_despesas):
    df_despesas = pd.DataFrame(dict_despesas)

    if n and not(valor == "" or valor== None):
        valor = round(valor, 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria

        recebido = 1 if 1 in switches else 0
        fixo = 0 if 2 in switches else 0
        
        if descricao == None or descricao == "":
            descricao = 0

        df_despesas.loc[df_despesas.shape[0]] = [valor, recebido, fixo, date, descricao, txt]
        df_despesas.to_csv("df_despesas.csv")

    data_return = df_despesas.to_dict()
    return data_return