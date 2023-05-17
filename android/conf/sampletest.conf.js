const { config: baseConfig } = require('./base.conf.js');

const parallelConfig = {
  maxInstances: 10,
  commonCapabilities: {
    'bstack:options': {
      buildName: 'Sample App',
      source: 'webdriverio:sample-master:v1.2'}
  },
  services: [
    [
      'browserstack',
      { buildIdentifier: '${BUILD_NUMBER}',
        testObservability: true,
        browserstackLocal: false,
        opts: { forcelocal: false, localIdentifier: "webdriverio-appium-app-browserstack-repo" },
        app: process.env.BROWSERSTACK_APP_PATH || 'BStackSampleApp.ipa',
        testObservabilityOptions: {
            'projectName': 'BrowserStack Samples',
            'buildName': 'Sample App',
            'buildTag': 'IOS'
        }},
      { buildIdentifier: '#${BUILD_NUMBER}' },
    ],
  ],
  capabilities: [{
    'bstack:options': {
      deviceName: 'iPhone 14',
      platformVersion: '16',
      platformName: 'ios',
    }
  }, {
    'bstack:options': {
      deviceName: 'iPhone XS',
      platformVersion: '15',
      platformName: 'ios',
    }}, {
    'bstack:options': {
      deviceName: 'iPhone 13 Pro Max',
      platformVersion: '15',
      platformName: 'ios',
    }
  }],
};

exports.config = { ...baseConfig, ...parallelConfig };

// Code to support common capabilities
exports.config.capabilities.forEach(function (caps) {
  for (var i in exports.config.commonCapabilities)
    caps[i] = { ...caps[i], ...exports.config.commonCapabilities[i]};
});
