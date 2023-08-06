# -*- coding: utf-8 -*-
# Copyright (c) 2022, KarjaKAK
# All rights reserved.

import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk
)
from matplotlib.figure import Figure
from dataclasses import dataclass
from types import MappingProxyType as mpt


__all__ = ["Charts"]


@dataclass(frozen=True, slots=True)
class Charts:
    """Creating charts for data given"""

    data: dict
    name: str

    def __post_init__(self):

        super(Charts, self).__setattr__("data", mpt(self.data))
        super(Charts, self).__setattr__("name", self.name)

    def pchart(self, root):
        root.title(self.name)
        root.attributes('-topmost',True)
        frameChartsLT = tk.Frame(root)
        frameChartsLT.pack(fill = tk.BOTH, expand = 1)
        fig = Figure()
        wedge_properties = {"edgecolor": "k",'linewidth': 1, 'width': 0.3}
        explode = [0.05 for _  in range(len(self.data))]

        ax = fig.add_subplot()

        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = pct*total/100.0
                return f"{pct:.2f}%\n{val:,.2f}"
            return my_autopct

        ax.pie(
            self.data.values(), 
            radius=1.3, 
            explode=explode, 
            labels=self.data.keys(), 
            autopct=make_autopct(self.data.values()), 
            shadow=False, 
            wedgeprops = wedge_properties,
        )

        chart1 = FigureCanvasTkAgg(fig,frameChartsLT)
        NavigationToolbar2Tk(chart1, frameChartsLT)
        chart1.get_tk_widget().pack(fill = tk.BOTH, expand = 1)
        tx = f"TOTAL {self.name.upper()}: {sum(self.data.values()):,.2f}"
        lab = tk.Label(frameChartsLT, text=tx, justify=tk.CENTER, bg="white", font="verdana 20 bold", fg = "black")
        lab.pack(fill=tk.BOTH, expand=1, ipady=2)
