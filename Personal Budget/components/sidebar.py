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



# ========= Layout ========= #
layout = dbc.Col([
                html.H1("MyBudget", className="text-primary"),
                html.P("By Vicentin", className="text-info"),
                html.Hr(),

# === Seção PERFIL === #
                dbc.Button(id='botao_avatar',
                    children=[html.Img(src='/assets/img_hom.png', id='avatar_change', alt='Avatar', className='perfil_avatar')], style={'background-color': 'transparent', 'border-color': 'transparent'}),
                                                                                                                                        
# === Seção NOVO === #
                dbc.Row([
                    dbc.Col([
                        dbc.Button(color='success', id='open-novo-receita', childdren=['+ Receita'])
                    ], width=6),
                    dbc.Col([
                        dbc.Button(color='danger', id='open-novo-despesa', childdren=['- Despesa'])
                    ], width=6),
                ]),

# === Seção NAV === #
                html.Hr(),
                dbc.Nav([
                    dbc.NavLink("Dashboard", href="/dashboars", active="exact"),
                    dbc.NavLink("Extratos", href="/extratos", active="exact"),
                ], vertical=True, pills=True, id='nav-buttons', style={"margin-butttom": "50px"}),



        ], id='sidebar_completa')



# =========  Callbacks  =========== #
# Pop-up receita
