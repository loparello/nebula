import Vue from 'vue';

import TestComponent from './components/TestComponent';

import '../sass/main.scss';

try {
    window.Popper = require('popper.js').default;
    window.$ = window.jQuery = require('jquery');

    require('bootstrap');
} catch (error) {
    console.error(error);
}

const app = new Vue({
    el: '#app',
    components: { TestComponent }
});
