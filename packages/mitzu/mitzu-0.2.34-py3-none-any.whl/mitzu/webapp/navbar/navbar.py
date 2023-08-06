from __future__ import annotations

import os

import dash_bootstrap_components as dbc
import mitzu.webapp.navbar.metric_type_handler as MNB
import mitzu.webapp.navbar.project_dropdown as PD
import mitzu.webapp.webapp as WA
from dash import html

MANAGE_PROJECTS_LINK = os.getenv("MANAGE_PROJECTS_LINK")
SIGN_OUT_URL = os.getenv("SIGN_OUT_URL")
LOGO = "navbar_logo"
MORE_DD = "navbar_more_dropdown"


def create_mitzu_navbar(webapp: WA.MitzuWebApp) -> dbc.Navbar:

    if webapp.logo_path is not None:
        logo_image = [html.Img(src=webapp.logo_path, height="32px", className="logo")]
    else:
        logo_image = [html.H2("Mitzu", className="logo")]

    res = dbc.Navbar(
        children=dbc.Container(
            children=[
                dbc.Row(
                    children=[
                        dbc.Col(
                            html.A(
                                # Use row and col to control vertical alignment of logo / brand
                                children=logo_image,
                                id=LOGO,
                                href="/",
                                style={"textDecoration": "none"},
                            )
                        ),
                        dbc.Col(PD.create_project_dropdown(webapp)),
                        dbc.Col(
                            MNB.MetricTypeHandler.from_metric_type(
                                MNB.MetricType.SEGMENTATION
                            ).component
                        ),
                        dbc.Col(
                            dbc.DropdownMenu(
                                [
                                    dbc.DropdownMenuItem("Projects", header=True),
                                    dbc.DropdownMenuItem(
                                        "Manage projects",
                                        external_link=True,
                                        href=MANAGE_PROJECTS_LINK,
                                        target="_blank",
                                        disabled=(MANAGE_PROJECTS_LINK is None),
                                    ),
                                    dbc.DropdownMenuItem(divider=True),
                                    dbc.DropdownMenuItem(
                                        "Sign out",
                                        disabled=(SIGN_OUT_URL is None),
                                        href=SIGN_OUT_URL,
                                    ),
                                ],
                                id=MORE_DD,
                                label="More",
                                size="sm",
                                color="dark",
                                in_navbar=True,
                                align_end=True,
                                direction="down",
                            )
                        ),
                    ],
                ),
            ],
            fluid=True,
        ),
    )
    return res
