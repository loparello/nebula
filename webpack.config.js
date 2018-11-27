const path = require('path')
const BundleTracker = require('webpack-bundle-tracker')
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const { VueLoaderPlugin } = require('vue-loader');
const CleanWebpackPlugin = require('clean-webpack-plugin');

const env = process.env.NODE_ENV;
const outputFilename = (env === 'production') ? '[name].[chunkhash].bundle.js' : '[name].bundle.js'
const outputPath = (env === 'production') ? path.resolve('./dist/build') : path.resolve('./dist/dev');

module.exports = {
  context: __dirname,
  entry: {
    main: './src/js/index.js'
  },
  output: {
    filename: outputFilename,
    path: outputPath
  },
  optimization: {
    splitChunks: {
      chunks: 'all'
    }
  },

  devtool: 'source-map',
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      },
      {
        test: /\.(png|jpe?g)/i,
        use: [
            {
                loader: 'url-loader',
                options: {
                    name: './img/[name].[ext]',
                    limit: 10000
                }
            },
            {
                loader: 'img-loader'
            }
        ]
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader', options: {
                sourceMap: true
            }
          },
          {
            loader: 'sass-loader', options: {
                sourceMap: true
            }
          }
        ]
      }
    ]
  },

  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    },
    extensions: ['*', '.js', '.vue', '.json']
  },

  plugins: [
    new CleanWebpackPlugin([outputPath]),
    new BundleTracker({filename: './webpack-stats.json'}),
    new MiniCssExtractPlugin({
      filename: '[name].bundle.css',
      chunkFilename: '[id].bundle.css'
    }),
    new VueLoaderPlugin()
  ]

}
