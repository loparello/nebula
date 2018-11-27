const path = require('path')
const BundleTracker = require('webpack-bundle-tracker')
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const { VueLoaderPlugin } = require('vue-loader');
const CleanWebpackPlugin = require('clean-webpack-plugin');

module.exports = (env, argv) => { 
  console.log(argv.mode);
  const isProduction = argv.mode === 'production';
  const outputPath = isProduction ? path.resolve('./dist/build') : path.resolve('./dist/dev');
  
  return {
    context: __dirname,
    entry: {
      main: './src/js/index.js'
    },
    output: {
      filename: isProduction ? '[name].[chunkhash].bundle.js' : '[name].bundle.js',
      path: outputPath
    },
    optimization: {
      splitChunks: {
        chunks: 'all'
      }
    },

    devtool: isProduction ? false : 'source-map',
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
  };
};
