import React from "react";
import ReactDOM from "react-dom";
import Core from './core/core.jsx';

const title = window.gettext("This is react") + " 🎉";

ReactDOM.render(<Core />, document.getElementById("app"));
