"""Thrusters amplification circuits."""


def thrusters(amplifier, phase_sequence):
    """Get thrusters signal from a chain of amplifiers."""
    signal = 0
    for phase in phase_sequence:
        amplifier.reset()
        signal = amplifier.execute([phase, signal])
    return signal


def feedback_thrusters(amplifiers, phase_sequence):
    """Get output signal from a chain of thrusters with feedback loop."""
    for amp, phase in zip(amplifiers, phase_sequence):
        # print(f"Init amp {amp} with phase {phase}")
        amp.execute(phase)
    signal = 0
    while not amplifiers[-1].finished:
        for amp in amplifiers:
            signal = amp.execute(signal)
            print(f"Amp {amp} output: {signal}")
            if amp is amplifiers[-1] and signal is not None:
                last_output_from_E = signal
    return last_output_from_E


if __name__ == "__main__":
    import env
    from tests import tests_thrusters
    tests_thrusters.tests()
