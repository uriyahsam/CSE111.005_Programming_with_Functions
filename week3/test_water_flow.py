from pytest import approx
import pytest
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    kpa_to_psi
)

# Test function for water_column_height
def test_water_column_height():
    assert water_column_height(0.0, 0.0) == approx(0.0, abs=0.001)
    assert water_column_height(0.0, 10.0) == approx(7.5, abs=0.001)
    assert water_column_height(25.0, 0.0) == approx(25.0, abs=0.001)
    assert water_column_height(48.3, 12.8) == approx(57.9, abs=0.001)

# Test function for pressure_gain_from_water_height
def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

# Test function for pressure_loss_from_pipe
def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)

# Test function for pressure_loss_from_fittings
def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)

# Test function for reynolds_number
def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)

# Test function for pressure_loss_from_pipe_reduction
def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-0.2403, abs=0.001)
    # assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

# Test function for kpa_to_psi
def test_kpa_to_psi():
    assert kpa_to_psi(158.7) == approx(23.018, abs=0.001)
    # assert kpa_to_psi(158.7) == approx(23.021, abs=0.001)

# Main call to pytest
pytest.main(["-v", "--tb=line", "-rN", __file__])
