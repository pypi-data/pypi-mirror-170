from __future__ import annotations

import pprint
import traceback
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union
from urllib.parse import ParseResult, urlparse

import dash.development.base_component as bc
import dash_bootstrap_components as dbc
import mitzu.model as M
import mitzu.serialization as SE
import mitzu.webapp.authorizer as AUTH
import mitzu.webapp.complex_segment_handler as CS
import mitzu.webapp.dates_selector_handler as DS
import mitzu.webapp.event_segment_handler as ES
import mitzu.webapp.graph_handler as GH
import mitzu.webapp.metric_config_handler as MC
import mitzu.webapp.metric_segments_handler as MS
import mitzu.webapp.navbar.metric_type_handler as MNB
import mitzu.webapp.navbar.navbar as MN
import mitzu.webapp.simple_segment_handler as SS
import mitzu.webapp.webapp as WA
from dash import Dash, ctx, dcc, html
from dash.dependencies import ALL, Input, Output, State
from mitzu.webapp.helper import (
    LOGGER,
    deserialize_component,
    find_components,
    find_event_field_def,
    get_path_project_name,
)
from mitzu.webapp.persistence import PersistencyProvider

PRINTER = pprint.PrettyPrinter(indent=4)


MAIN = "main"
PATH_RESULTS = "results"
MITZU_LOCATION = "mitzu_location"
MAIN_CONTAINER = "main_container"
GRAPH_CONTAINER = "graph_container"
GRAPH_CONTAINER_HEADER = "graph_container_header"
GRAPH_REFRESH_BUTTON = "graph_refresh_button"

GRAPH_VAL_CHART = "chart"
GRAPH_VAL_TABLE = "table"
GRAPH_VAL_SQL = "sql"

SELECT_PROJECT_DIV = "select_project_div"
GRAPH_TOOLBAR_BUTTON_HEIGHT = "30px"


def create_hint_div(text: str) -> html.Div:
    return html.Div(children=text, className=GRAPH_CONTAINER)


def create_graph_container_toolbar():
    return dbc.Row(
        dbc.Col(
            dbc.InputGroup(
                children=[
                    dbc.Button(
                        children=[html.B(className="bi bi-arrow-clockwise")],
                        size="sm",
                        color="primary",
                        className=GRAPH_REFRESH_BUTTON,
                        id=GRAPH_REFRESH_BUTTON,
                        style={
                            "height": GRAPH_TOOLBAR_BUTTON_HEIGHT,
                        },
                    ),
                    dbc.Button(
                        children=[html.B(className="bi bi-graph-up")],
                        size="sm",
                        color="info",
                        className=GRAPH_REFRESH_BUTTON,
                        id=GRAPH_VAL_CHART,
                        outline=False,
                        style={
                            "height": GRAPH_TOOLBAR_BUTTON_HEIGHT,
                        },
                    ),
                    dbc.Button(
                        children=[
                            html.B(
                                className="bi bi-grid-3x3",
                            )
                        ],
                        size="sm",
                        color="info",
                        className=GRAPH_REFRESH_BUTTON,
                        id=GRAPH_VAL_TABLE,
                        outline=True,
                        style={
                            "height": GRAPH_TOOLBAR_BUTTON_HEIGHT,
                        },
                    ),
                    dbc.Button(
                        children=[html.Span("sql")],
                        size="sm",
                        color="info",
                        className=GRAPH_REFRESH_BUTTON,
                        outline=True,
                        id=GRAPH_VAL_SQL,
                        style={
                            "height": GRAPH_TOOLBAR_BUTTON_HEIGHT,
                        },
                    ),
                ],
            )
        )
    )


def create_graph_container(graph: dcc.Graph, webapp: MitzuWebApp):
    metrics_config_card = MC.MetricConfigHandler.from_metric(
        None, webapp._discovered_datasource.get_value()
    ).component
    toolbar = create_graph_container_toolbar()
    graph_container = dbc.Card(
        children=[
            dbc.CardBody(
                children=[
                    html.Div([metrics_config_card, toolbar]),
                    dcc.Loading(
                        className=GRAPH_CONTAINER,
                        id=GRAPH_CONTAINER,
                        type="dot",
                        children=[graph],
                    ),
                ],
            ),
        ],
    )
    return graph_container


