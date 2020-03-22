import pytest


class TestAuidtPlan:

    @pytest.mark.parametrize("planname", [""])
    def test_query_plan(self, auditplan_setting, planname):
        auditplan_setting.query_flow(planname)
