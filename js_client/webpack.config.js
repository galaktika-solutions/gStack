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
  watchOptions: {
    ignored: /node_modules/,
    poll: true
  },
  output: {
    filename: "main.[hash].js",
    path: __dirname + "/../django_project/demo/static/demo/dist"
  },
  plugins: [
    new CleanWebpackPlugin(["django_project/demo/static/demo/dist"], {
      root: "/src"
    })
  ],
  devtool: "source-map"
};
