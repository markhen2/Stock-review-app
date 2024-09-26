import _plotly_utils.basevalidators


class ZautoValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(self, plotly_name="zauto", parent_name="heatmapgl", **kwargs):
        super(ZautoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            implied_edits=kwargs.pop("implied_edits", {}),
            **kwargs,
        )
