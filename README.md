# pyppet_models
Example models repository for https://github.com/david-dorf/pyppet

<img width="1115" height="571" alt="image" src="https://github.com/user-attachments/assets/a2053c77-41d0-4c6f-8fde-f87595ca502d" />


## Installation

### pixi
- Install pixi: https://pixi.sh/latest/#installation
- Clone this repository, `cd` into it, and run `pixi run move_franka` (or any other example in this repository)

### pip
- `pip install pyppet-models pyppet`
- NOTE: The path definition at the end of the Franka model relies on Pixi, but you can edit the path handling to suit your needs https://github.com/david-dorf/pyppet_models/blob/main/pyppet_models/franka_research_3/model.py
