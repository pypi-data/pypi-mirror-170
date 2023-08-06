zxgraphs: A Python implementation of ZX graphs for quantum computing.
=====================================================================

.. image:: https://img.shields.io/badge/python-3.9+-green.svg
    :target: https://docs.python.org/3.9/
    :alt: Python versions

.. image:: https://img.shields.io/pypi/v/zxgraphs.svg
    :target: https://pypi.python.org/pypi/zxgraphs/
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/status/zxgraphs.svg
    :target: https://pypi.python.org/pypi/zxgraphs/
    :alt: PyPI status

.. image:: http://www.mypy-lang.org/static/mypy_badge.svg
    :target: https://github.com/python/mypy
    :alt: Checked with Mypy
    
.. image:: https://readthedocs.org/projects/zxgraphs/badge/?version=latest
    :target: https://zxgraphs.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://github.com/hashberg-io/zxgraphs/actions/workflows/python-pytest.yml/badge.svg
    :target: https://github.com/hashberg-io/zxgraphs/actions/workflows/python-pytest.yml
    :alt: Python package status

.. image:: https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square
    :target: https://github.com/RichardLitt/standard-readme
    :alt: standard-readme compliant


ZX graphs are a graph-theoretic tool to represent quantum circuits and computations in terms of computational basis (Z basis) and Fourier basis (X basis) tensors (known to us as "spiders") for finite Abelian group algebras.
They are closely related to the original qubit ZX calculus [1]_ [2]_ and recent developments in higher-dimensional variants [3]_ [4]_.

.. [1] Bob Coecke and Ross Duncan, *"Interacting Quantum Observables: Categorical Algebra and Diagrammatics"*, 2009. `arXiv:0906.4725 <https://arxiv.org/abs/0906.4725>`_
.. [2] Aleks Kissinger and John van de Wetering, *"PyZX: Large Scale Automated Diagrammatic Reasoning"*, 2020. `arXiv:1904.04735 <https://arxiv.org/abs/1904.04735>`_, `pyzx on GitHub <https://github.com/Quantomatic/pyzx>`_
.. [3] John van de Wetering and Lia Yeh, *"Phase gadget compilation for diagonal qutrit gates"*, 2022. `arXiv:2204.13681 <https://arxiv.org/abs/2204.13681>`_
.. [4] Robert I. Booth and Titouan Carette, *"Complete ZX-calculi for the stabiliser fragment in odd prime dimensions"*, 2022. `arXiv:2204.12531 <https://arxiv.org/abs/2204.12531>`_

.. contents::


Install
-------


ZX graphs are currently in pre-alpha development.
Once development is complete, you will be able to install the latest release from `PyPI <https://pypi.org/project/zxgraphs/>`_ as follows:

.. code-block:: console

    $ pip install --upgrade zxgraphs


Usage
-----

ZX graphs are currently in pre-alpha development.


API
---


ZX graphs are currently in pre-alpha development. Once development is complete, the full API documentation will be available at https://zxgraphs.readthedocs.io/


Contributing
------------

Please see `<CONTRIBUTING.md>`_.


License
-------

`LGPL (c) Hashberg Ltd. <LICENSE>`_
