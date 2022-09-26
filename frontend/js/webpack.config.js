
const Dotenv = require('dotenv-webpack');

module.exports = {
    plugins: [
    new Dotenv()
  ],
    resolve: {
        fallback: {
            "process": require.resolve("process/browser"),

        },


    },

    module: {
        rules: [
            {
                test: [/\.js$/, /\.svg$/,],
                exclude: /node_modules/,
                use: [{
                    loader: "babel-loader"
                },],

            },
             {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
        ]
    }
};