/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "../templates/*.html",
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    // colors: {
    //   "drk": '#2A2A2A',
    //   "blue": '#87CEEB',
    //   "yellow": '#FFD700',
    //   "green": '#98FB98',
    //   "red": '#FFA07A',
    // },
    extend: {
      colors: {
        "drk": '#2A2A2A',
        "drk-accent": '#3A3A3A',
        "blue": '#87CEEB',
        "yellow": '#FFD700',
        "green": '#98FB98',
        "red": '#FFA07A',
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

