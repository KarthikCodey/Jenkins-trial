const { config: baseConfig } = require('./base.conf.js');

const parallelConfig = {
  maxInstances: 10,
  commonCapabilities: {
    'bstack:options': {
      buildName: 'browserstack build',
      source: 'webdriverio:sample-master:v1.2'}
  },
  services: [
    [
      'browserstack',
      { buildIdentifier: '${BUILD_NUMBER}',
        testObservability: true,
        browserstackLocal: true,
        opts: { forcelocal: false, localIdentifier: "webdriverio-appium-app-browserstack-repo" },
        app: process.env.BROWSERSTACK_APP_PATH || './android/examples/wikipedia1.apk',
        testObservabilityOptions: {
            'projectName': 'BrowserStack Samples',
            'buildName': 'browserstack build',
            'buildTag': 'WDIO'
        }},
      { buildIdentifier: '#${BUILD_NUMBER}' },
    ],
  ],
  capabilities: [{
    'bstack:options': {
      deviceName: 'Samsung Galaxy S22 Ultra',
      platformVersion: '12.0',
      platformName: 'android',
    }
  }, {
    'bstack:options': {
      deviceName: 'Google Pixel 7 Pro',
      platformVersion: '13.0',
      platformName: 'android',
    }}, {
    'bstack:options': {
      deviceName: 'OnePlus 9',
      platformVersion: '11.0',
      platformName: 'android',
    }
  }],
};

exports.config = { ...baseConfig, ...parallelConfig };

// Code to support common capabilities
exports.config.capabilities.forEach(function (caps) {
  for (var i in exports.config.commonCapabilities)
    caps[i] = { ...caps[i], ...exports.config.commonCapabilities[i]};
});
