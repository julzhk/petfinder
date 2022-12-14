module.exports = {
    mode: 'jit',
    purge: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}"
    ],
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {},
    },
    plugins: [],
}
