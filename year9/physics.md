# Physics Notes

## Curriculum Overview (2025-26)
**Exam Board**: Edexcel IGCSE Physics (4PH1)

### Autumn Term
- **Electricity**: Mastering the relationship between charge, current, voltage, and resistance; rules for series and parallel circuits; calculating electrical power and energy.
- **Waves**: Differentiating between longitudinal and transverse waves; understanding wave properties (amplitude, frequency, wavelength, period).
- **Sound**: Investigating the speed of sound; applications of ultrasound and the human hearing range; using an oscilloscope to analyze sound wave features.

### Spring Term
- **Light**: Laws of reflection and the phenomenon of refraction; mathematical application of Snell’s Law; Total Internal Reflection (TIR) and the critical angle.
- **IGCSE Physics (Spring 2)**: Core units on **Density** (calculating mass/volume) and **Pressure** (pressure in solids, liquids, and gases).

### Summer Term
- **Solids, Liquids, and Gases**: Molecular kinetic theory of the states of matter; calculating Energy and **Specific Heat Capacity** ($c$); the **Ideal Gas Law** ($P_1V_1 = P_2V_2$).
- **Motion**: Representing and analyzing movement using Distance-Time and Velocity-Time graphs; calculating acceleration.

---

## Topics

### Voltage, Current and Circuits

#### Key Definitions
- **Charge**: A property of particles (electrons have negative charge). Cannot be created or destroyed, only moved. Unit: **Coulomb (C)**.
- **Current**: Rate of flow of charge (charge per second). Unit: **Ampere/Amp (A)**.
- **Voltage**: Energy given to charge by the battery to be carried around the circuit. Also the "push" that drives electrons. Unit: **Volt (V)**.
- **Resistance**: Property of a component (lamp, resistor, motor) that slows the flow of current.

#### Circuit Rules — Current
- **Series circuit**: Current is the same everywhere.
- **Parallel circuit**: Current splits at a junction. The branch currents add up to the total (e.g. 0.8A total → 0.2A + 0.6A across two branches).

#### Circuit Rules — Voltage
- **Series circuit**: Voltage is shared between components. Component voltages add up to the battery voltage (e.g. 6V battery, lamp = 4V → resistor = 2V).
- **Parallel circuit**: Each branch has the same voltage as the battery (e.g. 3V battery → every branch = 3V).

#### Worked Example (Parallel with series branch)

```
          ┌──────────────────┬───────────────────────────┐
          │                  │                           │
        (V9)               (V10)                     [Lamp]──(V=3.2V)
          │                  │                           │
      [Battery]           [Lamp]                     [Lamp]──(V=3.6V)
          │                  │                           │
          └──────────────────┴───────────────────────────┘

  Branch 1 (left)   Branch 2 (mid)       Branch 3 (right)
  Battery + V9      1 lamp + V10         2 lamps in series
```

- Right branch (series): 3.2V + 3.6V = **6.8V**
- Parallel rule → all branches equal → **V10 = 6.8V**, **V9 = 6.8V**

#### Hydraulic Analogy (Water Circuit)
Think of an electrical circuit like a water pipe system:

| Electrical | Water equivalent |
|-----------|-----------------|
| Battery | Pump |
| Voltage | Water pressure |
| Current | Flow rate (how much water per second) |
| Resistance | Narrow pipe (restricts flow) |
| Charge | Water itself |

- **Series**: Like water through one pipe with multiple narrow sections — flow rate is the same throughout, but pressure drops at each narrow section (adds up to total pump pressure).
- **Parallel**: Like water splitting into two pipes from the same tank — each pipe has the same pressure across it, but the flow divides between them.

---

### Water Waves in Shallow Water
- **Wave Speed**: Water waves slow down as they enter shallower water.
    - Speed is dependent on depth (shallower = slower).
- **Wavelength**: As the speed decreases, the wavelength ($\lambda$) also decreases.
    - The waves "bunch up" together.
- **Frequency**: The frequency ($f$) of the waves remains **constant**.
    - Frequency is determined by the source of the wave, not the medium.
- **Wave Equation**: $v = f \lambda$
    - Since $v$ decreases and $f$ is constant, $\lambda$ must decrease.
- **Refraction**: This change in speed causes the waves to change direction (bend), a phenomenon known as refraction.
    - Waves tend to bend towards the normal (if entering a slower medium at an angle), or in the case of shorelines, refract to become parallel to the shore.

### Sound
- **Nature of Sound Waves**: Sound waves are **longitudinal waves** created by vibrating objects.
    - They consist of **compressions** (high pressure) and **rarefactions** (low pressure).
    - Sound requires a medium to travel (cannot travel through a vacuum).
- **Frequency and Pitch**: The pitch of a sound depends on its frequency.
    - **High Frequency** = High Pitch.
    - **Low Frequency** = Low Pitch.
    - Measured in **Hertz (Hz)**.
- **Amplitude and Loudness**: The loudness depends on the amplitude of the wave.
    - **Large Amplitude** = Loud Sound (more energy).
    - **Small Amplitude** = Quiet Sound.
- **Speed of Sound**: Speed varies with the medium.
    - Fastest in solids, then liquids, slowest in gases (~340 m/s in air).
    - Equation: $v = f \lambda$
- **Reflection (Echoes)**: Sound waves define reflection as bouncing off hard surfaces.
    - An **echo** is a reflected sound wave.
- **Hearing Range**: Humans can hear frequencies between **20 Hz and 20,000 Hz**.
- **Ultrasound**: Sound with frequencies **above 20,000 Hz**.
    - Used for medical scans (prenatal) and sonar.
