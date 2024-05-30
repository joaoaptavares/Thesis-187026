import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams
from buttons import *

rcParams["figure.figsize"] = (16,6)

typedata = {"object": "bar", "float64": "bar", "category": "bar", "int64": "bar"}


def show_table(d, desc="", mvalue=(), disp=True, bins=False, nbins='auto', int_check=False, int_var= "", int_value=[]):

    global selected_output
    output_options = {selected_output[0]: 'sum', selected_output[1]: 'sum'}

    if len(mvalue) != 0:
        df1 = df[df[desc].isin(mvalue)]
        if isinstance(d, str):
            title = "##### Feature: " + d + " for " + desc + "=" + str(mvalue)
        elif isinstance(d, list):
            title = str("##### Feature: " + d[0] + " + " + d[1] + " for " + desc + "=" + str(mvalue))
    else:
        df1 = df
        if isinstance(d, str):
            title = str("##### Feature: " + d)
        elif isinstance(d, list):
            title = str("##### Feature: " + d[0] + " + " + d[1])

    if int_check:
        df1 = df1[df1[int_var] >= int_value[0]]
        df1 = df1[df1[int_var] <= int_value[1]]

    if bins and isinstance(d, str):
        if str(df1[d].dtype) in ['float64', 'int64']:
            df1 = df1.groupby(d, as_index=False).agg(output_options)
            if nbins == "auto":
                nbins = max(3,round(len(df1.index)/4))
            df1[d] = pd.cut(df1[d], bins=nbins)
        df2 = df1.groupby(d, as_index=False).agg(output_options)
    elif bins and isinstance(d, list):
        dft = []
        for i in d:
            dft.append(str(df1[i].dtype))

        df1 = df1.groupby(d, as_index=False).agg(output_options)

        for idx, val in enumerate(dft):
            df3 = df1
            if val in ['float64', 'int64']:
                if nbins == "auto":
                    nbins = max(3,round(len(df1.index)/4))
                df1[d[idx]] = pd.cut(df3[d[idx]], bins=nbins)

        df2 = df1.groupby(by=d, as_index=False, observed=True).agg(output_options)
    else:
        df2 = df1.groupby(by=d, as_index=False).agg(output_options)


    df2["percentage"] = df2[selected_output[0]]/df2[selected_output[1]]*100

    if disp:
        display(Markdown("---"))
        display(Markdown(title))
        display(df2)

    return df2


def show_graphic1D(df1, d, output, desc, mvalue):
    dft = str(df1[d].dtype)
    display(Markdown("---"))

    if len(mvalue) != 0:
        title = "Feature: " + d + " for " + desc + "=" + str(mvalue)
    else:
        title = str("Feature: " + d)

    sel_output = []
    for i in range(0, len(output)):
            if output[i].value == True:
                sel_output.append(str(output[i].description))
    sel_output = ["out_defects", "percentage"]

    print(dft)
    print(sel_output)
    if dft == "object":
        if len(sel_output) == 1:
            ax = df1.plot(x=d, y=sel_output[0], title=title, kind=typedata[dft], color="tab:blue")
        elif len(sel_output) == 2:
            ax = df1.plot(x=d, y=sel_output[0], title=title, kind=typedata[dft], width=-0.3, color="tab:orange", align='edge')
            ax1 = ax.twinx()
            df1.plot(ax=ax1, x=d, y=sel_output[1], kind=typedata[dft], width=0.3, color="tab:blue", align='edge')
    elif dft in ["float64", "int64", "category"]:
        if len(sel_output) == 1:
            ax = df1.plot(x=d, y=sel_output[0], title=title, kind=typedata[dft], style="o-", color="tab:blue")
        elif len(sel_output) == 2:
            ax = df1.plot(x=d, y=sel_output[0], title=title, kind=typedata[dft], style="o-", width=-0.3, color="tab:orange", align='edge')
            ax1 = ax.twinx()
            df1.plot(ax=ax1, x=d, y=sel_output[1], kind=typedata[dft], style="o--", width=0.3, color="tab:blue", align='edge')

    ax.set_xlabel(str('Feature: ' + d))
    ax.figure.autofmt_xdate(rotation=45)
    ax.legend(loc="upper left")
    ax.set_ylabel(str('Output: ' + sel_output[0]))
    if len(sel_output) == 2:
        ax1.set_ylabel(str('Output: ' + sel_output[1]))

    # save the figure
    results_dir = 'Results/'
    plt.savefig(results_dir + str('plot-1D-' + d + '.png'))

    plt.show()



def show_graphic2D(df1, d, output):
    dft = []
    print("Output: ", output)
    for i in d:
        dft.append(str(df1[i].dtype))

    display(Markdown("---"))
    fig = plt.figure(figsize=(16, 12))
    if all(x == "float64" for x in dft):
        rcParams["figure.figsize"] = (16,6)
        pivot = df1.pivot(d[0], d[1], output)
        sns.heatmap(data=pivot, annot=True, cmap="YlGnBu")
#         sns.relplot(data=df1, x=d[0], y=d[1], hue=output[0], size=output[0], sizes=(100,700))
    elif not all(x != "float64" for x in dft):
        pivot = df1.pivot(d[0], d[1], output)
        sns.heatmap(data=pivot, annot=True, cmap="YlGnBu")
    elif all(x != "float64" for x in dft):
        pivot = df1.pivot(d[0], d[1], output)
        sns.heatmap(data=pivot, annot=True, cmap="YlGnBu")

    # save the figure
    results_dir = 'Results/'
    plt.savefig(results_dir + str('plot-2D-' + d[0] + '.png'))
    plt.show()
