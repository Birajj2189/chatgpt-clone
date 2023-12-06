/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,htm}",
    "./static/src/**/*.js"
],
  theme: {
    extend: {
      colors: {
        'white': '#ffffff',
        'grey': '#202023',
        'dark-white': '#f7f7f8',
      },
    },
  },

}

