
// Mock IntersectionObserver
global.IntersectionObserver = class {
    constructor(callback) {
        this.callback = callback;
    }
    observe() {}
    unobserve() {}
    disconnect() {}
};

// Import the observver from main.js
const { observer } = require('../static/js/main');

test('Observer should be defined', () => {
    expect(observer).toBeDefined();
});