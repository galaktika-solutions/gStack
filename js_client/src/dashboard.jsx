/* global gettext */
var React = require("react");

var Ajax = require("./ajax.jsx");
var AbortRequests = require("../utils/abort_requests.js");

class Dashboard extends React.PureComponent {
  constructor(props) {
    super(props);
    window.title = gettext("Dashboard");
    this.requests = [];
    this.state = {
      data: []
    };
  }
  componentDidMount() {
    Ajax({
      url: "/api/core/key_value_store/",
      statusCode: {
        200: response => {
          this.setState({data: response});
          console.log(response);
        }
      }
    });
  }

  componentWillUnmount() {
    AbortRequests(this.requests);
  }

  render() {
    return <div>{gettext("Welcome on the Dasboard page")}</div>;
  }
}

module.exports = Dashboard;
