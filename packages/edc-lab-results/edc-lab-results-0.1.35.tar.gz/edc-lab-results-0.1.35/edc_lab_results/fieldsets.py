from typing import List, Optional, Tuple

from django_audit_fields import audit_fieldset_tuple

panel_conclusion_fieldset: Tuple[str, dict] = (
    "Conclusion",
    {"fields": ("results_abnormal", "results_reportable")},
)
panel_summary_fieldset: Tuple[str, dict] = ("Summary", {"fields": ("summary",)})


calculate_egfr_fieldset: Tuple[str, dict] = (
    "Calculated eGFR",
    {
        # "classes": ("collapse",),
        "description": "To be calculated (or recalulated) when this form is saved",
        "fields": ["egfr_value", "egfr_units", "egfr_grade"],
    },
)

calculate_egfr_drop_fieldset: Tuple[str, dict] = (
    "Calculated eGFR Drop",
    {
        # "classes": ("collapse",),
        "description": "To be calculated (or recalulated) when this form is saved",
        "fields": ["egfr_drop_value", "egfr_drop_units", "egfr_drop_grade"],
    },
)


class BloodResultFieldsetError(Exception):
    pass


class BloodResultFieldset:
    """A class to generate a modeladmin `fieldsets` using the
    lab panel for this `blood result`.
    """

    def __init__(
        self,
        panel,
        title=None,
        model_cls=None,
        extra_fieldsets: Optional[List[Tuple[int, Tuple[str, dict]]]] = None,
        excluded_utest_ids=None,
        exclude_units=None,
    ):
        self.panel = panel
        self.title = title or panel.name
        self.model_cls = model_cls
        self.extra_fieldsets = extra_fieldsets
        self.excluded_utest_ids = excluded_utest_ids or []
        self.exclude_units = exclude_units

    def __repr__(self):
        return f"{self.__class__.__name__}({self.panel})"

    def __str__(self):
        return f"{self.__class__.__name__}({self.panel})"

    @property
    def fieldsets(self):
        fieldsets = [
            (None, {"fields": ("subject_visit", "report_datetime")}),
            (self.title, {"fields": ["requisition", "assay_datetime"]}),
        ]
        for item in self.panel.utest_ids:
            if item in self.excluded_utest_ids:
                continue
            try:
                code, title = item
            except ValueError:
                code = item
                title = code.upper()
            fieldsets.append(self.get_panel_item_fieldset(code, title=title))
        fieldsets.extend(
            [
                panel_conclusion_fieldset,
                panel_summary_fieldset,
                audit_fieldset_tuple,
            ]
        )
        for pos, fieldset in self.extra_fieldsets or []:
            if pos < 0:
                fieldsets.append(fieldset)
            else:
                fieldsets.insert(pos, fieldset)
        return tuple(fieldsets)

    def get_panel_item_fieldset(self, code, title=None):
        if not title:
            title = code.upper()
        model_fields = [
            f"{code}_value",
            f"{code}_units",
            f"{code}_abnormal",
            f"{code}_reportable",
        ]
        if self.exclude_units:
            model_fields.remove(f"{code}_units")
        if self.model_cls:
            for field in model_fields:
                try:
                    getattr(self.model_cls, field)
                except AttributeError as e:
                    raise BloodResultFieldsetError(f"{e}. See {self}")

        return (
            title,
            {"fields": model_fields},
        )
