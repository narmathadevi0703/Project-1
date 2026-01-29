from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


def Dash_board(df):

    
    df = df.copy()

   
    qs_numeric_cols = [
        'Academic Reputation',
        'Employer Reputation',
        'Citations per Faculty',
        'Faculty Student',
        'International Faculty',
        'International Students',
        'Employment Outcomes',
        'Sustainability',
        'QS Overall Score'
    ]

    
    for col in qs_numeric_cols:
        if col in df.columns:
            df.loc[:, col] = (
                df[col]
                .astype(str)
                .str.strip()
                .replace('', pd.NA)
            )

            df.loc[:, col] = pd.to_numeric(
                df[col],
                errors='coerce'
            )

    
    available_columns = [c for c in qs_numeric_cols if c in df.columns]

    if not available_columns:
        print("No QS numeric indicators found.")
        return

   
    df.loc[:, available_columns] = df[available_columns].fillna(0)


    if 'Location' in df.columns:
        country_options = sorted(df['Location'].dropna().unique())
    else:
        country_options = []

  
    if 'QS Overall Score' in df.columns:
        df = df.sort_values(
            by='QS Overall Score',
            ascending=False
        ).head(50)

   
    app = Dash(__name__)

   
    app.layout = html.Div([

        html.H1(
            "QS World University Rankings 2025",
            style={'textAlign': 'center', 'color': '#003366'}
        ),

        html.P(
            "Interactive dashboard to analyze QS ranking indicators "
            "such as Academic Reputation, Citations per Faculty, and Overall Score.",
            style={'textAlign': 'center', 'fontSize': 16}
        ),

        
        dcc.Dropdown(
            id="metric_dropdown",
            options=[
                {"label": col, "value": col}
                for col in available_columns
            ],
            value='QS Overall Score' if 'QS Overall Score' in available_columns else available_columns[0],
            clearable=False,
            style={'width': '60%', 'margin': '15px auto'}
        ),

        dcc.Dropdown(
            id="country_dropdown",
            options=[
                {"label": c, "value": c}
                for c in country_options
            ],
            placeholder="Filter by Country (Optional)",
            multi=True,
            style={'width': '60%', 'margin': '10px auto'}
        ),

        
        dcc.Graph(
            id="metric_graph",
            style={'width': '95%', 'height': '65vh', 'margin': 'auto'}
        )

    ], style={'padding': '20px', 'backgroundColor': '#ffffff'})

    
    @app.callback(
        Output("metric_graph", "figure"),
        [
            Input("metric_dropdown", "value"),
            Input("country_dropdown", "value")
        ]
    )
    def update_graph(metric, countries):

        plot_df = df.copy()

        if countries and 'Location' in plot_df.columns:
            plot_df = plot_df[plot_df['Location'].isin(countries)]

        x_axis = (
            'Institution Name'
            if 'Institution Name' in plot_df.columns
            else plot_df.index
        )

        fig = px.bar(
            plot_df,
            x=x_axis,
            y=metric,
            title=f"{metric} Comparison Across Universities",
            labels={
                x_axis: "University",
                metric: metric
            },
            hover_data=['Location'] if 'Location' in plot_df.columns else None
        )

        fig.update_layout(
            xaxis_tickangle=-45,
            title_font_size=20,
            font=dict(size=14),
            plot_bgcolor='white',
            paper_bgcolor='white'
        )

        return fig

    app.run(debug=False)
