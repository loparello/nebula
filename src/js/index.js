// Loads styles entry point.
import '../sass/main.scss';

/* Loads jQuery and the Bootstrap jQuery plugin which provides support
 * for JavaScript based Bootstrap features such as modals and tabs.
 */
try {
    window.Popper = require('popper.js').default;
    window.$ = window.jQuery = require('jquery');

    require('bootstrap');
} catch (error) {
    console.error(error);
}

