const CleanWebpackPlugin = require("clean-webpack-plugin");

module.exports = {
  entry: "./src/main.js",
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ["babel-loader"]
      }
    ]
  },
  output: {
    filename: "build.[hash].js",
    path: __dirname + "/../django_project/demo/static/demo/dist"
  },
  plugins: [new CleanWebpackPlugin(["dist"])]
};
