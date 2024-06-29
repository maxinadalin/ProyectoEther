// webpack.config.js

const path = require('path');

module.exports = {
  resolve: {
    fallback: {
      "domain": require.resolve("domain-browser"),
      "os": require.resolve("os-browserify/browser"),
      "util": require.resolve("util/"),
      // Agrega más polyfills según sea necesario para otros módulos
    },
  },
  // Otras configuraciones de webpack si las necesitas
};
