# -*- coding: utf-8 -*-
"""
/***************************************************************************
 UPrepEdit2R
                                 A QGIS plugin
 File Editor for Prepair to R
                             -------------------
        begin                : 2016-08-22
        copyright            : (C) 2016 by Toshio Yamazaki / UPCS
        email                : lisa9500jp@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load UPrepEdit2R class from file UPrepEdit2R.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .uprep_edit_2r import UPrepEdit2R
    return UPrepEdit2R(iface)
