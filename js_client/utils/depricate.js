module.exports = function(message) {
  if (process.env.NODE_ENV === 'development') {
    console.warn(message); // eslint-disable-line no-console
  }
};
