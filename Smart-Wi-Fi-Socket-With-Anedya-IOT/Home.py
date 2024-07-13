import streamlit as st
import pandas as pd
import altair as alt
from streamlit_autorefresh import st_autorefresh

from utils.anedya import anedya_config
from utils.anedya import anedya_sendCommand
from utils.anedya import anedya_getValue
from utils.anedya import anedya_setValue
from utils.anedya import fetchHumidityData
from utils.anedya import fetchTemperatureData

nodeId = "0190aaa5-20cc-7a9e-843e-9c803a5343df"  # get it from anedya dashboard -> project -> node 
apiKey = "ddf16e7a59f2d5f3e45a9661ef39b01487f847ddad21e75ecaa2d8b909c7baf3"  # aneyda project apikey

st.set_page_config(page_title="Smart Wi-Fi Socket With Anedya IOT", layout="wide")


st_autorefresh(interval=10000, limit=None, key="auto-refresh-handler")

# --------------- HELPER FUNCTIONS -----------------------


def V_SPACE(lines):
    for _ in range(lines):
        st.write("&nbsp;")


humidityData = pd.DataFrame()
temperatureData = pd.DataFrame()


def main():

    anedya_config(nodeId, apiKey)
    global humidityData, temperatureData

    # Initialize the log in state if does not exist
    if "LoggedIn" not in st.session_state:
        st.session_state.LoggedIn = False

    if "FanButtonText" not in st.session_state:
        st.session_state.FanButtonText = "Turn Fan On!"

    if "LightButtonText" not in st.session_state:
        st.session_state.LightButtonText = "Turn Light On!"

    if "LightState" not in st.session_state:
        st.session_state.LightState = False

    if "FanState" not in st.session_state:
        st.session_state.FanState = False

    if "CurrentHumidity" not in st.session_state:
        st.session_state.CurrentHumidity = 0

    if "CurrentTemperature" not in st.session_state:
        st.session_state.CurrentTemperature = 0

    if st.session_state.LoggedIn is False:
        drawLogin()
    else:
        humidityData = fetchHumidityData()
        temperatureData = fetchTemperatureData()

        GetFanStatus()
        GetLightStatus()

        drawDashboard()


def drawLogin():
    cols = st.columns([1, 0.8, 1], gap='small')
    with cols[0]:
        pass
    with cols[1]:
        st.title("Smart Wi-Fi Socket With Anedya IOT", anchor=False)
        username_inp = st.text_input("Username")
        password_inp = st.text_input("Password", type="password")
        submit_button = st.button(label="Submit")

        if submit_button:
            if (username_inp == "astha" or "manav") and (password_inp == "astha" or "manav"):
                st.session_state.LoggedIn = True
                st.rerun()
            else:
                st.error("Invalid Credential!")
    with cols[2]:
        print()


def drawDashboard():
    headercols = st.columns([1, 0.1, 0.1], gap="small")
    with headercols[0]:
        st.title("Smart Wi-Fi Socket With Anedya IOT", anchor=False)
    with headercols[1]:
        st.button("Refresh")
    with headercols[2]:
        logout = st.button("Logout")

    if logout:
        st.session_state.LoggedIn = False
        st.rerun()

    st.markdown("Allowing you to control the connected device remotely!")

    st.subheader(body="Current Status", anchor=False)
    cols = st.columns(2, gap="medium")
    
    # with cols[2]:
    #    st.metric(label="Refresh Count", value=count)

    buttons = st.columns(2, gap="small")
    with buttons[0]:
        st.text("Control Socket1")
        st.button(label=st.session_state.FanButtonText, on_click=operateFan)
    with buttons[1]:
        st.text("Control Socket2")
        st.button(label=st.session_state.LightButtonText, on_click=operateLight)

    charts = st.columns(2, gap="small")
   

    

           


def operateFan():
    if st.session_state.FanState is False:
        anedya_sendCommand("fan", "ON")
        anedya_setValue("fan", True)
        st.session_state.FanButtonText = "Turn Socket1 Off!"
        st.session_state.FanState = True
        st.toast("Socket1 turned on!")
    else:
        st.session_state.FanButtonText = "Turn Socket1 On!"
        st.session_state.FanState = False
        anedya_sendCommand("fan", "OFF")
        anedya_setValue("fan", False)
        st.toast("Socket1 turned off!")


def operateLight():
    if st.session_state.LightState is False:
        anedya_sendCommand("light", "ON")
        anedya_setValue("light", True)
        st.session_state.LightButtonText = "Turn Socket2 Off!"
        st.session_state.LightState = True
        st.toast("Socket2 turned on!")
    else:
        anedya_sendCommand("light", "OFF")
        anedya_setValue("light", False)
        st.session_state.LightButtonText = "Turn Socket2 On!"
        st.session_state.LightState = False
        st.toast("Socket2 turned off!")


@st.cache_data(ttl=4, show_spinner=False)
def GetFanStatus() -> list:
    value = anedya_getValue("fan")
    if value[1] == 1:
        on = value[0]
        if on:
            st.session_state.FanState = True
            st.session_state.FanButtonText = "Turn Socket1 Off!"
        else:
            st.session_state.FanState = False
            st.session_state.FanButtonText = "Turn Socket1 On!"
    return value


@st.cache_data(ttl=4, show_spinner=False)
def GetLightStatus() -> list:
    value = anedya_getValue("light")
    if value[1] == 1:
        on = value[0]
        if on:
            st.session_state.LightState = True
            st.session_state.LightButtonText = "Turn Socket2 Off!"
        else:
            st.session_state.LightState = False
            st.session_state.LightButtonText = "Turn Socket2 On!"
    return value


if __name__ == "__main__":
    main()
