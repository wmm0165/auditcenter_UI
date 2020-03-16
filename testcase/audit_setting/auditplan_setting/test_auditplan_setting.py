import pytest


class TestAuidtPlan:
    # def test_add_auditplan(self, auditplan_setting):
    #     auditplan_setting.add_plan('住院')

    @pytest.mark.parametrize("planname", ["mz"])
    def test_query_plan(self, auditplan_setting, planname):
        auditplan_setting.query_flow(planname)
