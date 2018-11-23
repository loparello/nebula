const path = require('path')

module.exports = {
  entry: './resources/index.js',
  output: {
    filename: 'app.js',
    path: path.resolve(__dirname, 'nebula/static/js')
  }
}
