from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np


class DynamicPlotter:
    def __init__(self):
        self.tic = None
        self.tvc = None
        self.effort = None
        self.figs = []
        self.axes = []
        self.n_sups = None
        self.n_cols = None
        self.n_ti = None
        self.n_tv = None
        self.ti_xlim = None
        self.ti_ylim = None
        self.tv_xlim = None
        self.tv_ylim = None
        self.width_ratios = None
        self.ti_xticks = None
        self.ti_xticklabels = None
        self.ti_yticks = None
        self.ti_yticklabels = None
        self.tv_xticks = None
        self.tv_xticklabels = None
        self.tv_yticks = None
        self.tv_yticklabels = None
        self.ti_names = None
        self.tv_names = None
        self.fig_title = None
        self.fig_size = None

    def determine_n_sups(self):
        self.n_sups = self.effort.shape[0]

    def determine_n_cols(self):
        self.n_ti = self.tic.shape[1]
        self.n_tv = self.tvc.shape[1]
        self.n_cols = self.n_ti + self.n_tv
        self.n_cols += 1

    def determine_n_ti_n_tv(self):
        self.n_ti = self.tic.shape[1]
        self.n_tv = self.tvc.shape[1]

    def plot(self):
        self.determine_n_sups()
        self.determine_n_cols()

        fig = plt.figure(figsize=self.fig_size)
        fig.suptitle(self.fig_title)
        if self.n_cols < 10:
            axes_pos = self.n_sups * 100 + self.n_cols * 10
        else:
            raise NotImplementedError(
                "Total number of variables (Time-invariant and varying) cannot exceed 10."
            )
        gs = GridSpec(
            self.n_sups,
            self.n_cols,
            figure=fig,
            width_ratios=self.width_ratios,
        )

        for i in range(self.n_sups):
            self.axes.append([])
            for j in range(self.n_cols):
                self.axes[i].append(fig.add_subplot(gs[i, j]))
        self.axes = np.array(self.axes)

        # add variable names
        for j in range(self.n_cols):
            if j < self.n_ti:
                self.axes[0, j].set_title(self.ti_names[j])
            elif self.n_ti <= j < self.n_ti + self.n_tv:
                self.axes[0, j].set_title(self.tv_names[j - self.n_ti])
            else:
                self.axes[0, j].set_title("Efforts")

        for i, (tic, tvc) in enumerate(zip(self.tic, self.tvc)):
            # TIC
            for j_ti, ti in enumerate(tic):
                self.axes[i, j_ti].plot(
                    [0, 1],
                    [ti, ti],
                )
            # TVC
            for j_tv, tv in enumerate(tvc):
                sorted_time = np.sort(list(tv.keys()))
                second_smallest_time = sorted_time[1]
                largest_time = sorted_time[-1]
                for time, val in tv.items():
                    if time == 0:
                        self.axes[i, self.n_ti + j_tv].axvline(
                            x=0,
                            ymin=0,
                            ymax=1,
                            ls=":",
                            c="black",
                            alpha=0.50,
                        )
                        self.axes[i, self.n_ti + j_tv].plot(
                            [0.0, second_smallest_time],
                            [val, val]
                        )
                    elif time == largest_time:
                        self.axes[i, self.n_ti + j_tv].axvline(
                            x=1,
                            ymin=0,
                            ymax=1,
                            ls=":",
                            c="black",
                            alpha=0.50,
                        )
                        self.axes[i, self.n_ti + j_tv].plot(
                            [time, 1.0],
                            [val, val]
                        )
                        self.axes[i, self.n_ti + j_tv].axvline(
                            x=time,
                            ymin=0,
                            ymax=1,
                            ls=":",
                            c="black",
                            alpha=0.50,
                        )
                    else:
                        self.axes[i, self.n_ti + j_tv].axvline(
                            x=time,
                            ymin=0,
                            ymax=1,
                            ls=":",
                            c="black",
                            alpha=0.50,
                        )
                        curr_time_idx = int(np.squeeze(np.argwhere(sorted_time == time)))
                        next_time = sorted_time[curr_time_idx + 1]
                        self.axes[i, self.n_ti + j_tv].plot(
                            [time, next_time],
                            [val, val],
                        )

            # effort
            self.axes[i, self.n_ti + self.n_tv].annotate(
                text=f"{effort[i] * 100:.2f}%",
                xy=(0.10, 0.10 + 0.45),
            )
        for i, ax in enumerate(self.axes):
            for j, a in enumerate(ax):
                if j < self.n_ti:
                    a.set_xlim(self.ti_xlim[j])
                    a.set_ylim(self.ti_ylim[j])
                    a.get_xaxis().set_ticks(self.ti_xticks[j])
                    a.get_yaxis().set_ticks(self.ti_yticks[j])
                    a.get_xaxis().set_ticklabels(self.ti_xticklabels[j])
                    a.get_yaxis().set_ticklabels(self.ti_yticklabels[j])

                elif self.n_ti <= j < self.n_ti + self.n_tv:
                    a.set_xlim(self.tv_xlim[j - self.n_ti])
                    a.set_ylim(self.tv_ylim[j - self.n_ti])
                    a.get_xaxis().set_ticks(self.tv_xticks[j - self.n_ti])
                    a.get_yaxis().set_ticks(self.tv_yticks[j - self.n_ti])
                    a.get_xaxis().set_ticklabels(self.tv_xticklabels[j - self.n_ti])
                    a.get_yaxis().set_ticklabels(self.tv_yticklabels[j - self.n_ti])
                else:
                    a.set_xlim([0, 1])
                    a.set_ylim([0, 1])
                    a.set_axis_off()
        fig.tight_layout()
        self.figs.append(fig)
        return fig


