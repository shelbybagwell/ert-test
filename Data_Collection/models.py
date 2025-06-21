import json
import jsonpickle


class RTSW_data:
    def __init__(
        self,
        time_tag,
        speed,
        density,
        temperature,
        bx,
        by,
        bz,
        bt,
        vx,
        vy,
        vz,
        propagated_time_tag,
    ) -> None:
        self.time_tag: str = time_tag
        self.speed: float = speed
        self.density: float = density
        self.temperature: int = temperature
        self.bx: float = bx
        self.by: float = by
        self.bz: float = bz
        self.bt: float = bt
        self.vx: float = vx
        self.vy: float = vy
        self.vz: float = vz
        self.propagated_time_tag: str = propagated_time_tag
