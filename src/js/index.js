import Vue from 'vue';
import TestComponent from './components/TestComponent';

import '../sass/main.scss';

const app = new Vue({
    el: '#app',
    components: { TestComponent }
});
