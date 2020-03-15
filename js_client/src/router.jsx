/* global gettext */
var React = require("react");
var ReactDOM = require("react-dom");
var ReactRouter = require("react-router");
var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var useRouterHistory = ReactRouter.useRouterHistory;
var createHashHistory = require("history").createHashHistory;

var App = require("./app.jsx");
var Dashboard = require("./dashboard.jsx");

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

var routes = (
  <Route component={App}>
    {/* Dashboard */}
    <Route path="/" component={Dashboard} />

    {/* Other */}
    <Route path="/notfound/" component={NotFound} />
    <Route path="*" component={NotFound} />
  </Route>
);

var history = useRouterHistory(createHashHistory)();

ReactDOM.render(
  <Router history={history}>{routes}</Router>,
  document.getElementsByClassName("react-root")[0]
);
