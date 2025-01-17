# -*- coding: utf-8 -*-
# Copyright 2018-2019 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A "Hello World" app."""

from __future__ import division, unicode_literals

import inspect
import textwrap
from collections import OrderedDict

import streamlit as st
from streamlit.logger import get_logger
from streamlit.hello import demos

LOGGER = get_logger(__name__)

# Dictionary of
# demo_name -> (demo_function, demo_description)
DEMOS = OrderedDict(
    [
        ("—", (demos.intro, None)),
        (
            "Animation Demo",
            (
                demos.fractal_demo,
                """
This demo shows how to use
[`st.deck_gl_chart`](https://streamlit.io/docs/api.html#streamlit.deck_gl_chart)
to display geospatial data.
""",
            ),
        ),
        (
            "Plotting Demo",
            (
                demos.plotting_demo,
                """
This app shows how you can use Streamlit to build cool animations.
It displays an animated fractal based on the the Julia Set. Use the slider
to tune different parameters.
""",
            ),
        ),
        (
            "Mapping Demo",
            (
                demos.mapping_demo,
                """
This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!
""",
            ),
        ),
        (
            "DataFrame Demo",
            (
                demos.data_frame_demo,
                """
This demo shows how to use `st.write` to visualize Pandas DataFrames.

(Data courtesy of the [UN Data Exlorer](http://data.un.org/Explorer.aspx).)
""",
            ),
        ),
    ]
)


def run():
    demo_name = st.sidebar.selectbox("Choose a demo", list(DEMOS.keys()), 0)
    demo = DEMOS[demo_name][0]

    if demo_name == "—":
        show_code = False
        st.write("# Welcome to Streamlit! 👋")
    else:
        show_code = st.sidebar.checkbox("Show code", True)
        st.markdown("# %s" % demo_name)
        description = DEMOS[demo_name][1]
        if description:
            st.write(description)
        # Clear everything from the intro page.
        # We only have 4 elements in the page so this is intentional overkill.
        for i in range(10):
            st.empty()

    demo()

    if show_code:
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))


if __name__ == "__main__":
    run()
