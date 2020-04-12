/* global gettext */
import React from "react";

import Ajax from "./ajax.jsx";
import AbortRequests from "../utils/abort_requests.js";

class Dashboard extends React.PureComponent {
  /* ***************************** */
  /* ** REACT LIFECYCLE METHODS ** */
  /* ***************************** */

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

  /* ***************** */
  /* ** MAIN RENDER ** */
  /* ***************** */

  render() {
    return <div>{gettext("Welcome on the Dasboard page")}</div>;
  }
}

export default Dashboard;
