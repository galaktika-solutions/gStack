import React from "react";
import PropTypes from "prop-types";

class App extends React.PureComponent {
  render() {
    return <div>{this.props.children}</div>;
  }
}

App.propTypes = {
  children: PropTypes.any,
  location: PropTypes.object
};

export default App;
