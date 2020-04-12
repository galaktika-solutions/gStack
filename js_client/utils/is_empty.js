var _ = require('lodash');

/**
 * Check the value if its empty or not.
 * @param {any} value - value to check
 * @return {Boolean} - True/False
 */
module.exports = function (value) {
  if (typeof value === 'object') {
    return _.isEmpty(value);
  }
  if (value instanceof Array) {
    return value.length === 0;
  }
  return (typeof value === 'undefined' ||
          value === '' ||
          value === null);
};
