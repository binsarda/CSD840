import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt
import base64


col1, col2, col3 = st.columns([1, 8, 1])
tab_titles=[
    "Home",
    "Modelling Framework",
    "Numerical Analysis"

]
tabs=st.tabs(tab_titles)

###################
with tabs[0]:
    st.markdown("# !!!! Welcome to my website !!!!")
    col1, col2, col3 = st.columns([1, 2, 1])

    logo = Image.open('msu_logo.png')
    col1.image(logo, caption='MSU')

    egr = Image.open('msu.png')
    egr = egr.resize((1000, 1000))
    col3.image(egr, caption='Spartans')

    fmath = Image.open('fmath_logo.png')


    button_home_sidbar_status = True

    button_home_sidbar = col1.button(":red[Show Github Link]")


    if col3.button(":red[Hide Github Link]"):
        button_home_sidbar_status= False
        button_home_sidbar = False

    if button_home_sidbar_status | button_home_sidbar:
        st.sidebar.write("My github link: [link](https://github.com/binsarda?tab=repositories)")
        st.sidebar.image(fmath, caption=' Fractional Mathematics for Anomalous Transport and Hydromechanics (FMATH) group')





    col1, col2, col3 = st.columns([1, 2, 1])
    col1.write("Owner Name: Sardar Nafis Bin Ali")
    col3.write("Institution: Michigan State University")
    st.markdown("# :red[Click below to know about the author of this site!]")
    with st.expander(label=("# :violet[Click here to know about the author of this site!]"),expanded=False):
        nafispic = Image.open('nafis.jpg')
        st.image(nafispic, caption='Sardar Nafis Bin Ali')
        st.write("Sardar is driven by a thirst for knowledge and has a spirit of exploration. "
                 "He focused on the captivating domain of high-speed aerodynamics during his undergraduate "
                 "studies in mechanical engineering. Currently, he is pursuing "
                 "a Ph.D. in mechanical engineering and planning to do a dual "
                 " degree with the department of communicative sciences and "
                 "disorders. He aims to learn about the intricate aspects of "
                 "human communication and contribute to advancements in voice science. "
                 " Apart from his academic pursuits, he finds solace in traveling, "
                 "embracing diverse cultures, and capturing the world's beauty through "
                 "his experiences. Sardar actively engages in initiatives "
                 "promoting sustainability and environmental conservation. "
                 "With an unquenchable curiosity and unwavering dedication, "
                 "he continues to make a meaningful impact in his chosen fields and beyond. ")

    st.markdown("# :red[Objective]")
    st.write("In this website, a tool is presented to simulate vocal fold motion. Two opposing vocal folds are modelled with one mass "
             "for each vocal fold. Their visco elastic properties are modelled with spring and damper. There are several options available "
             "for changing various parameters. By using the model, effect of various different parameters on vocal fold motion can be "
             "observed. It can be used as a research tool for studying voice disorders. "
             )

with tabs[1]:
    st.markdown("# :violet[Modelling Framework]")
    st.write("Vocal folds are modelled with lumped elements. Two opposing vocal folds are modelled. Each vocal fold is modelled with "
             "single mass-spring-damper system. The working principle aligns with myoelastic aerodynamic theory of phonation. Initially "
             "the vocal folds are in contact with each other. Air cannot escape from lungs in this situation. Air pressure builds up "
             "in the lungs. This build up of air pressure moves the vocal folds apart from each other. As a result, vocal folds starts "
             "opening. Their opening creates a path for airflow to take place. As air flows between the vocal folds, static pressure working "
             "on the vocal folds decrease due to formation of dynamic pressure according to Bernoulli's principle. This reduction in static "
             "pressure along with the elastic recoil force brings the vocal folds close to each other again. So, they become closed again. "
             "That is how a glottal cycle is cmpleted. After they are in contact with each other, they start moves away from each other "
             "again due to build up of air pressure in lungs. So, glottal cycles are repeated. ")

    st.markdown("## :violet[Detailed Modelling]")



    def show_pdf(file_path, width=700, height=1000):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="{width}" height="{height}" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)



    pdf_file_path = 'Sardar_Nafis_presentation.pdf'

    show_pdf(pdf_file_path, width=1000, height=1000)







