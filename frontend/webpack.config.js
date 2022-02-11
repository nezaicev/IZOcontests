module.exports = {
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

            }
        ]
    }
};