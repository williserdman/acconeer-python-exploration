# Copyright (c) Acconeer AB, 2023
# All rights reserved

from __future__ import annotations

from copy import copy
from typing import List, Optional

from PySide6.QtWidgets import (
    QButtonGroup,
    QFrame,
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

import pyqtgraph as pg

from acconeer.exptool.app.new.ui.utils import LayoutWrapper, LeftAlignDecorator


class TabPGWidget(QFrame):
    """
    Custom tab widget to handle GraphicsLayoutWidget.
    Since QTabWidget and GraphicsLayoutWidget caused GUI to freeze.
    """

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent=parent)

        self._button_group = QButtonGroup()
        self._button_layout = QHBoxLayout()
        self._button_layout.setContentsMargins(0, 0, 0, 0)

        self._main_layout = QVBoxLayout()
        button_wrapper = LeftAlignDecorator(LayoutWrapper(self._button_layout))
        self._main_layout.addWidget(button_wrapper)

        self._plot_widgets: List[pg.GrachicsLayoutWidget] = []

        self.setLayout(self._main_layout)

    def newPlotWidget(self, title: str) -> pg.GraphicsLayoutWidget:
        new_tab_id = len(self._button_group.buttons())
        plot_widget = pg.GraphicsLayoutWidget()
        plot_widget.setVisible(new_tab_id == 0)
        self._plot_widgets.append(plot_widget)
        self._main_layout.addWidget(plot_widget)

        button = QPushButton(title, self)
        button.setCheckable(True)
        button.setChecked(new_tab_id == 0)
        button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self._button_group.addButton(button, id=len(self._button_group.buttons()))
        self._button_group.idToggled.connect(
            lambda button_id, checked: plot_widget.setVisible(button_id == new_tab_id and checked)
        )
        self._button_layout.addWidget(button)

        return plot_widget

    def clear(self) -> None:
        try:
            self._button_group.idToggled.disconnect()
        except RuntimeError:
            pass

        for plot_widget in self._plot_widgets:
            self._main_layout.removeWidget(plot_widget)
            plot_widget.deleteLater()

        self._plot_widgets = []

        for button in copy(self._button_group.buttons()):
            self._button_group.removeButton(button)
            self._button_layout.removeWidget(button)
            button.deleteLater()
