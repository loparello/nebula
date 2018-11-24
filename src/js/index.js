import '../sass/main.scss';

const test = () => {
    const root = document.getElementById('test');
    root.innerHTML = '<p>Hello Webpack.</p>';
    console.log('Webpack is loading');
};

test();
