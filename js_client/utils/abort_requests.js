var _ = require('lodash');

module.exports = function(requests) {
  _.forEach(requests, function(request) {
    if (request.readyState !== 4) {
      request.abort();
    }
  });
};
