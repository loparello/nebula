import Vue from 'vue';

import Jumbotron from './components/Jumbotron';

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
    components: { Jumbotron }
});