@dataclass
class MitzuWebApp:

    persistency_provider: PersistencyProvider
    app: Dash
    authorizer: Optional[AUTH.MitzuAuthorizer]
    logo_path: Optional[str] = None
    viz_type: str = GRAPH_VAL_CHART

    _discovered_datasource: M.ProtectedState[M.DiscoveredProject] = M.ProtectedState[
        M.DiscoveredProject
    ]()
    _current_project: Optional[str] = None

    def get_discovered_project(self) -> Optional[M.DiscoveredProject]:
        return self._discovered_datasource.get_value()

    def _load_dataset_model(self, path_project_name: str):
        if (
            path_project_name == self._current_project
            and self._discovered_datasource.has_value()
        ):
            return
        self._current_project = path_project_name
        if path_project_name:
            print(f"Loading project: {path_project_name}")
            dd = self.persistency_provider.get_project(path_project_name)
            if dd is not None:
                dd.project._discovered_project.set_value(dd)
            self._discovered_datasource.set_value(dd)

    def init_app(self):
        loc = dcc.Location(id=MITZU_LOCATION, refresh=False)
        navbar = MN.create_mitzu_navbar(self)

        metric_segments_div = MS.MetricSegmentsHandler.from_metric(
            discovered_project=self._discovered_datasource.get_value(),
            metric=None,
            metric_type=MNB.MetricType.SEGMENTATION,
        ).component

        graph = html.Div(className=GRAPH_CONTAINER)
        graph_container = create_graph_container(graph, self)
        self.app.layout = html.Div(
            children=[
                loc,
                navbar,
                dbc.Container(
                    children=[
                        dbc.Row(
                            children=[
                                dbc.Col(metric_segments_div, lg=4, md=12),
                                dbc.Col([graph_container], lg=8, md=12),
                            ],
                            justify="start",
                            align="top",
                            className="g-1",
                        ),
                    ],
                    fluid=True,
                ),
            ],
            className=MAIN,
            id=MAIN,
        )

        self.create_callbacks()

    def get_metric_from_query(
        self, query: str
    ) -> Tuple[Optional[M.Metric], MNB.MetricType]:
        discovered_project = self.get_discovered_project()
        if discovered_project is None:
            return None, MNB.MetricType.SEGMENTATION
        try:
            metric = SE.from_compressed_string(query, discovered_project.project)
        except Exception:
            metric = None

        metric_type = MNB.MetricType.from_metric(metric)
        return metric, metric_type

    def create_metric_from_compoments(
        self,
        metric_seg_children: List[bc.Component],
        mc_children: List[bc.Component],
        discovered_project: Optional[M.DiscoveredProject],
        metric_type: MNB.MetricType,
    ) -> Optional[M.Metric]:
        if discovered_project is None:
            return None

        segments = MS.MetricSegmentsHandler.from_component(
            discovered_project, html.Div(children=metric_seg_children)
        ).to_metric_segments()
        metric: Optional[Union[M.Segment, M.Conversion]] = None
        if metric_type == MNB.MetricType.CONVERSION:
            metric = M.Conversion(segments)
        elif metric_type == MNB.MetricType.SEGMENTATION:
            if len(segments) >= 1:
                metric = segments[0]

        if metric is None:
            return None

        metric_config_comp = MC.MetricConfigHandler.from_component(
            html.Div(children=mc_children), discovered_project
        )
        metric_config, conv_tw = metric_config_comp.to_metric_config_and_conv_window()
        if metric_config.agg_type:
            agg_str = M.AggType.to_agg_str(
                metric_config.agg_type, metric_config.agg_param
            )
        else:
            agg_str = None

        group_by = None
        if len(metric_seg_children) > 0:
            group_by_paths = find_components(
                CS.COMPLEX_SEGMENT_GROUP_BY, metric_seg_children[0]
            )
            if len(group_by_paths) == 1:
                gp = group_by_paths[0].value
                group_by = find_event_field_def(gp, discovered_project) if gp else None

        if isinstance(metric, M.Conversion):
            return metric.config(
                time_group=metric_config.time_group,
                conv_window=conv_tw,
                group_by=group_by,
                lookback_days=metric_config.lookback_days,
                start_dt=metric_config.start_dt,
                end_dt=metric_config.end_dt,
                custom_title="",
                aggregation=agg_str,
            )
        elif isinstance(metric, M.Segment):
            return metric.config(
                time_group=metric_config.time_group,
                group_by=group_by,
                lookback_days=metric_config.lookback_days,
                start_dt=metric_config.start_dt,
                end_dt=metric_config.end_dt,
                custom_title="",
                aggregation=agg_str,
            )
        raise Exception("Invalid metric type")

    def handle_discovered_datasource(
        self, parse_result: ParseResult
    ) -> Optional[M.DiscoveredProject]:
        path_project_name = get_path_project_name(parse_result, self.app)
        if path_project_name is None:
            return None
        self._load_dataset_model(path_project_name)
        return self.get_discovered_project()

    def handle_metric_changes(
        self,
        parse_result: ParseResult,
        discovered_project: M.DiscoveredProject,
        metric_seg_divs: List[Dict],
        metric_configs: List[Dict],
        metric_type_value: str,
    ) -> Tuple[Optional[M.Metric], MNB.MetricType]:
        metric: Optional[M.Metric] = None
        metric_type = MNB.MetricType.SEGMENTATION
        if ctx.triggered_id == WA.MITZU_LOCATION:
            query = parse_result.query[2:]
            metric, metric_type = self.get_metric_from_query(query)
        else:
            metric_seg_children = [deserialize_component(c) for c in metric_seg_divs]
            metric_configs_children = [deserialize_component(c) for c in metric_configs]
            metric_type = MNB.MetricType(metric_type_value)
            metric = self.create_metric_from_compoments(
                metric_seg_children,
                metric_configs_children,
                discovered_project,
                metric_type,
            )
        return metric, metric_type

    def create_callbacks(self):
        SS.SimpleSegmentHandler.create_callbacks(self.app)

        all_input_comps = {
            "all_inputs": {
                "href": Input(WA.MITZU_LOCATION, "href"),
                "metric_type_value": Input(MNB.METRIC_TYPE_DROPDOWN, "value"),
                "event_name_dd_value": Input(
                    {"type": ES.EVENT_NAME_DROPDOWN, "index": ALL}, "value"
                ),
                "property_operator_dd_value": Input(
                    {"type": SS.PROPERTY_OPERATOR_DROPDOWN, "index": ALL}, "value"
                ),
                "property_name_dd_value": Input(
                    {"type": SS.PROPERTY_NAME_DROPDOWN, "index": ALL}, "value"
                ),
                "property_value_input": Input(
                    {"type": SS.PROPERTY_VALUE_INPUT, "index": ALL}, "value"
                ),
                "group_by_dd_value": Input(
                    {"type": CS.COMPLEX_SEGMENT_GROUP_BY, "index": ALL}, "value"
                ),
                "time_group_dd_value": Input(DS.TIME_GROUP_DROWDOWN, "value"),
                "custom_start_date_value": Input(DS.CUSTOM_DATE_PICKER, "start_date"),
                "custom_end_date_value": Input(DS.CUSTOM_DATE_PICKER, "end_date"),
                "lookback_dd_value": Input(DS.LOOKBACK_WINDOW_DROPDOWN, "value"),
                "conv_window_tg_dd_value": Input(
                    MC.CONVERSION_WINDOW_INTERVAL_STEPS, "value"
                ),
                "conv_window_interval_value": Input(
                    MC.CONVERSION_WINDOW_INTERVAL, "value"
                ),
                "agg_type_dd_value": Input(MC.AGGREGATION_TYPE, "value"),
                "refresh_n_clicks": Input(GRAPH_REFRESH_BUTTON, "n_clicks"),
            }
        }

        @self.app.callback(
            output=[
                Output(MS.METRIC_SEGMENTS, "children"),
                Output(MC.METRICS_CONFIG_CONTAINER, "children"),
                Output(WA.MITZU_LOCATION, "search"),
                Output(MNB.METRIC_TYPE_DROPDOWN, "value"),
            ],
            inputs=all_input_comps,
            state=dict(
                metric_segment_divs=State(MS.METRIC_SEGMENTS, "children"),
                metric_configs=State(MC.METRICS_CONFIG_CONTAINER, "children"),
            ),
            prevent_initial_call=True,
        )
        def change_layout(
            all_inputs: Dict[str, Any],
            metric_segment_divs: List[Dict],
            metric_configs: List[Dict],
        ) -> Tuple[List[html.Div], List[html.Div], str, str]:

            parse_result = urlparse(all_inputs["href"])
            discovered_project = self.handle_discovered_datasource(parse_result)

            if discovered_project is None:
                def_mc_comp = MC.MetricConfigHandler.from_metric(None, None)
                def_mc_children = def_mc_comp.component.children
                return (
                    [],
                    [c.to_plotly_json() for c in def_mc_children],
                    "?" + parse_result.query[2:],
                    MNB.MetricType.SEGMENTATION.value,
                )

            metric, metric_type = self.handle_metric_changes(
                parse_result=parse_result,
                discovered_project=discovered_project,
                metric_seg_divs=metric_segment_divs,
                metric_configs=metric_configs,
                metric_type_value=all_inputs["metric_type_value"],
            )

            url_search = "?"
            if metric is not None:
                url_search = "?m=" + SE.to_compressed_string(metric)

            metric_segments = MS.MetricSegmentsHandler.from_metric(
                discovered_project=discovered_project,
                metric=metric,
                metric_type=metric_type,
            ).component.children

            metric_segment_comps = [seg.to_plotly_json() for seg in metric_segments]

            mc_children = MC.MetricConfigHandler.from_metric(
                metric, discovered_project
            ).component.children
            metric_config_comps = [c.to_plotly_json() for c in mc_children]

            return (
                metric_segment_comps,
                metric_config_comps,
                url_search,
                metric_type.value,
            )

        @self.app.callback(
            output=[
                Output(GRAPH_CONTAINER, "children"),
                Output(GRAPH_VAL_CHART, "outline"),
                Output(GRAPH_VAL_TABLE, "outline"),
                Output(GRAPH_VAL_SQL, "outline"),
            ],
            inputs={
                **all_input_comps,
                "chart_options": {
                    "graph_viz_table": Input(GRAPH_VAL_TABLE, "n_clicks"),
                    "graph_viz_chart": Input(GRAPH_VAL_CHART, "n_clicks"),
                    "graph_viz_sql": Input(GRAPH_VAL_SQL, "n_clicks"),
                },
            },
            state=dict(
                metric_segment_divs=State(MS.METRIC_SEGMENTS, "children"),
                metric_configs=State(MC.METRICS_CONFIG_CONTAINER, "children"),
            ),
            prevent_initial_call=True,
        )
        def change_graph_container(
            all_inputs: Dict[str, Any],
            chart_options: Dict[str, Any],
            metric_segment_divs: List[Dict],
            metric_configs: List[Dict],
        ) -> Tuple[List[Dict], bool, bool, bool]:
            parse_result = urlparse(all_inputs["href"])
            discovered_project = self.handle_discovered_datasource(parse_result)
            if ctx.triggered_id in [GRAPH_VAL_CHART, GRAPH_VAL_SQL, GRAPH_VAL_TABLE]:
                self.viz_type = ctx.triggered_id
            viz_types = (
                self.viz_type != GRAPH_VAL_CHART,
                self.viz_type != GRAPH_VAL_TABLE,
                self.viz_type != GRAPH_VAL_SQL,
            )

            if discovered_project is None:
                return (
                    [
                        create_hint_div(
                            "Start by selecting a project ..."
                        ).to_plotly_json()
                    ],
                    *viz_types,
                )

            metric, _ = self.handle_metric_changes(
                parse_result=parse_result,
                discovered_project=discovered_project,
                metric_seg_divs=metric_segment_divs,
                metric_configs=metric_configs,
                metric_type_value=all_inputs["metric_type_value"],
            )

            if (
                metric is None
                or (
                    isinstance(metric, M.SegmentationMetric) and metric._segment is None
                )
                or (
                    isinstance(metric, M.ConversionMetric)
                    and len(metric._conversion._segments) == 0
                )
            ):
                return (
                    [create_hint_div("Select the first event ...").to_plotly_json()],
                    *viz_types,
                )

            try:
                if self.viz_type == GRAPH_VAL_CHART:
                    return (
                        [GH.create_graph(metric).to_plotly_json()],
                        *viz_types,
                    )
                elif self.viz_type == GRAPH_VAL_TABLE:
                    return (
                        [GH.create_table(metric).to_plotly_json()],
                        *viz_types,
                    )
                elif self.viz_type == GRAPH_VAL_SQL:
                    return (
                        [GH.create_sql_area(metric).to_plotly_json()],
                        *viz_types,
                    )
            except Exception as exc:
                traceback.print_exc()
                LOGGER.error(exc)
                return (
                    [
                        html.Div(
                            str(exc), style={"min-height": "500px", "color": "red"}
                        ).to_plotly_json()
                    ],
                    *viz_types,
                )
            return (
                [],
                *viz_types,
            )
