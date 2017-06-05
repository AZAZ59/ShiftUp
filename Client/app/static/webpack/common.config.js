const path = require('path');
const autoprefixer = require('autoprefixer');
const postcssImport = require('postcss-import');
const merge = require('webpack-merge');

const development = require('./dev.config');
const production = require('./prod.config');

require('babel-polyfill').default;


var ExtractTextPlugin = require ('extract-text-webpack-plugin');

const TARGET = process.env.npm_lifecycle_event;

const PATHS = {
    app: path.join(__dirname, '../src'),
    build: path.join(__dirname, '../dist'),
};

process.env.BABEL_ENV = TARGET;
process.env.NODE_ENV = 'production';

const common = {
    entry: [
        PATHS.app,
    ],

    output: {
        path: PATHS.build,
        filename: 'bundle.js',
    },

    resolve: {
        extensions: ['', '.jsx', '.js', '.json', '.scss', '.css'],
        modulesDirectories: ['node_modules', PATHS.app],
    },

    module: {
        loaders: [
            { test: /\.svg$/, loader: 'url?limit=65000&mimetype=image/svg+xml&name=fonts/[name].[ext]' },
            { test: /\.woff$/, loader: 'url?limit=65000&mimetype=application/font-woff&name=fonts/[name].[ext]' },
            { test: /\.woff2$/, loader: 'url?limit=65000&mimetype=application/font-woff2&name=fonts/[name].[ext]' },
            { test: /\.[ot]tf$/, loader: 'url?limit=65000&mimetype=application/octet-stream&name=fonts/[name].[ext]' },
            { test: /\.eot$/, loader: 'url?limit=65000&mimetype=application/vnd.ms-fontobject&name=fonts/[name].[ext]' },
            {
            test: /\.js$/,
            loaders: ['babel-loader'],
            exclude: /node_modules/,
        }, {
            test: /\.png$/,
            loader: 'file?name=[name].[ext]',
        },{
            test: /\.css$/, loader: 'file?name=[name].[ext]'
        }],
    },


    postcss: (webpack) => (
        [
            autoprefixer({
                browsers: ['last 2 versions'],
            }),
            postcssImport({
                addDependencyTo: webpack,
            }),
        ]
    ),

};

if (TARGET === 'start' || !TARGET) {
    module.exports = merge(development, common);
}

if (TARGET === 'build' || !TARGET) {
    module.exports = merge(production, common);
}