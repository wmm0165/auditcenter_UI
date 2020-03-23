import pytest


class TestAuidtPlan:

    @pytest.mark.parametrize("planname", ["mz"])
    def test_query_plan(self, auditplan_setting, planname):
        """查询审方方案"""
        auditplan_setting.query_flow(planname)

    def test_add_plan(self):
        """添加审方方案"""
        pass

    def test_modify_plan(self):
        """修改审方方案"""
        pass

    def test_delete_plan(self):
        """删除审方方案"""
        pass