###################

with tabs[2]:
    ################## model start

    st.markdown("# :violet[Numerical Analysis]")

    m1 = st.slider('Select the value for Mass 1 in gram', min_value=0.0, max_value=0.25, value=0.12, step=0.01)  # input
    m2 = st.slider('Select the value for Mass 2 in gram', min_value=0.0, max_value=0.25, value=0.12, step=0.01)  # input

    k1_lar = st.slider('Select the value for Elasticity 1 in N/m', min_value=1, max_value=2000, value=200,
                       step=1)  # input
    k2_lar = st.slider('Select the value for Elasticity 2 in N/m', min_value=1, max_value=2000, value=200,
                       step=1)  # input

    k1 = k1_lar * (10 ** 3)
    k2 = k2_lar * (10 ** 3)

    c1min = st.slider('Select the value for minimum Damping Co efficient 1 in gram/sec', min_value=0, max_value=25,
                      value=0, step=1)  # input
    c2min = st.slider('Select the value for minimum Damping Co efficient 2 in gram/sec', min_value=0, max_value=25,
                      value=0, step=1)  # input

    delc1 = st.slider('Select the value for difference of min and max Damping Co efficient 1 in gram/sec', min_value=0,
                      max_value=250, value=10, step=1)  # input
    delc2 = st.slider('Select the value for difference of min and max Damping Co efficient 2 in gram/sec', min_value=0,
                      max_value=250, value=10, step=1)  # input

    c1max = c1min + delc1
    c2max = c2min + delc2

    ps = st.slider('Select the value for minimum sub-glottal pressure', min_value=1000, max_value=8000, value=8000,
                   step=100)  # input
    delps = st.slider('Select the value for difference of min and max sub-glottal pressure', min_value=0,
                      max_value=4000, value=600, step=100)  # input
    psmax = ps + delps

    tc_s = st.slider('Select the value for closure time*(1/4) in milli sec', min_value=3, max_value=25, value=12,
                     step=1)  # input
    tc = tc_s / 4000

    l = 1.4
    d = 0.32

    rho = 1.3 * (10 ** (-3))
    mu = 1.8 * (10 ** (-4))

    Ag0 = 0.05
    x0 = -(Ag0 / (2 * l))

    ti = 0
    xi = x0
    vi = 0

    tfinal = .1  # input
    dtframe = (1 / 4000)
    dtfactor = 256
    dt = dtframe / dtfactor
    dtcontrol = 1 * dt

    steps = round((tfinal - ti) / dt)

    y1 = np.zeros((steps + 1, 3))
    y2 = np.zeros((steps + 1, 3))
    y1[0, :] = [ti, xi, vi]
    y2[0, :] = [ti, xi, vi]

    zone_id = 4
    c_counter = 0

    close_steady = 0
    y1_c = x0
    y2_c = x0

    for i in range(steps):
        if zone_id == 1:
            C1 = c1min
            C2 = c2min
            P = ps

            Ag = Ag0 + l * y1[i, 1] + l * y2[i, 1]

            if Ag <= 0:
                Pb = 0
            elif Ag > 0:
                a_q = (0.875 * rho / (2 * Ag ** 2))
                b_q = (12 * mu * d * (l ** 2) / (Ag ** 3))
                c_q = (-P)
                Q = -(b_q / (2 * a_q)) + (np.sqrt((b_q ** 2) - 4 * a_q * c_q)) / (2 * a_q)
                V_air = Q / Ag
                Pb = 0.5 * rho * (V_air ** 2)

            P1 = P - 1.37 * Pb
            P2 = -0.5 * Pb

            F_aero = 0.5 * l * d * (P1 + P2)

            acc1 = (1 / m1) * (F_aero - k1 * y1[i, 1] - C1 * y1[i, 2])
            acc2 = (1 / m2) * (F_aero - k2 * y2[i, 1] - C2 * y2[i, 2])

            y1[i + 1, 1] = y1[i, 1] + y1[i, 2] * dt
            y2[i + 1, 1] = y2[i, 1] + y2[i, 2] * dt

            y1[i + 1, 2] = y1[i, 2] + acc1 * dt
            y2[i + 1, 2] = y2[i, 2] + acc2 * dt

            if F_aero >= 0:
                zone_id = 2

            continue





        elif zone_id == 2:
            C1 = (c1min + c1max) / 2
            C2 = (c2min + c2max) / 2
            P = (ps+psmax)/2

            Ag = Ag0 + l * y1[i, 1] + l * y2[i, 1]

            acc1 = (1 / m1) * (-k1 * y1[i, 1] - C1 * y1[i, 2])
            acc2 = (1 / m2) * (-k2 * y2[i, 1] - C2 * y2[i, 2])

            y1[i + 1, 1] = y1[i, 1] + y1[i, 2] * dt
            y2[i + 1, 1] = y2[i, 1] + y2[i, 2] * dt

            y1[i + 1, 2] = y1[i, 2] + acc1 * dt
            y2[i + 1, 2] = y2[i, 2] + acc2 * dt

            Ag_next = Ag0 + l * y1[i + 1, 1] + l * y2[i + 1, 1]

            if Ag_next > 0 and Ag_next > Ag:
                zone_id = 1
            elif Ag_next <= 0:
                zone_id = 3

            continue

        elif zone_id == 3:
            c_counter = c_counter + dt

            C1 = c1max
            C2 = c2max
            P = psmax

            Ag = Ag0 + l * y1[i, 1] + l * y2[i, 1]

            F_aero = 0.5 * (P) * l * d

            if close_steady == 0:
                acc1 = (1 / m1) * (F_aero - k1 * y1[i, 1] - C1 * y1[i, 2])
                acc2 = (1 / m2) * (F_aero - k2 * y2[i, 1] - C2 * y2[i, 2])

                y1[i + 1, 1] = y1[i, 1] + y1[i, 2] * dt
                y2[i + 1, 1] = y2[i, 1] + y2[i, 2] * dt

                y1[i + 1, 2] = y1[i, 2] + acc1 * dt
                y2[i + 1, 2] = y2[i, 2] + acc2 * dt
            elif close_steady == 1:
                y1[i + 1, 1] = y1_c
                y2[i + 1, 1] = y2_c

                y1[i + 1, 2] = v1_c
                y2[i + 1, 2] = v2_c

            Ag_next = Ag0 + l * y1[i + 1, 1] + l * y2[i + 1, 1]

            if Ag_next >= 0:
                close_steady = 1
                y1_c = y1[i, 1]
                y2_c = y2[i, 1]
                v1_c = 0
                v2_c = 0

                y1[i + 1, 1] = y1_c
                y2[i + 1, 1] = y2_c

                y1[i + 1, 2] = v1_c
                y2[i + 1, 2] = v2_c

            if c_counter >= tc:
                zone_id = 4
                c_counter = 0
                close_steady = 0
            continue

        elif zone_id == 4:
            C1 = (c1min + c1max) / 2
            C2 = (c2min + c2max) / 2
            P = (ps+psmax)/2

            Ag = Ag0 + l * y1[i, 1] + l * y2[i, 1]

            if Ag <= 0:
                Pb = 0
            elif Ag > 0:
                a_q = (0.875 * rho / (2 * Ag ** 2))
                b_q = (12 * mu * d * (l ** 2) / (Ag ** 3))
                c_q = (-P)
                Q = -(b_q / (2 * a_q)) + (np.sqrt((b_q ** 2) - 4 * a_q * c_q)) / (2 * a_q)
                V_air = Q / Ag
                Pb = 0.5 * rho * (V_air ** 2)

            P1 = P - 1.37 * Pb
            P2 = -0.5 * Pb

            F_aero = 0.5 * l * d * (P1 + P2)

            acc1 = (1 / m1) * (F_aero - k1 * y1[i, 1] - C1 * y1[i, 2])
            acc2 = (1 / m2) * (F_aero - k2 * y2[i, 1] - C2 * y2[i, 2])

            y1[i + 1, 1] = y1[i, 1] + y1[i, 2] * dt
            y2[i + 1, 1] = y2[i, 1] + y2[i, 2] * dt

            y1[i + 1, 2] = y1[i, 2] + acc1 * dt
            y2[i + 1, 2] = y2[i, 2] + acc2 * dt

            if F_aero <= 0:
                zone_id = 1

            continue

    Ag_simtotal = 100 * (Ag0 + l * y1[:, 1] + l * y2[:, 1])

    #############Figures

    fig1 = go.Figure()

    # Add Sine wave plot
    fig1.add_trace(
        go.Scatter(x=1000 * np.linspace(0, tfinal, steps + 1), y=10 * y1[:, 1], mode='lines', name='VF1 Displacement',
                   line=dict(color='blue', width=2, dash='solid')))

    # Add Cosine wave plot
    fig1.add_trace(
        go.Scatter(x=1000 * np.linspace(0, tfinal, steps + 1), y=10 * y2[:, 1], mode='lines', name='VF2 Displacement',
                   line=dict(color='red', width=3, dash='dot')))
    fig1.add_trace(
        go.Scatter(x=1000 * np.linspace(0, tfinal, steps + 1), y=10 * x0 * np.ones(Ag_simtotal.size), mode='lines',
                   name='Midline',
                   line=dict(color='green', width=2, dash='dash')))
    # Enhance the figure with titles and labels
    fig1.update_layout(title='Displacements of 2 opposing vocal folds',
                       xaxis_title='Time(ms)',
                       yaxis_title='Displacement(mm)',
                       template='plotly_white',
                       #legend_title='Wave Type',
                       width=1200,  # Custom width in pixels
                       height=500)  # Custom height in pixels

    # Display the figure in the Streamlit app
    st.plotly_chart(fig1)

    y1_mod = y1[:, 1] - x0
    y2_mod = y2[:, 1] - x0
    y2_mod = -y2_mod

    fig2 = go.Figure()

    # Add Sine wave plot
    fig2.add_trace(
        go.Scatter(x=1000 * np.linspace(0, tfinal, steps + 1), y=10 * y1_mod, mode='lines', name='VF1 Displacement',
                   line=dict(color='blue', width=2, dash='solid')))

    # Add Cosine wave plot
    fig2.add_trace(
        go.Scatter(x=1000 * np.linspace(0, tfinal, steps + 1), y=10 * y2_mod, mode='lines', name='VF2 Displacement',
                   line=dict(color='red', width=3, dash='dot')))
    fig2.add_trace(
        go.Scatter(x=1000 * np.linspace(0, tfinal, steps + 1), y=10 * 0 * np.ones(Ag_simtotal.size), mode='lines',
                   name='Midline',
                   line=dict(color='green', width=2, dash='dash')))
    # Enhance the figure with titles and labels
    fig2.update_layout(title='Displacements of 2 opposing vocal folds with respect to  x<sub>0</sub> or midline ',
                       xaxis_title='Time(ms)',
                       yaxis_title='Displacement(mm)',
                       template='plotly_white',
                       #legend_title='Wave Type',
                       width=1200,  # Custom width in pixels
                       height=500)  # Custom height in pixels

    # Display the figure in the Streamlit app
    st.plotly_chart(fig2)

    fig3 = go.Figure()

    # Add Sine wave plot
    fig3.add_trace(go.Scatter(x=1000 * np.linspace(0, tfinal, steps + 1), y=Ag_simtotal, mode='lines',
                              line=dict(color='blue', width=2, dash='solid')))

    fig3.update_layout(title='Glottal Area vs Time',
                       xaxis_title='Time(ms)',
                       yaxis_title='Glottal Area (mm<sup>2</sup>)',
                       template='plotly_white',

                       width=1200,  # Custom width in pixels
                       height=500)  # Custom height in pixels

    # Display the figure in the Streamlit app
    st.plotly_chart(fig3)
    ################## model end

