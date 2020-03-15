var PropTypes = require("prop-types");
var React = require("react");

class App extends React.PureComponent {
  render() {
    return <div>{this.props.children}</div>;
  }
}

App.propTypes = {
  children: PropTypes.any,
  location: PropTypes.object
};

module.exports = App;
