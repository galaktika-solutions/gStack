/* global gettext */
var React = require("react");

class Dashboard extends React.PureComponent {
  render() {
    return <div className="content">{gettext("Welcome on the Dasboard page")}</div>;
  }
}

module.exports = Dashboard;
