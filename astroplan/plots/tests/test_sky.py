# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import pytest

try:
    import matplotlib  # noqa
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


# TODO: replace this with actual plot checks once these
# issues are resolved:
# https://github.com/astropy/astroplan/issues/65
# https://github.com/astropy/astroplan/issues/74
@pytest.mark.skipif('not HAS_MATPLOTLIB')
@pytest.mark.mpl_image_compare
def test_image_example():
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot([1, 2, 3])
    return fig


@pytest.mark.skipif('not HAS_MATPLOTLIB')
@pytest.mark.mpl_image_compare
def test_timezone():
    import matplotlib.pyplot as plt
    from astropy import coordinates
    from astropy import units as u
    from ..time_dependent import plot_airmass
    from ... import Observer
    import datetime
    import pytz

    bg = coordinates.SkyCoord.from_name('Betelgeuse')
    vla = Observer(coordinates.EarthLocation.of_site('VLA'))
    now_ET = pytz.timezone('US/Eastern').localize(datetime.datetime.now())

    plot_airmass(bg, vla, now_ET, use_local_tz=True)
