import unittest
import sys
sys.path.append('../')
from src.calculate_membership_fee import calculate_membership_fee, OrganisationUnit, OrganisationUnitConfig


class TestCalculateMembershipFee(unittest.TestCase):
    def setUp(self):
        self.client = OrganisationUnit("client", OrganisationUnitConfig(False, 0))
        self.division_a = OrganisationUnit("division_a", OrganisationUnitConfig(False, 0))
        self.division_b = OrganisationUnit("division_b", OrganisationUnitConfig(True, 35000))
        self.area_a = OrganisationUnit("area_a", OrganisationUnitConfig(True, 45000))
        self.area_b = OrganisationUnit("area_b", OrganisationUnitConfig(False, 0))
        self.area_c = OrganisationUnit("area_c", OrganisationUnitConfig(True, 45000))
        self.area_d = OrganisationUnit("area_d", OrganisationUnitConfig(False, 0))
        self.branch_a = OrganisationUnit("branch_a", OrganisationUnitConfig(None, None))
        self.branch_b = OrganisationUnit("branch_b", OrganisationUnitConfig(False, 0))
        self.branch_c = OrganisationUnit("branch_c", OrganisationUnitConfig(False, 0))
        self.branch_d = OrganisationUnit("branch_d", OrganisationUnitConfig(None, None))
        self.branch_e = OrganisationUnit("branch_e", OrganisationUnitConfig(False, 0))
        self.branch_f = OrganisationUnit("branch_f", OrganisationUnitConfig(False, 0))
        self.branch_g = OrganisationUnit("branch_g", OrganisationUnitConfig(False, 0))
        self.branch_h = OrganisationUnit("branch_h", OrganisationUnitConfig(False, 0))
        self.branch_i = OrganisationUnit("branch_i", OrganisationUnitConfig(False, 0))
        self.branch_j = OrganisationUnit("branch_j", OrganisationUnitConfig(False, 0))
        self.branch_k = OrganisationUnit("branch_k", OrganisationUnitConfig(True, 25000))
        self.branch_l = OrganisationUnit("branch_l", OrganisationUnitConfig(False, 0))
        self.branch_m = OrganisationUnit("branch_m", OrganisationUnitConfig(None, None))
        self.branch_n = OrganisationUnit("branch_n", OrganisationUnitConfig(False, 0))
        self.branch_o = OrganisationUnit("branch_o", OrganisationUnitConfig(False, 0))
        self.branch_p = OrganisationUnit("branch_p", OrganisationUnitConfig(False, 0))

        # Adding children to their respective parents
        self.client.add_child(self.division_a)
        self.client.add_child(self.division_b)
        self.division_a.add_child(self.area_a)
        self.division_a.add_child(self.area_b)
        self.division_b.add_child(self.area_c)
        self.division_b.add_child(self.area_d)
        self.area_a.add_child(self.branch_a)
        self.area_a.add_child(self.branch_b)
        self.area_a.add_child(self.branch_c)
        self.area_a.add_child(self.branch_d)
        self.area_b.add_child(self.branch_e)
        self.area_b.add_child(self.branch_f)
        self.area_b.add_child(self.branch_g)
        self.area_b.add_child(self.branch_h)
        self.area_c.add_child(self.branch_i)
        self.area_c.add_child(self.branch_j)
        self.area_c.add_child(self.branch_k)
        self.area_c.add_child(self.branch_l)
        self.area_d.add_child(self.branch_m)
        self.area_d.add_child(self.branch_n)
        self.area_d.add_child(self.branch_o)
        self.area_d.add_child(self.branch_p)


    def test_valid_input(self):
        result = calculate_membership_fee(25000, 'month', self.branch_a)
        self.assertEqual(result, 45000)

    def test_rent_below_min_threshold(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(2000, 'week', self.branch_b)

    def test_rent_above_max_threshold(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(1000000, 'week', self.branch_c)

    def test_org_unit_fixed_membership_fee(self):
        result = calculate_membership_fee(25000, 'month', self.area_a)
        self.assertEqual(result, 45000)

    def test_org_unit_recursive_fixed_membership_fee(self):
        result = calculate_membership_fee(25000, 'month', self.branch_f)
        self.assertEqual(result, 70020)
    
    def test_parent_has_no_fixed_membership_fee_week(self):
        result = calculate_membership_fee(12000, 'week', self.branch_g)
        self.assertEqual(result, 14400)
    
    def test_parent_has_no_fixed_membership_fee_month(self):
        result = calculate_membership_fee(81000, "month", self.branch_e)
        self.assertEqual(result, 226864)
    
    def test_first_parent_has_fixed_membership_fee(self):
        result = calculate_membership_fee(38000, "month", self.branch_j)
        self.assertEqual(result, 45000)
    
    def test_second_parent_has_fixed_membership_fee(self):
        result = calculate_membership_fee(58000, "month", self.branch_o)
        self.assertEqual(result, 35000)