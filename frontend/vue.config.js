// const BundleTracker = require("webpack-bundle-tracker");
// module.exports = {
//   // 如果不在windows环境请试下: "http://0.0.0.0:8080/"
//   publicPath: "http://127.0.0.1:8080",
//   outputDir: "./dist/",

//   chainWebpack: (config) => {
//     config
//       .plugin("BundleTracker")
//       .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);

//     config.output.filename("bundle.js");

//     config.optimization.splitChunks(false);

//     config.resolve.alias.set("__STATIC__", "static");

//     config.devServer
//       // the first 3 lines of the following code have been added to the configuration
//       .public("http://127.0.0.1:8080")
//       .host("127.0.0.1")
//       .port(8080)
//       .hotOnly(true)
//       .watchOptions({ poll: 1000 })
//       .https(false)
//       .disableHostCheck(true)
//       .headers({ "Access-Control-Allow-Origin": ["*"] });
//   },
// };
const fs = require("fs");

module.exports = {
  runtimeCompiler: true,
  publicPath: "/",
  devServer: {
    // public: "xxx.com",
    host: "0.0.0.0",
    disableHostCheck: true,
    // https: true,
    // key: fs.readFileSync("./ssh/private.key"),
    // cert: fs.readFileSync("./ssh/certificate.crt"),
    // ca: fs.readFileSync("./ssh/ca_bundle.crt"),
    proxy: {
      "/api": {
        // target: `http://localhost:8000/api`,
        target: `http://django:8000/api`,
        changeOrigin: true,
        pathRewrite: {
          "^/api": "",
        },
      },
    },
  },
};
