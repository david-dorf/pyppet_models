# pyppet_models
Example models repository for https://github.com/david-dorf/pyppet

## Installation

### pixi
- Install pixi: https://pixi.sh/latest/#installation
- Clone this repository: `git clone https://github.com/david-dorf/pyppet_models.git`
- Navigate to the root of this repository: `cd pyppet_models`
- Run an example: `pixi run move_franka`. Pixi will install dependencies in a virtual environment.

### pip/venv
- Create a virtual environment: `python -m venv venv`
- Activate the virtual environment: `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on Windows)
- Clone this repository: `git clone https://github.com/david-dorf/pyppet_models.git`
- Navigate to the root of this repository: `cd pyppet_models`
- Install dependencies: `pip install .`
- Run an example: `cd pyppet_models/franka_research_3/examples` and then `python3 move_franka.py`
- A similar approach would work for `uv`, a faster alternative to pip
