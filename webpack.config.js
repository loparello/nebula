const path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,
  entry: './src/index.js',
  output: {
    filename: '[name].js',
    path: path.resolve('./assets/bundles')
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ]
}
