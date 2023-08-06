# AiDev

AiDev is a Python library for dealing with structural optimization.

It leverages surrogate modelling in order to speed up optimization when function evaluations are too expensive.

The library is born for a joint usage together with  Finite Element Model (FEM) code but the same workflow 
can easily be applied to any simulation (e.g. CFD).

The library automates:

1. The sampling of the simulation in order to create a dataset to train the surrogate.
2. The surrogate training.
3. The optimization, based on the surrogate model.
4. The post-processing, using Multi-Criteria Decision Making in order to select the best design.

## Installation

AiDev is available on Pypi.

```bash
pip install -U aidev
```

## Usage

Here is illustrated a simple usage for minimizing objective f1 and f2 of a dummy function emulating a FEM wrapper.

The parameters are (*x1*, *x2*).

```python
from aidev.aidev import AiDev
from aidev.utilities.types import Parameter, Target, FeatureDefinition
from aidev.blocks.postprocessing import ScatterPlot

def objective(x, *args):
    f1 = 100 * (x[0] ** 2 + x[1] ** 2)
    f2 = (x[0] - 1) ** 2 + x[1] ** 2
    return [f1, f2]

if __name__ == "__main__":

    x1 = Parameter("x1", "Millimeter", -2, 2)
    x2 = Parameter("x2", "Millimeter", -2, 2)
    f1 = Target("f1", objective=True, weight=0.7)
    f2 = Target("f2", objective=True, weight=0.3)

    parameters = [x1, x2]
    targets = [f1, f2]

    features = FeatureDefinition(parameters, targets)

    ai = AiDev(
        features,
        objective,
        path="",
    )
    ai.surrogate_strategy = 'polynomial'
    ai.degree_fit = 2

    data = ai.run(global_iter=2)

    ScatterPlot(data, pareto_x="f1", pareto_y="f2", save=True, figname="pareto.html")
    print(data)
```

Results is an interactive html image as below:

![pareto](/images/pareto.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU GPLv3 with Commons Clause](https://github.com/radiate-engineering/AiDev/blob/main/LICENSE)