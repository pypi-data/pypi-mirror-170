import json
from typing import List

class MDSettings():
    def __init__(
            self,
            ens : str,
            dt : float,
            nsteps : int,
            trj_freq : int,
            temps : List[float] = None,
            press : List[float] = None,
            tau_t : float = 0.1,
            tau_p : float = 0.5,
            pka_e : float = None,
            neidelay : int = None,
            no_pbc : bool = False,
            use_clusters : bool = False,
            relative_epsilon : float = None,
            relative_v_epsilon : float = None,
            ele_temp_f : float = None,
            ele_temp_a : float = None,
    )->None:
        self.ens = ens
        self.temps = temps
        self.press = press
        self.dt = dt
        self.nsteps = nsteps
        self.trj_freq = trj_freq,
        self.pka_e = pka_e
        self.neidelay = neidelay
        self.no_pbc = no_pbc
        self.tau_t = tau_t
        self.tau_p = tau_p
        self.use_clusters = use_clusters
        self.relative_epsilon = relative_epsilon
        self.relative_v_epsilon = relative_v_epsilon
        self.ele_temp_f = ele_temp_f
        self.ele_temp_a = ele_temp_a


    def to_str(
            self,
    )->str:
        return json.dumps(
            self, 
            default=lambda o: o.__dict__, 
            sort_keys=True, 
            indent=4
        )
