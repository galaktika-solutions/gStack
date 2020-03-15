module.exports = {
  entry: "./src/router.jsx",
  output: {
    filename: "build.js",
    path: __dirname + "/../django_project/core/static"
  },
  watchOptions: {
    ignored: /node_modules/,
    poll: true
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ["babel-loader"]
      }
    ]
  },
  performance: {
    maxEntrypointSize: 5242880,
    maxAssetSize: 5242880
  }
};
