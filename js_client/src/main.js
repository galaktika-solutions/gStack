import React from "react";
import ReactDOM from "react-dom";

const title = window.gettext("This is react") + " 🎉";

ReactDOM.render(<div>{title}</div>, document.getElementById("app"));
