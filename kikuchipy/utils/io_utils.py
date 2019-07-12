# -*- coding: utf-8 -*-
# Copyright 2019 The KikuchiPy developers
#
# This file is part of KikuchiPy.
#
# KikuchiPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# KikuchiPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with KikuchiPy. If not, see <http://www.gnu.org/licenses/>.

import logging
from hyperspy.misc.utils import DictionaryTreeBrowser

_logger = logging.getLogger(__name__)


def kikuchipy_metadata():
    """Return a dictionary in HyperSpy's DictionaryTreeBrowser format
    with the default KikuchiPy metadata.

    See :func:`kikuchipy.signals.EBSD.set_experimental_parameters` for
    an explanation of the parameters.

    Returns
    -------
    md : DictionaryTreeBrowser
    """
    md = DictionaryTreeBrowser()
    sem_node, ebsd_node = metadata_nodes()
    ebsd = {'azimuth_angle': -1, 'binning': -1, 'detector': '',
            'detector_pixel_size': -1, 'elevation_angle': -1,
            'exposure_time': -1, 'frame_number': -1, 'frame_rate': -1,
            'gain': -1, 'grid_type': '', 'manufacturer': '', 'n_columns': -1,
            'n_rows': -1, 'pattern_height': -1, 'pattern_width': -1,
            'sample_tilt': -1, 'scan_time': -1, 'step_x': -1, 'step_y': -1,
            'static_background': -1, 'version': '', 'xpc': -1, 'ypc': -1,
            'zpc': -1}
    sem = {'microscope': '', 'magnification': -1, 'beam_energy': -1,
           'working_distance': -1}
    md.set_item(sem_node, sem)
    md.set_item(ebsd_node, ebsd)
    return md


def get_input_bool(question):
    """Get input from user on boolean choice, returning the answer.

    Parameters
    ----------
    question : str
        Question to ask user.
    """
    try:
        answer = input(question)
        answer = answer.lower()
        while (answer != 'y') and (answer != 'n'):
            print("Please answer y or n.")
            answer = input(question)
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
    except BaseException:
        # Running in an IPython notebook that does not support raw_input
        _logger.info("Your terminal does not support raw input. Not adding "
                     "scan. To add the scan use `add_scan=True`")
        return False
    else:
        return True


def get_input_variable(question, var_type):
    """Get variable input from user, returning the variable.

    Parameters
    ----------
    question : str
        Question to ask user.
    var_type : type
        Type of variable to return.
    """
    try:
        answer = input(question)
        while type(answer) != var_type:
            print("Please enter a variable of type {}:\n".format(var_type))
            answer = input(question)
        return answer
    except BaseException:
        # Running in an IPython notebook that does not support raw_input
        _logger.info("Your terminal does not support raw input. Not adding "
                     "scan. To add the scan use `add_scan=True`")
        return None


def metadata_nodes(sem=True, ebsd=True):
    """Return SEM and EBSD metadata nodes.

    This is a convenience function so that we only have to define these
    node strings here.

    Parameters
    ----------
    sem, ebsd : bool, optional
        Whether to return the node string (default is True).

    Returns
    -------
    sem_node, ebsd_node : str
    """
    sem_node = 'Acquisition_instrument.SEM'
    ebsd_node = sem_node + '.Detector.EBSD'
    if sem and ebsd:
        return sem_node, ebsd_node
    elif sem:
        return sem_node
    elif ebsd:
        return ebsd_node


