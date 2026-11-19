"""第 58 批：角色从斜坡走到台阶，前脚掌埋进地面，后脚又悬空，跑起来还一抽一抽..."""

def lowest_foot(samples):
    """返回脚掌最低采样点。"""
    raise NotImplementedError("TODO: lowest_foot")

def pelvis_offset(leg_length, current):
    """返回骨盆高度偏移。"""
    raise NotImplementedError("TODO: pelvis_offset")

def biped_balance(left, right):
    """返回双足平衡高度。"""
    raise NotImplementedError("TODO: biped_balance")

def stair_ray_hits(hits):
    """统计台阶射线命中数。"""
    raise NotImplementedError("TODO: stair_ray_hits")

def platform_velocity(base, platform):
    """继承移动平台速度。"""
    raise NotImplementedError("TODO: platform_velocity")

def root_motion_weight(root_weight, ik_weight):
    """返回根运动与 IK 权重。"""
    raise NotImplementedError("TODO: root_motion_weight")

def knee_limit(angle, max_angle):
    """限制膝盖角度。"""
    raise NotImplementedError("TODO: knee_limit")

def speed_smooth(speed, max_speed):
    """按速度返回平滑权重。"""
    raise NotImplementedError("TODO: speed_smooth")

def contact_sync(local, remote):
    """同步接触点。"""
    raise NotImplementedError("TODO: contact_sync")

def normal_align(angle, slope):
    """按地形法线对齐脚掌。"""
    raise NotImplementedError("TODO: normal_align")

def event_lock(event_time, key_time, threshold):
    """锁定脚部事件帧。"""
    raise NotImplementedError("TODO: event_lock")

def lod_ik_weight(distance, max_distance):
    """按 LOD 返回 IK 权重。"""
    raise NotImplementedError("TODO: lod_ik_weight")
