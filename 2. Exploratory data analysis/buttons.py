class Bttns:

    import ipywidgets as widgets
    from IPython.display import display, clear_output, Markdown

    def __init__(self):
        # creating menu with them
        self.dropdown = self.widgets.Dropdown(options=selected_data, description="Feature: ")
        self.out_dropdown = self.widgets.Dropdown(options=selected_output)

        # button, output, function and linkage
        self.butt1 = self.widgets.Button(description='Table', tooltip='table1D')
        self.butt2 = self.widgets.Button(description='Graphic', tooltip='graphic1D')
        self.filter_butt = self.widgets.Button(description='Filter', icon="filter", tooltip='1D')
        self.options_butt = self.widgets.Button(description='Options', icon="ellipsis-v", tooltip='1D')
        self.output_butt = self.widgets.Button(description='Output', icon="arrow-right", tooltip='1D')
        self.o_options = out_checkboxes
        self.multiple = self.widgets.SelectMultiple()
        self.b_options = list(range(1, 21)) ; self.b_options.append("auto")
        self.nbins = self.widgets.Dropdown(value = "auto", options=self.b_options, description="number of bins")
        self.bins = self.widgets.Checkbox(value=False, description="Bins")
        self.percent = self.widgets.Checkbox(value=False, description="percentage")
        self.vpercent = self.widgets.ToggleButtons(options=["Absolute", "Relative"], description="Percentage")
        self.min_check = self.widgets.Checkbox(value=False, description="Interval of values")
        self.min_value = self.widgets.IntRangeSlider()

        self.outt1 = self.widgets.Output() ; self.outt2 = self.widgets.Output() ; self.outt3 = self.widgets.Output()


        self.butt1.on_click(self.on_butt_clicked1)
        self.butt2.on_click(self.on_butt_clicked2)
        self.output_butt.on_click(self.output_butt_clicked)
        self.filter_butt.on_click(self.filter_butt_clicked)
        self.options_butt.on_click(self.options_butt_clicked)

        self.tab1 = self.widgets.VBox()
        self.tab1_1 = self.widgets.HBox([self.output_butt, self.filter_butt, self.options_butt])
        self.tab1.children = [self.tab1_1, self.widgets.HBox([self.outt2, self.outt3])]

    def output_1D(self):
        # display
        display(self.widgets.VBox([self.dropdown, self.widgets.VBox(children=[self.tab1]),
                    self.widgets.HBox([self.butt1, self.butt2]), self.outt1]))


    def filter_butt_clicked(b):
        if "1D" in b.tooltip:
            tab1.layout = Layout(border="solid gray 2px")
            with outt3:
                clear_output()
            with outt2:
                clear_output()
                d = str(dropdown.value)
                display(Markdown('Select value to be evaluated:'))
                s = selected_data.copy()
                s.remove(d)
                interact(filter_butt_clicked1, x=s);
        elif "2D" in b.tooltip:
            tab2.layout = Layout(border="solid gray 2px")
            with outt2_3:
                clear_output()
            with outt2_2:
                clear_output()
                d1 = str(dropdown2_1.value) ; d2 = str(dropdown2_2.value)
                if d1 == d2:
                    display(Markdown("Choose diferent variables!"))
                else:
                    display(Markdown('Select value to be evaluated:'))
                    s = selected_data.copy()
                    s.remove(d1) ; s.remove(d2)
                    interact(filter_butt_clicked2, x=s);



    def options_butt_clicked(b):
        if "1D" in b.tooltip:
            tab1.layout = Layout(border="solid gray 2px")
            with outt3:
                clear_output()
            with outt2:
                clear_output()
                display(Markdown('More options:'))
                w = interactive(options_butt_clicked1, x=percent, y=min_check, z=bins)
                display(self.widgets.VBox([w]))
        elif "2D" in b.tooltip:
            self.tab2.layout = Layout(border="solid gray 2px")
            with outt2_3:
                clear_output()
            with outt2_2:
                clear_output()
                display(Markdown('More options:'))
                w = interactive(options_butt_clicked2, x=percent2, y=min_check2, z=bins2)
                display(w)


    def output_butt_clicked(b):
        if "1D" in b.tooltip:
            tab1.layout = Layout(border="solid gray 2px")
            with outt3:
                clear_output()
            with outt2:
                clear_output()
                display(Markdown('Output options:'))
                global o_options
                o_options = []
                for i in range(0, len(out_checkboxes)):
                    if out_checkboxes[i].value == True:
                        w = self.widgets.Checkbox(value=True, description=out_checkboxes[i].description)
                        o_options.append(w)
                o_options.append(percent)
                display(self.widgets.VBox(o_options))
        elif "2D" in b.tooltip:
            tab1.layout = Layout(border="solid gray 2px")
            with outt2_3:
                clear_output()
            with outt2_2:
                clear_output()
                display(Markdown('Output options:'))
                global o_options2 ; w = []
                w = selected_output.copy() ; w.append('percentage')
                print(w)
                o_options2 = self.widgets.RadioButtons(options=w, value='percentage')
                display(o_options2)


    def on_butt_clicked1(b):
        if "1D" in b.tooltip:
            with outt1:
                clear_output()
                d = str(dropdown.value)
                mvalue = multiple.value ; desc = multiple.description
                b = bins.value ; nb = nbins.value
                ichk = min_check.value ; iv = min_value.value ; ivar = str(out_dropdown.value)
                show_table(d, desc, mvalue, bins=b, nbins=nb, int_check=ichk, int_var= ivar, int_value=iv)
        elif "2D" in b.tooltip:
            with outt2_1:
                clear_output()
                d1 = str(dropdown2_1.value) ; d2 = str(dropdown2_2.value) ; lst12 = [d1, d2]
                b = bins2.value ; nb = nbins2.value
                mvalue = multiple2.value ; desc = multiple2.description
                ichk = min_check2.value ; iv = min_value2.value ; ivar = str(out_dropdown2.value)
                if d1 == d2: print("Choose diferent variables!")
                else: show_table(lst12, desc, mvalue, bins=b, nbins=nb, int_check=ichk, int_var= ivar, int_value=iv)


    def on_butt_clicked2(b):
        if "1D" in b.tooltip:
            with outt1:
                d = str(dropdown.value) ; out = o_options
                mvalue = multiple.value ; desc = multiple.description
                b = bins.value ; nb = nbins.value
                ichk = min_check.value ; iv = min_value.value ; ivar = str(out_dropdown.value)
                df2 = show_table(d, desc, mvalue, disp=False, bins=b, nbins=nb, int_check=ichk, int_var= ivar, int_value=iv)
                clear_output()
                show_graphic1D(df2, d, out, desc, mvalue)
        elif "2D" in b.tooltip:
            with outt2_1:
                clear_output()
                d1 = str(dropdown2_1.value) ; d2 = str(dropdown2_2.value)
                out = str(out_dropdown2.value) ; lst12 = [d1, d2]
                if d1 == d2: print("Choose diferent variables!")
                else:
                    b = bins2.value ; nb = nbins2.value
                    mvalue = multiple2.value ; desc = multiple2.description
                    ichk = min_check2.value ; iv = min_value2.value ; ivar = str(out_dropdown2.value)
                    df2 = show_table(lst12, desc, mvalue, disp=False, bins=b, nbins=nb, int_check=ichk, int_var= ivar, int_value=iv)
                    clear_output()
                    show_graphic2D(df2, lst12, output=o_options2.value)


    def options_butt_clicked1(x, y, z):
        with outt3:
            clear_output()

            d = str(dropdown.value) ; b = bins.value
            df1 = show_table(d, bins=b, disp=False)

            global min_value
            min_value = widgets.IntRangeSlider(min=df1[out_dropdown.value].min(), max=df1[out_dropdown.value].max())
            vpercent.disabled = not x ; min_value.disabled = not y ; nbins.disabled = not z

            display(vpercent, widgets.HBox([out_dropdown, min_value]), nbins)


    def options_butt_clicked2(x, y, z):
        with outt2_3:
            clear_output()

            d1 = str(dropdown2_1.value) ; d2 = str(dropdown2_2.value) ; b = bins2.value
            lst12 = [d1, d2]
            if d1 == d2: print("Choose diferent variables!")
            else:
                df1 = show_table(lst12, bins=b, disp=False)

                global min_value2
                min_value2 = widgets.IntRangeSlider(min=df1[out_dropdown2.value].min(), max=df1[out_dropdown2.value].max())
                vpercent2.disabled = not x ; min_value2.disabled = not y ; nbins2.disabled = not z

                display(vpercent2, widgets.HBox([out_dropdown2, min_value2]), nbins2)



    def filter_butt_clicked1(x):
        with outt3:
            clear_output()

            options=df[x].unique()
            global multiple
            multiple = widgets.SelectMultiple(options=options, description=x, disabled=False)
            display(multiple)

    def filter_butt_clicked2(x):
        with outt2_3:
            clear_output()

            options=df[x].unique()
            global multiple2
            multiple2 = widgets.SelectMultiple(options=options, description=x, disabled=False)
            display(multiple2)
