/* global gettext */
import React from "react";
import ReactDOM from "react-dom";
import {Router, Route, useRouterHistory} from "react-router";
import {createHashHistory} from "history";

import App from "./app.jsx";
import Dashboard from "./dashboard.jsx";

class NotFound extends React.PureComponent {
  render() {
    return (
      <div>
        <h3>{gettext("Oops! You're lost.")}</h3>
        <p>{gettext("We can not find the page you're looking for.")}</p>
      </div>
    );
  }
}

let routes = (
  <Route component={App}>
    {/* Dashboard */}
    <Route path="/" component={Dashboard} />

    {/* Other */}
    <Route path="/notfound/" component={NotFound} />
    <Route path="*" component={NotFound} />
  </Route>
);

let hashHistory = useRouterHistory(createHashHistory)();

ReactDOM.render(
  <Router history={hashHistory}>{routes}</Router>,
  document.getElementsByClassName("react-root")[0]
);