if __name__ == '__main__':
    import numpy as np
    dyn_plotter = DynamicPlotter()

    """ Plotting options """
    dyn_plotter.width_ratios = [1, 4, 0.25]
    dyn_plotter.ti_xlim = np.array([
        [-0.1, 1.1],
    ])
    dyn_plotter.tv_xlim = np.array([
        [-0.02, 1.02],
    ])
    dyn_plotter.ti_xticks = [
        [],
    ]
    dyn_plotter.ti_xticklabels = [
        [],
    ]
    dyn_plotter.ti_yticks = [
        [65 + 273.15, 70 + 273.15, 75 + 273.15],
    ]
    dyn_plotter.ti_yticklabels = [
        [65+273.15, 70+273.15, 75+273.15],
    ]
    dyn_plotter.tv_xticks = [
        [],
    ]

    dyn_plotter.tv_xticklabels = [
        [],
    ]
    dyn_plotter.ti_names = [
        "$T$ (K)",
    ]
    dyn_plotter.tv_names = [
        r"$u(t) \times 10^{5}$ (L/s)",
    ]

    """ Experimental Campaign Description """
    # TEST 1
    if False:
        exp_name = "fbr_cvar_optimal"
        effort = np.array([
            0.271,
            0.263,
            0.246,
            0.163,
            0.057,
        ])
        tic = np.array([
            [
                65+273.15,
                75+273.15,
                75+273.15,
                65+273.15,
                65+273.15,
            ],
        ]).T
        tvc = np.array([[
        {
            0: 1,
            0.25: 1,
            0.50: 0.70,
            0.75: 0.70,
        },
        {
            0: 1,
            0.25: 1,
            0.50: 0.70,
            0.75: 0.70,
        },
        {
            0: 1,
            0.25: 0,
            0.50: 0,
            0.75: 0,
        },
        {
            0: 1,
            0.25: 0,
            0.50: 0,
            0.75: 0,
        },
        {
            0: 0,
            0.25: 0,
            0.50: 0,
            0.75: 0,
        },
    ]]).T
        dyn_plotter.ti_ylim = np.array([
            [64+273.15, 76+273.15],
        ])
        dyn_plotter.tv_ylim = np.array([
            [-0.1, 1.1],
        ])
        dyn_plotter.tv_yticks = [
            [0, 0.50, 1.00],
        ]
        dyn_plotter.tv_yticklabels = [
            [0, 0.75, 1.50],
        ]
    # TEST 2
    if False:
        exp_name = "test_experiment_2"
        dyn_plotter.fig_size = (10, 5)
        dyn_plotter.width_ratios = [1, 1, 4, 4, 0.25]
        dyn_plotter.ti_names = [
            "$x_1$",
            "$x_2$",
        ]
        dyn_plotter.tv_names = [
            r"$u_1(t)$",
            r"$u_2(t)$",
        ]
        effort = np.array([
            0.271,
            0.263,
            0.246,
            0.163,
            0.057,
        ])
        tic = np.array([
            [65 + 273.15, 65 + 273.15],
            [75 + 273.15, 75 + 273.15],
            [75 + 273.15, 75 + 273.15],
            [65 + 273.15, 65 + 273.15],
            [65 + 273.15, 65 + 273.15],
        ])
        tvc = np.array([
            [
                {
                    0: 1,
                    0.25: 1,
                    0.50: 0.70,
                    0.75: 0.70,
                },
                {
                    0: 1,
                    0.25: 1,
                    0.50: 0.70,
                    0.75: 0.70,
                },
                {
                    0: 1,
                    0.25: 0,
                    0.50: 0,
                    0.75: 0,
                },
                {
                    0: 1,
                    0.25: 0,
                    0.50: 0,
                    0.75: 0,
                },
                {
                    0: 0,
                    0.25: 0,
                    0.50: 0,
                    0.75: 0,
                },
            ],
            [
                {
                    0: 1,
                    0.25: 1,
                    0.50: 0.70,
                    0.75: 0.70,
                },
                {
                    0: 1,
                    0.25: 1,
                    0.50: 0.70,
                    0.75: 0.70,
                },
                {
                    0: 1,
                    0.25: 0,
                    0.50: 0,
                    0.75: 0,
                },
                {
                    0: 1,
                    0.25: 0,
                    0.50: 0,
                    0.75: 0,
                },
                {
                    0: 0,
                    0.25: 0,
                    0.50: 0,
                    0.75: 0,
                },
            ]
        ]).T
        dyn_plotter.ti_ylim = np.array([
            [64 + 273.15, 76 + 273.15],
            [64 + 273.15, 76 + 273.15],
        ])
        dyn_plotter.tv_ylim = np.array([
            [-0.1, 1.1],
            [-0.1, 1.1],
        ])
        dyn_plotter.tv_yticks = [
            [0, 0.50, 1.00],
            [0, 0.50, 1.00],
        ]
        dyn_plotter.tv_yticklabels = [
            [0, 0.75, 1.50],
            [0, 0.75, 1.50],
        ]
        dyn_plotter.ti_xlim = np.array([
            [-0.1, 1.1],
            [-0.1, 1.1],
        ])

        dyn_plotter.tv_xlim = np.array([
            [-0.02, 1.02],
            [-0.02, 1.02],
        ])

        dyn_plotter.ti_xticks = [
            [],
            [],
        ]
        dyn_plotter.ti_xticklabels = [
            [],
            [],
        ]
        dyn_plotter.ti_yticks = [
            [65 + 273.15, 70 + 273.15, 75 + 273.15],
            [65 + 273.15, 70 + 273.15, 75 + 273.15],
        ]
        dyn_plotter.ti_yticklabels = [
            [65, 70, 75],
            [65, 70, 75],
        ]
        dyn_plotter.tv_xticks = [
            [],
            [],
        ]

        dyn_plotter.tv_xticklabels = [
            [],
            [],
        ]
    # Test 3: random experimental campaign
    if False:
        n_sup = np.random.randint(2, 10, 1)[0]
        n_ti = np.random.randint(2, 4, 1)[0]
        n_tv = np.random.randint(2, 4, 1)[0]
        n_tv_pieces = np.random.randint(2, 10, (n_sup, n_tv))

        exp_name = f"Test_3_{n_sup}_sup_{n_ti}_ti_{n_tv}_tv"

        effort = np.random.uniform(0, 1, n_sup)
        effort = effort / np.sum(effort)

        tic = np.random.uniform(-1, 1, (n_sup, n_ti))
        tvc = np.array([
            [
                {key: np.random.uniform(-1, 1, 1)[0] for key in np.linspace(0, 1, n_tv_pieces[sup, tv], endpoint=False)}
                for sup in range(n_sup)
            ] for tv in range(n_tv)
        ]).T

        """ Optional Attributes """
        dyn_plotter.fig_size = (10, 5)
        dyn_plotter.width_ratios = []
        dyn_plotter.width_ratios.extend([1 for ti in range(n_ti)])
        dyn_plotter.width_ratios.extend([4 for ti in range(n_tv)])
        dyn_plotter.width_ratios.extend([0.25])
        dyn_plotter.ti_names = [f"$x_{ti}$" for ti in range(n_ti)]
        dyn_plotter.tv_names = [rf"$u_{tv}(t)$" for tv in range(n_tv)]
        dyn_plotter.ti_xlim = np.array([
            [-0.1, 1.1] for ti in range(n_ti)
        ])
        dyn_plotter.tv_xlim = np.array([
            [-0.1, 1.1] for tv in range(n_tv)
        ])
        dyn_plotter.ti_ylim = np.array([
            [-1.1, 1.1] for ti in range(n_ti)
        ])
        dyn_plotter.tv_ylim = np.array([
            [-1.1, 1.1] for tv in range(n_tv)
        ])
        dyn_plotter.tv_yticks = [
            [-1.0, 0.00, 1.00] for tv in range(n_tv)
        ]
        dyn_plotter.tv_yticklabels = [
            [-1.0, 0.0, 1.0] for tv in range(n_tv)
        ]
        dyn_plotter.ti_xticks = [
            [] for ti in range(n_ti)
        ]
        dyn_plotter.ti_xticklabels = [
            [] for ti in range(n_ti)
        ]
        dyn_plotter.ti_yticks = [
            [-1.0, 0.0, 1.0] for ti in range(n_ti)
        ]
        dyn_plotter.ti_yticklabels = [
            [-1.0, 0.0, 1.0] for ti in range(n_ti)
        ]
        dyn_plotter.tv_xticks = [
            [] for tv in range(n_tv)
        ]
        dyn_plotter.tv_xticklabels = [
            [] for tv in range(n_tv)
        ]
    # RESTRICTED PB 2729168
    if False:
        exp_name = "Restricted Maximal Average"
        criterion = "d_opt_criterion"
        criterion_value = 2.8229196318734426
        effort = np.array([
            0.4487,
            0.0500,
            0.0715,
            0.3128,
            0.1169,
        ])
        tic = np.array([
            [
                347.67,
                348.14,
                339.33,
                338.34,
                347.85,
            ],
        ]).T
        tvc = np.array([[
            {
                0.00:   12.28/10,
                0.25:    9.11/10,
                0.50:    5.41/10,
                0.75:    6.63/10,
            },
            {
                0.00:   11.89/10,
                0.25:    0.69/10,
                0.50:    1.87/10,
                0.75:   10.40/10,
            },
            {
                0.00:    5.54/10,
                0.25:    0.72/10,
                0.50:    2.59/10,
                0.75:    6.94/10,
            },
            {
                0.00:   11.56/10,
                0.25:    6.32/10,
                0.50:    2.71/10,
                0.75:    1.56/10,
            },
            {
                0.00:   12.44/10,
                0.25:    1.87/10,
                0.50:    0.88/10,
                0.75:    1.68/10,
            },
        ]]).T
        dyn_plotter.ti_ylim = np.array([
            [64+273.15, 76+273.15],
        ])
        dyn_plotter.tv_ylim = np.array([
            [-0.3/10, 13.3/10],
        ])
        dyn_plotter.tv_yticks = [
            [0, 6.5/10, 13/10],
        ]
        dyn_plotter.tv_yticklabels = [
            [0, 6.5/10, 13/10],
        ]
    # RESTRICTED PB 2729145
    if False:
        exp_name = "restricted_pb_2729145"
        effort = np.array([
            0.3203,
            0.4401,
            0.0074,
            0.1638,
            0.0684,
        ])
        tic = np.array([
            [
                338.91,
                347.87,
                338.41,
                348.10,
                338.34,
            ],
        ]).T
        tvc = np.array([[
            {
                0.00:    7.00,
                0.25:    8.78,
                0.50:    5.73,
                0.75:    4.37,
            },
            {
                0.00:   12.59,
                0.25:    7.69,
                0.50:    8.00,
                0.75:    3.29,
            },
            {
                0.00:   12.00,
                0.25:    0.05,
                0.50:    1.75,
                0.75:    2.52,
            },
            {
                0.00:   12.68,
                0.25:    1.15,
                0.50:    2.35,
                0.75:    5.67,
            },
            {
                0.00:    4.70,
                0.25:    3.55,
                0.50:    2.55,
                0.75:    1.32,
            },
        ]]).T
        dyn_plotter.ti_ylim = np.array([
            [64 + 273.15, 76 + 273.15],
        ])
        dyn_plotter.tv_ylim = np.array([
            [-0.3, 13.3],
        ])
        dyn_plotter.tv_yticks = [
            [0, 6.50, 13.00],
        ]
        dyn_plotter.tv_yticklabels = [
            [0, 6.50, 13.00],
        ]
    # RESTRICTED LOCAL 2729213
    if True:
        exp_name = "Restricted Local"
        effort = np.array([
            0.4827,
            0.0507,
            0.3035,
            0.1356,
            0.0274,
        ])
        tic = np.array([
            [
                347.67,
                348.14,
                338.34,
                340.21,
                347.85,
            ],
        ]).T
        tvc = np.array([[
            {
                0.00:   12.28/10,
                0.25:    9.11/10,
                0.50:    5.41/10,
                0.75:    6.63/10,
            },
            {
                0.00:   11.89/10,
                0.25:    0.07/10,
                0.50:    1.87/10,
                0.75:   10.40/10,
            },
            {
                0.00:   11.56/10,
                0.25:    6.32/10,
                0.50:    2.71/10,
                0.75:    1.56/10,
            },
            {
                0.00:    4.54/10,
                0.25:    1.50/10,
                0.50:    3.77/10,
                0.75:    1.43/10,
            },
            {
                0.00:   12.44/10,
                0.25:    1.87/10,
                0.50:    0.88/10,
                0.75:    1.68/10,
            },
        ]]).T
        dyn_plotter.ti_ylim = np.array([
            [64 + 273.15, 76 + 273.15],
        ])
        dyn_plotter.tv_ylim = np.array([
            [-0.3/10, 13.3/10],
        ])
        dyn_plotter.tv_yticks = [
            [0, 6.50/10, 13.00/10],
        ]
        dyn_plotter.tv_yticklabels = [
            [0, 6.50/10, 13.00/10],
        ]
    # UNRESTRICTED LOCAL 2729211
    if False:
        exp_name = "unrestricted_local_2729211"
        effort = np.array([
            0.1679,
            0.3417,
            0.1498,
            0.3406,
        ])
        tic = np.array([
            [
                338.15,
                338.15,
                348.15,
                348.15,
            ],
        ]).T
        tvc = np.array([[
            {
                0.00:   18.67,
                0.25:    0.00,
                0.50:    0.00,
                0.75:    9.33,
            },
            {
                0.00:   28.00,
                0.25:   28.00,
                0.50:   28.00,
                0.75:   28.00,
            },
            {
                0.00: 28.00,
                0.25:  0.00,
                0.50:  9.33,
                0.75:  0.00,
            },
            {
                0.00: 28.00,
                0.25: 28.00,
                0.50:  0.00,
                0.75:  0.00,
            },
        ]]).T
        dyn_plotter.ti_ylim = np.array([
            [64 + 273.15, 76 + 273.15],
        ])
        dyn_plotter.tv_ylim = np.array([
            [-0.5, 28.5],
        ])
        dyn_plotter.tv_yticks = [
            np.linspace(0, 28, 4),
        ]
        dyn_plotter.tv_yticklabels = [
            np.round(np.linspace(0, 28, 4), decimals=1),
        ]
    # UNRESTRICTED LOCAL 2729212
    if False:
        exp_name = "Unrestricted Local"
        effort = np.array([
            0.1672,
            0.0025,
            0.3392,
            0.1502,
            0.3409,
        ])
        tic = np.array([
            [
                338.15,
                338.15,
                338.15,
                348.15,
                348.15,
            ],
        ]).T
        tvc = np.array([[
            {
                0.00: 18.67,
                0.25: 0.00,
                0.50: 0.00,
                0.75: 9.33,
            },
            {
                0.00: 28.00,
                0.25: 28.00,
                0.50: 28.00,
                0.75: 18.67,
            },
            {
                0.00: 28.00,
                0.25: 28.00,
                0.50: 28.00,
                0.75: 28.00,
            },
            {
                0.00: 28.00,
                0.25: 0.00,
                0.50: 9.33,
                0.75: 0.00,
            },
            {
                0.00: 28.00,
                0.25: 28.00,
                0.50:  0.00,
                0.75:  0.00,
            },
        ]]).T
        dyn_plotter.ti_ylim = np.array([
            [64 + 273.15, 76 + 273.15],
        ])
        dyn_plotter.tv_ylim = np.array([
            [-0.5, 28.5],
        ])
        dyn_plotter.tv_yticks = [
            np.linspace(0, 28, 4),
        ]
        dyn_plotter.tv_yticklabels = [
            np.round(np.linspace(0, 28, 4), decimals=1),
        ]

    # pass to plotter
    dyn_plotter.effort = effort
    dyn_plotter.tic = tic
    dyn_plotter.tvc = tvc

    """ Plot Function """
    fig = dyn_plotter.plot()
    # fig.savefig(f"{exp_name}.png", dpi=180)
    plt.show()
