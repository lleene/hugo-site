from sympy import Symbol, log, sin
from scipy import constants
from quantiphy import Quantity
import control as ct

eval_constants = {
    "k": constants.k,  # Boltzmann contant
    "T": constants.convert_temperature(25.0, "Celsius", "Kelvin"),
    "q": constants.e,  # Elementary charge
}

_pi = constants.pi
_kT = constants.Boltzmann * constants.convert_temperature(25.0, "Celsius", "Kelvin")


class Crystal:
    def __init__(self, frequency: float = 4.8e7, noise_floor_dBc: float = -160):
        self.frequency = frequency
        self.noise_floor_dBc = noise_floor_dBc
        ## TODO low-frequency jitter offset contribution

    def xtal_jitter(self, bandwidth, ref_frequency):
        """XTAL jitter estimate over bandwidth"""
        return Quantity(
            (
                2
                * 10 ** (self.noise_floor_dBc / 10)
                * bandwidth
                / (ref_frequency * 2 * _pi) ** 2
            )
            ** 0.5,
            units="s_rms",
        )


class Oscillator:
    """
    VCO Phase-Noise Model of LC Oscillator

    Bandwidth upper limit is set by the refence clock
    Back off by 10x in sampled systems for stability
    More accurately take xtal into account and equate jitter

    Reference B. Razavi, "Jitter-Power Trade-Offs in PLLs,"
    in IEEE Transactions on Circuits and Systems I: Regular Papers,
    vol. 68, no. 4, pp. 1381-1387, April 2021, doi: 10.1109/TCSI.2021.3057580.
    """

    def __init__(
        self,
        f_center: float = 5e9,
        vout_max: float = 1.0,
        ibias: float = 5.0e-3,
        q_factor: float = 10,
        eta: float = 2.4,  # noise excess factor (1+gamma)
    ):
        self.R = _pi * vout_max / ibias / 2
        self.f_center = f_center
        self.vout_max = vout_max
        self.q_factor = q_factor
        self.ibias = ibias
        self.eta = eta

    @property
    def vco_alpha(self):
        """Oscillator Noise Figure alpha"""
        return (
            _kT / (self.q_factor**2) * self.eta * (_pi / self.ibias) ** 2 / self.R / 8
        )

    def pll_phase_noise(self, pll_bandwidth):
        """Estimate on a LC oscillator phase-noise as alpha/f**2"""
        return self.vco_alpha * (self.f_center / pll_bandwidth) ** 2

    def pll_jitter(self, pll_bandwidth, ref_frequency):
        """PLL jitter estimate due to VCO"""
        return Quantity(
            (
                4
                * self.pll_phase_noise(pll_bandwidth)
                * pll_bandwidth
                / (ref_frequency * 2 * _pi) ** 2
            )
            ** 0.5,
            units="s_rms",
        )

    def opt_bandwidth(self, ref_xtal: Crystal):
        """Optimal PLL bandwidth for matching reference noise."""
        f_ratio = self.f_center / ref_xtal.frequency
        eff_ref_noise = 2 * 10 ** (ref_xtal.noise_floor_dBc / 10) * f_ratio**2
        return Quantity(
            (4 * self.vco_alpha * self.f_center**2 / _pi / eff_ref_noise) ** 0.5,
            units="Hz",
        )

    def jitter_tol(self, adc_tol_db: float, adc_resolution: float, adc_clock: float):
        """Jitter tolerance calculation for m-dB penalty in ADC performance"""
        return Quantity(
            (
                (10 ** (adc_tol_db / 10) - 1)
                / (3 * _pi**2 * adc_clock**2 * 2 ** (2 * adc_resolution - 1))
            )
            ** 0.5,
            units="s_rms",
        )


# LC Tank Parameter Selection
# E. Hegazi, H. Sjoland and A. A. Abidi,
# "A filtering technique to lower LC oscillator phase noise,"
# in IEEE Journal of Solid-State Circuits,
# vol. 36, no. 12, pp. 1921-1930, Dec. 2001, doi: 10.1109/4.972142
# A. Mazzanti and P. Andreani,
# "Class-C Harmonic CMOS VCOs, With a General Result on Phase Noise,"
# in IEEE Journal of Solid-State Circuits,
# vol. 43, no. 12, pp. 2716-2729, Dec. 2008,


class Divider:
    # Error-Feedback Topology
    # https://www.youtube.com/watch?v=t1TY-D95CY8&t=4373s

    ω = Symbol("ω")

    def __init__(self, order: int = 2, fb_int:int = 100, fb_frac:float = 0.1337):
        self.fb_int = fb_int
        self.fb_frac = fb_frac
        self.order = order

    @property
    def noise_function_approx(self):
        return (_pi / 3 / self.ω) ** self.order

    @property
    def noise_function_exact(self):
        return (2 * sin(self.ω / 2)) ** self.order

    @property
    def psd_out(self):
        return self.noise_function_exact**2 / 12
    
    @property
    def modulator_c2p(self):
        return ct.tf([0,1],[1,-1],dt=True)*(2*_pi/(self.fb_int+self.fb_frac))

    @property
    def pll_ntf(self):
        pass

    @property
    def modulator_response_ss(self):
        return ct.tf2ss(self.modulator_c2p) * ct.tf2ss(self.pll_ntf)
