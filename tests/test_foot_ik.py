import pytest
from gameplay import foot_ik as mod

CASES = [
    ("lowest", 'm.lowest_foot([0.2, 0.1, 0.3]) == approx(0.1)'),
    ("pelvis", 'm.pelvis_offset(1.0, 0.8) == approx(0.2)'),
    ("balance", 'm.biped_balance(1.0, 3.0) == approx(2.0)'),
    ("stair", 'm.stair_ray_hits([True, False, True]) == 2'),
    ("stair_zero", 'm.stair_ray_hits([]) == 0'),
    ("platform", 'm.platform_velocity(1.0, 2.0) == approx(3.0)'),
    ("root", 'm.root_motion_weight(0.5, 0.8) == approx(0.5)'),
    ("knee", 'm.knee_limit(120.0, 90.0) == approx(90.0)'),
    ("speed", 'm.speed_smooth(2.0, 4.0) == approx(0.5)'),
    ("speed_zero", 'm.speed_smooth(0.0, 4.0) == approx(0.0)'),
    ("contact", 'm.contact_sync(1.0, 3.0) == approx(2.0)'),
    ("normal", 'm.normal_align(10.0, 5.0) == approx(15.0)'),
    ("event", 'm.event_lock(1.01, 1.0, 0.02) == approx(1.0)'),
    ("lod_near", 'm.lod_ik_weight(0.0, 10.0) == approx(1.0)'),
    ("lod_far", 'm.lod_ik_weight(10.0, 10.0) == approx(0.0)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
