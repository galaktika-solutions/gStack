/* global gettext */
var React = require("react");

var Ajax = require("./ajax.jsx");

class Dashboard extends React.PureComponent {
  componentDidMount() {
    Ajax({
      url: "/api/core/key_value_store/",
      statusCode: {
        200: response => {
          console.log(response);
        }
      }
    });
  }

  render() {
    return <div className="content">{gettext("Welcome on the Dasboard page")}</div>;
  }
}

module.exports = Dashboard;
