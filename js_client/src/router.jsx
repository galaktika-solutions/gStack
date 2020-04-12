/* global gettext */
import React from "react";
import ReactDOM from "react-dom";
import {HashRouter as Router, Switch, Route} from "react-router-dom";

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

ReactDOM.render(
  <Router>
    <App>
      <Switch>
        {/* Dashboard */}
        <Route exact path="/" component={Dashboard} />

        {/* Other */}
        <Route path="/notfound/" component={NotFound} />
        <Route path="*" component={NotFound} />
      </Switch>
    </App>
  </Router>,
  document.getElementsByClassName("react-root")[0]
);
