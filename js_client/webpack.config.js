const CleanWebpackPlugin = require("clean-webpack-plugin");

module.exports = {
  entry: "./src/main.js",
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ["babel-loader"]
      },
      {
        test: /\.(png|jpg|gif)$/,
        use: ["file-loader"],
      },
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
    new CleanWebpackPlugin(["*"], {
      root: "/src/django_project/demo/static/demo/dist",
      verbose: true,
      watch: true
    })
  ],
  devtool: "source-map"
};
